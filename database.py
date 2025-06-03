import json

def ler_dados(nome_arquivo):
    try:
        with open(f"{nome_arquivo}.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return[]

def escrever_dados(lista, nome_arquivo):
    with open(f"{nome_arquivo}.json", "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)