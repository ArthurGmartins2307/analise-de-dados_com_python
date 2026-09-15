import pandas as pd


dados = {
    "CLIENTES": [
        "Arthur Galvão", "João Silva", "Maria Santos", "Lucas Oliveira",
        "Ana Costa", "Pedro Souza", "Juliana Alves", "Gabriel Lima",
        "Beatriz Rocha", "Rafael Martins", "Camila Ferreira", "Felipe Gomes",
        "Larissa Mendes", "Bruno Carvalho", "Isabela Ramos", "Gustavo Barbosa",
        "Mariana Dias", "Leonardo Nunes", "Sofia Castro", "Thiago Moreira"
    ],

    "DESTINOS": [
        "Vancouver", "Lisboa", "Nova York", "Tóquio", "Buenos Aires",
        "Londres", "Madrid", "Roma", "Toronto", "Dubai",
        "Orlando", "Amsterdã", "Santiago", "Cancún", "Berlim",
        "Miami", "Barcelona", "Sydney", "Lima", "Paris"
    ],

    "PAÍSES": [
        "Canadá", "Portugal", "Estados Unidos", "Japão", "Argentina",
        "Inglaterra", "Espanha", "Itália", "Canadá", "Emirados Árabes Unidos",
        "Estados Unidos", "Holanda", "Chile", "México", "Alemanha",
        "Estados Unidos", "Espanha", "Austrália", "Peru", "França"
    ],

    "VALORES": [
        8500, 5200, 7800, 9200, 3500,
        6800, 4900, 6100, 7300, 10500,
        5600, 6400, 3200, 4700, 5900,
        7200, 5100, 12500, 3800, 6900
    ],

    "PASSAGEIROS": [
        2, 1, 3, 2, 4,
        2, 1, 3, 2, 4,
        2, 3, 1, 4, 2,
        3, 2, 2, 1, 3
    ]
}

tabela = pd.DataFrame(dados)
print(tabela)