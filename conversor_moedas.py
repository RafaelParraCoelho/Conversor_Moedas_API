import requests
import pandas as pd
from datetime import datetime

# Lista para armazenar o histórico das conversões
historico = []

# Função para obter moedas suportadas pela API
def obter_moedas_suportadas():
    url = "https://api.frankfurter.app/currencies"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()  # retorna um dicionário { "USD": "United States Dollar", "BRL": "Brazilian Real", ... }
    else:
        print("Erro ao buscar moedas suportadas.")
        return {}

# Função para mostrar cotações em relação ao BRL
def mostrar_cotacoes_em_brl():
    moedas = ["USD", "EUR", "GBP", "JPY", "CAD", "AUD", "CHF", "CNY", "INR"]
    print("Cotação de moedas em relação ao Real (BRL):\n")
    
    for moeda in moedas:
        url = f"https://api.frankfurter.app/latest?amount=1&from={moeda}&to=BRL"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()
            taxa = dados['rates']['BRL']
            print(f"1 {moeda} = {taxa:.2f} BRL")
        else:
            print(f"Erro ao acessar a API para {moeda}")

# Função para obter taxa e mostrar conversão
def obter_taxa_moeda(origem, destino, valor):
    url = f"https://api.frankfurter.app/latest?amount={valor}&from={origem}&to={destino}"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        print("Erro ao acessar a API. Verifique os dados e a conexão.")
        return

    dados = resposta.json()
    resultado = dados['rates'][destino]
    taxa = resultado / valor

    print(f"\nTaxa de câmbio: 1 {origem} = {taxa:.2f} {destino}")
    print(f"{valor} {origem} = {resultado:.2f} {destino}")

    # Adiciona ao histórico
    historico.append({
        'data_hora': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'origem': origem,
        'destino': destino,
        'valor': valor,
        'resultado': resultado,
        'taxa': round(taxa, 4)
    })

# Programa principal
if __name__ == "__main__":
    print("=== Conversor de Moedas ===\n")
    mostrar_cotacoes_em_brl()
    
    moedas_suportadas = obter_moedas_suportadas()

    print("\nMoedas suportadas:")
    for codigo, nome in moedas_suportadas.items():
        print(f"{codigo} - {nome}")

    while True:
        moeda_origem = input("\nDigite a moeda de origem (ex: USD, EUR, BRL): ").upper()
        moeda_destino = input("Digite a moeda de destino (ex: USD, EUR, BRL): ").upper()

        try:
            valor = float(input(f"Digite o valor em {moeda_origem}: "))
            obter_taxa_moeda(moeda_origem, moeda_destino, valor)
        except ValueError:
            print("Valor inválido. Digite um número válido.")
            continue

        continuar = input("Deseja converter outra moeda? (s/n): ").lower()
        if continuar != 's':
            break

    # Exibe e salva o histórico
    df = pd.DataFrame(historico)
    if not df.empty:
        print("\nHistórico de Conversões:")
        print(df)
        df.to_csv("historico_conversoes.csv", index=False)
        print("\nConversões salvas no arquivo 'historico_conversoes.csv'. Até logo!")
    else:
        print("Nenhuma conversão foi realizada.")
