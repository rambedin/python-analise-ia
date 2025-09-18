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

    '''
        1 - Normalizando as colunas texto com LabelEncoder

        cientista - 1
        mecanico - 2
        ator - 3
        pintor - 4
        motorista - 5
        engenheiro - 6
        pedreiro - 7    
                    
    '''
    codificador1 = LabelEncoder()
    tabela["profissao"] = codificador1.fit_transform(tabela["profissao"])

    # para texto (object)
    #tabela["profissao"] = codificador1.inverse_transform(tabela["profissao"])

    # mix_credito
    codificador2 = LabelEncoder()
    tabela["mix_credito"] = codificador2.fit_transform(tabela["mix_credito"])

    # comportamento_pagamento
    codificador3 = LabelEncoder()
    tabela["comportamento_pagamento"] = codificador3.fit_transform(tabela["comportamento_pagamento"])

    '''
        2 - Separação de dados X e Y
        
        X = Outras colunas (colunas usadas para previsão)
        Y = Quem devo prever (coluna score_credito)
    '''

    y = tabela["score_credito"]
    x = tabela.drop(columns=["score_credito", "id_cliente"]) # exclui colunas que nao devo usar.

    '''
        3 - Treinamento para IA
        
        separação do X/Y para treinamento e teste da IA.
        30% de teste e 70% de treinamento.
    '''
    from sklearn.model_selection import train_test_split

    x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3) #30% para teste

    '''
        4 - Criação do modelo de IA
        
        Modelos usados:
            Arvore de decisão -> RandomForest
            Vizinhos Proximos -> KNN 
        
        - importar modelo
        - criar modelo
        - treinar modelo

    '''

    # importar modelo de IA
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.neighbors import KNeighborsClassifier

    # criar modelo de IA
    modelo_arvoredecisao = RandomForestClassifier()
    modelo_knn = KNeighborsClassifier()

    #treinar o modelo
    modelo_arvoredecisao.fit(x_treino, y_treino)
    modelo_knn.fit(x_treino, y_treino)

    '''
        Escolher e executar o modelo com melhor acuracia (resultado)
    '''
    previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)
    previsao_knn = modelo_knn.predict(x_teste)

    from sklearn.metrics import accuracy_score

    accuracy_arvoredecisao = accuracy_score(y_teste, previsao_arvoredecisao)
    accuracy_knn = accuracy_score(y_teste, previsao_knn)

    print(accuracy_arvoredecisao)
    print(accuracy_knn)

    '''
        Exemplo de novas previsões, com novos registros
    '''
    tabela_nova = pandas.read_csv("novos_clientes.csv")

    # normaliza novamente profissao para IA
    tabela_nova["profissao"] = codificador1.fit_transform(tabela_nova["profissao"])

    # normaliza novamente mix_credito para IA
    tabela_nova["mix_credito"] = codificador2.fit_transform(tabela_nova["mix_credito"])

    # normaliza novamente comportamento_pagamento para IA
    tabela_nova["comportamento_pagamento"] = codificador3.fit_transform(tabela_nova["comportamento_pagamento"])

    # realiza a previsão para os novos dados.
    if (accuracy_arvoredecisao > accuracy_knn):
        print('utilizando arvore de decisão para previsão de dados.')
        previsao = modelo_arvoredecisao.predict(tabela_nova)
    else:
        print('utilizando knn de decisão para previsão de dados.')
        previsao = modelo_knn.predict(tabela_nova)

    print(previsao)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    processa("clientes.csv")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
