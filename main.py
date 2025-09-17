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

# Bom - Good
# Ok - Standard
# Ruim - Poor

import pandas
from sklearn.preprocessing import LabelEncoder

def processa(arquivo):

    tabela = pandas.read_csv("clientes.csv")

    # Verificando as colunas do arquivo
    print(tabela.info())

    #LabelEncoder
    codificador = LabelEncoder()


    # profissao

    # cientista - 1
    # mecanico - 2
    # ator - 3
    # pintor - 4
    # motorista - 5
    # engenheiro - 6
    # pedreiro - 7




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    processa("clientes.csv")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
