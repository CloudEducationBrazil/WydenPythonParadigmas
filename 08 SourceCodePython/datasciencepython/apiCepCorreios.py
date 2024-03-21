# pip install requests
import requests

def obter_cep_info(cep):
    url = f"https://viacep.com.br/ws/{cep}/json"
    resposta = requests.get(url)
    dados = resposta.json()
    return dados

def main():
    cep = input("Digite o CEP para consultar: ")
    try:
        info_cep = obter_cep_info(cep)
        print("Informações do CEP:")
        for chave, valor in info_cep.items():
            print(f"{chave}: {valor}")
    except Exception as e:
        print("Ocorreu um erro ao obter informações do CEP:", e)

if __name__ == "__main__":
    main()