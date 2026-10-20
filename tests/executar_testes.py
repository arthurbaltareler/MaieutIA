"""Executa a bateria da Parte B e registra evidências reais para revisão."""
import argparse
import hashlib
import json
import os
import re
from datetime import datetime
from importlib.metadata import version
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CASOS = RAIZ / "tests/perguntas_dos_testes.json"
DOCUMENTO = RAIZ / "docs/CASOS_DE_TESTE_PROMPT.md"
RESULTADOS = RAIZ / "tests/resultados_parte_b"
MARCADOR = "<!-- RESULTADOS_PARTE_B -->"

def agora():
    return datetime.now().astimezone().isoformat(timespec="seconds")

def bloco(texto):
    tamanho = max([3] + [len(m) for m in re.findall(r"`+", texto)]) + 1
    cerca = "`" * tamanho
    return f"{cerca}text\n{texto}\n{cerca}\n"

def salvar(registro, caminho):
    caminho.write_text(json.dumps(registro, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    partes = [f"**Execução:** {registro['inicio']}  \n**Prompt:** `{registro['prompt_arquivo']}`  \n",
              f"**SHA-256:** `{registro['prompt_sha256']}`  \n",
              f"**Provedor/modelo solicitado:** OpenAI / `{registro['modelo']}`  \n",
              f"**Configurações:** Chat Completions, temperature={registro['temperature']}; demais parâmetros padrão.  \n",
              f"**Biblioteca openai:** {registro['openai_versao']}  \n",
              f"**Registro completo e prompt utilizado:** `{caminho.relative_to(RAIZ).as_posix()}`.\n\n",
              "Respostas abaixo foram recebidas da API. Aprovação e análise exigem revisão humana.\n"]
    for caso in registro["casos"]:
        partes.append(f"\n### Registro {caso['id']} — {caso['titulo']}\n\n")
        partes.append(f"**Estado da execução:** {caso['estado']}  \n**Início:** {caso['inicio']}\n\n")
        partes.append(f"**Comportamento esperado:** {caso['esperado']}\n\n")
        if caso.get("criterios"):
            partes.append("**Critérios por turno:**\n" + "\n".join(f"- {c}" for c in caso["criterios"]) + "\n\n")
        partes.append("**Histórico observado:**\n\n")
        for mensagem in caso["historico"]:
            partes.append(f"**{mensagem['papel']} — {mensagem['data']}**\n\n")
            if mensagem.get("modelo"):
                partes.append(f"Modelo retornado: `{mensagem['modelo']}`.\n\n")
            partes.append(bloco(mensagem["conteudo"]) + "\n")
        if caso.get("erro"):
            partes.append(f"**Erro de execução:** {caso['erro']}\n\n")
        for chave, rotulo in [("resultado", "Resultado da avaliação"), ("observado", "Resultado observado"),
                              ("analise", "Análise crítica da condução socrática"), ("ajuste", "Decisão de ajuste")]:
            partes.append(f"**{rotulo}:** {caso.get(chave) or 'Pendente de revisão.'}\n\n")
    texto = DOCUMENTO.read_text(encoding="utf-8")
    base = texto.split(MARCADOR, 1)[0]
    concluidos = sum(c["estado"] == "concluido" for c in registro["casos"])
    revisados = sum(bool(c.get("data_revisao")) for c in registro["casos"])
    situacao = (f"**Situação:** a execução mais recente registra {len(registro['casos'])} dos 18 casos da bateria; "
                f"{concluidos} concluídos e {revisados} revisados. A seção 5 mostra essa execução. "
                "Execuções anteriores permanecem em `tests/resultados_parte_b/`. A conclusão da Parte B exige os 18 casos executados e avaliados.")
    base = re.sub(r"^\*\*Situação:\*\*.*$", lambda _: situacao, base, count=1, flags=re.MULTILINE)
    DOCUMENTO.write_text(base + MARCADOR + "\n" + "".join(partes), encoding="utf-8")

def revisar():
    arquivos = sorted(RESULTADOS.glob("*/registro.json"))
    if not arquivos:
        raise SystemExit("Não há execução registrada. Execute o script sem --revisar primeiro.")
    caminho = arquivos[-1]
    registro = json.loads(caminho.read_text(encoding="utf-8"))
    for caso in registro["casos"]:
        print(f"\n{caso['id']} — {caso['titulo']}\nEsperado: {caso['esperado']}")
        for m in caso["historico"]:
            print(f"\n{m['papel']}: {m['conteudo']}")
        if caso["estado"] != "concluido":
            caso["resultado"] = "Inconclusivo: execução não concluída."
            caso["ajuste"] = "Resolver o erro de execução e repetir o caso antes de avaliar a pedagogia."
        else:
            opcoes = {"a": "Atendeu", "p": "Atendeu parcialmente", "f": "Falhou", "i": "Inconclusivo"}
            escolha = input("\nResultado [a=atendeu, p=parcialmente, f=falhou, i=inconclusivo]: ").strip().lower()
            while escolha not in opcoes:
                escolha = input("Informe a, p, f ou i: ").strip().lower()
            caso["resultado"] = opcoes[escolha]
            for chave, pergunta in [("observado", "O que ocorreu? Cite a resposta ou o turno: "),
                                    ("analise", "Como a resposta atendeu ou não à condução socrática? "),
                                    ("ajuste", "Qual ajuste será feito, ou por que manter o prompt? ")]:
                valor = input(pergunta).strip()
                while not valor:
                    valor = input("Preencha o registro: ").strip()
                caso[chave] = valor
        caso["data_revisao"] = agora()
        salvar(registro, caminho)
    print(f"\nRevisão salva em {DOCUMENTO}")

def executar(config, casos):
    from dotenv import load_dotenv
    from openai import OpenAI
    load_dotenv(RAIZ / ".env")
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("Configure OPENAI_API_KEY no .env local. Nenhuma chamada foi realizada.")
    prompt_arquivo = RAIZ / config["prompt"]
    if not prompt_arquivo.is_file():
        raise SystemExit(f"Prompt não encontrado: {prompt_arquivo}. Copie este pacote para o repositório.")
    prompt_bytes = prompt_arquivo.read_bytes()
    prompt = prompt_bytes.decode("utf-8")
    cliente = OpenAI(timeout=60.0, max_retries=0)
    pasta = RESULTADOS / datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    pasta.mkdir(parents=True)
    caminho = pasta / "registro.json"
    registro = {"inicio": agora(), "prompt_arquivo": config["prompt"],
                "prompt_sha256": hashlib.sha256(prompt_bytes).hexdigest(), "prompt_texto": prompt,
                "modelo": config["modelo"], "temperature": config["temperature"],
                "openai_versao": version("openai"), "casos": []}
    salvar(registro, caminho)
    try:
        for definicao in casos:
            caso = {**definicao, "inicio": agora(), "estado": "em andamento", "historico": []}
            registro["casos"].append(caso)
            mensagens = [{"role": "system", "content": prompt}]
            print(f"\nExecutando {caso['id']} — {caso['titulo']}", flush=True)
            for turno in caso["turnos"]:
                mensagens.append({"role": "user", "content": turno})
                caso["historico"].append({"papel": "Aluno", "data": agora(), "conteudo": turno})
                salvar(registro, caminho)
                try:
                    resposta = cliente.chat.completions.create(model=config["modelo"], messages=mensagens,
                                                               temperature=config["temperature"])
                    escolha = resposta.choices[0]
                    texto = escolha.message.content or ""
                    caso["historico"].append({"papel": "Maieut-IA", "data": agora(), "conteudo": texto,
                                              "modelo": resposta.model, "id_resposta": resposta.id,
                                              "finish_reason": escolha.finish_reason,
                                              "uso": resposta.usage.model_dump() if resposta.usage else None})
                    mensagens.append({"role": "assistant", "content": texto})
                    print(f"Maieut-IA: {texto}", flush=True)
                    if escolha.finish_reason != "stop" or not texto.strip():
                        caso["estado"] = "resposta incompleta"
                        caso["erro"] = "A resposta veio vazia ou não terminou normalmente. Repetir antes de avaliar."
                        break
                except Exception as erro:
                    caso["estado"] = "erro"
                    caso["erro"] = f"{type(erro).__name__}; status HTTP: {getattr(erro, 'status_code', 'não disponível')}."
                    print(f"Falha em {caso['id']}: {caso['erro']}", flush=True)
                    break
                finally:
                    salvar(registro, caminho)
            if caso["estado"] == "em andamento":
                caso["estado"] = "concluido"
            salvar(registro, caminho)
            if caso["estado"] == "erro":
                print("Execução interrompida. Corrija o acesso à API antes de executar novamente.")
                break
    finally:
        registro["fim"] = agora()
        salvar(registro, caminho)
    print(f"\nRegistros: {caminho}\nDocumento: {DOCUMENTO}\nUse --revisar para registrar a avaliação humana.")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    grupo = parser.add_mutually_exclusive_group()
    grupo.add_argument("--validar", action="store_true", help="Confere a estrutura sem chamar a API.")
    grupo.add_argument("--revisar", action="store_true", help="Avalia a execução mais recente sem chamar a API.")
    grupo.add_argument("--caso", help="Executa somente um identificador, como ADV-03.")
    args = parser.parse_args()
    config = json.loads(CASOS.read_text(encoding="utf-8"))
    casos = config["casos"]
    ids = [c["id"] for c in casos]
    if len(ids) != len(set(ids)) or len(casos) != 18:
        raise SystemExit("A bateria deve conter 18 identificadores únicos.")
    if any(not c["turnos"] or not c["esperado"] or any(not t.strip() for t in c["turnos"]) for c in casos):
        raise SystemExit("Há caso sem entrada ou comportamento esperado.")
    if MARCADOR not in DOCUMENTO.read_text(encoding="utf-8"):
        raise SystemExit("O documento não contém o marcador de resultados.")
    if args.validar:
        print(f"Estrutura válida: {len(casos)} casos e {sum(len(c['turnos']) for c in casos)} chamadas planejadas.")
        return
    if args.revisar:
        revisar()
        return
    if args.caso:
        casos = [c for c in casos if c["id"] == args.caso]
        if not casos:
            raise SystemExit("Identificador de caso não encontrado.")
    executar(config, casos)

if __name__ == "__main__":
    main()
