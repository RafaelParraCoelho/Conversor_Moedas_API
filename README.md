# Conversor de Moedas em Python

Este projeto é um **conversor de moedas** simples que utiliza uma API pública para obter taxas de câmbio em tempo real. Ele permite que o usuário converta valores entre diferentes moedas, armazene um histórico das conversões e exporte esse histórico para um arquivo CSV.

## Funcionalidades

- Consulta taxas de câmbio atualizadas via API.
- Conversão de valores entre moedas escolhidas pelo usuário.
- Armazenamento do histórico das conversões feitas durante a execução.
- Exportação do histórico para um arquivo CSV chamado `historico_conversoes.csv`.

## Tecnologias Utilizadas

- Python 3
- Biblioteca `requests` para fazer requisições HTTP.
- Biblioteca `pandas` para manipulação e exportação de dados.
