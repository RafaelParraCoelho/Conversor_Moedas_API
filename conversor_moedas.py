import requests
import pandas as pd

# Lista para armazenar o histórico das conversões
historico = []

def obter_taxa_moeda(origem, destino, valor):
    # Monta a URL para a API Frankfurter com parâmetros de origem, destino e valor
    url = f"https://api.frankfurter.app/latest?amount={valor}&from={origem}&to={destino}"

    # Faz a requisição GET para a API
    resposta = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if resposta.status_code != 200:
        print("Erro de acesso à API. Verifique a conexão.")
        return None
    
    # Converte a resposta JSON em um dicionário Python
    dados = resposta.json()

    # Extrai o valor convertido da moeda de destino
    resultado = dados['rates'][destino]
    
    # Calcula a taxa de câmbio com base no valor convertido e no valor inicial
    taxa = resultado / valor

    # Mostra a taxa de câmbio e o resultado da conversão para o usuário
    print(f"\nTaxa de câmbio: 1 {origem} = {taxa:.4f} {destino}")
    print(f"{valor} {origem} = {resultado:.2f} {destino}")

    # Adiciona essa conversão ao histórico
    historico.append({
        'origem': origem,
        'destino': destino,
        'valor': valor,
        'resultado': resultado,
        'taxa': taxa
    })

if __name__ == "__main__":
    print("Conversor de Moedas")

    while True:
        # Solicita a moeda de origem (ex: USD, EUR, BRL)
        moeda_origem = input("Digite a moeda de origem (ex: USD, EUR, BRL): ").upper()
        # Solicita a moeda de destino
        moeda_destino = input("Digite a moeda de destino (ex: USD, EUR, BRL): ").upper()

        try:
            # Solicita o valor para conversão e converte para float
            valor = float(input(f"Digite o valor em {moeda_origem}: "))
            obter_taxa_moeda(moeda_origem, moeda_destino, valor)

        except ValueError:
            print("Valor inválido. Por favor, insira um número válido.")
        
        # Pergunta se o usuário deseja fazer outra conversão
        continuar = input("Deseja converter outra moeda? (s/n): ").lower()
        if continuar != 's':
            break
    
    # Cria um DataFrame pandas com o histórico das conversões feitas
    df = pd.DataFrame(historico)
    
    if not df.empty:
        print("\nHistórico de Conversões:")
        print(df)
    else:
        print("Nenhuma conversão foi realizada.")

    # Salva o histórico em um arquivo CSV para consulta futura
    df.to_csv("historico_conversoes.csv", index=False)
    
    print("\nConversões salvas no arquivo 'historico_conversoes.csv'. Até logo!")
