# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Entender o desafio da empresa
# Importar a base de dados
# Preparar a base de dados para IA
# Criar o modelo de IA para prever a nota de crédito
# Escolher o melhor modelo
# Fazer novas previsões

# Score [BOM, OK, RUIM]

import pandas

def processa(arquivo):

    tabela = pandas.read_csv("clientes.csv")
    print(tabela)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    processa("clientes.csv")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
