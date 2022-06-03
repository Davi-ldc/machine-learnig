import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer

#carrega os dados
with open('data/emotions_train.txt') as f:
    treinamento = pd.read_csv(f, sep = ';', names=["emotion", "sentence"])

with open('data/emotions_test.txt') as f:
    teste = pd.read_csv(f, sep = ';', names=["emotion", "sentence"])
    
dados = treinamento.append(teste)

cv = CountVectorizer()
vetor = cv.fit(dados['sentence'])

treinamento = cv.transform(treinamento['sentence'])
teste = cv.transform(teste['sentence'])

#divide os dados

dados_previsores_treinamento = treinamento.iloc[:, 0].values
classes_treinamento = treinamento.iloc[:, 1].values

dados_previsores_teste = teste.iloc[:, 0].values
classes_teste = teste.iloc[:, 1].values


def emotions(string,vector,model):
     vectorized = vector.transform([string])
     pred = model.predict(vectorized)
     return pred

#aplica a rede neural
from sklearn.neural_network import MLPClassifier

neural_network = MLPClassifier(verbose=True, max_iter=100, tol=0.001, solver='adam', hidden_layer_sizes=(100, 100, 100), random_state=1)

#treina a rede neural
neural_network.fit(dados_previsores_treinamento, classes_treinamento)



#testa a rede neural
previsoes = neural_network.predict(dados_previsores_teste)

#pontuação
pontuação = accuracy_score(classes_teste, previsoes)
print(pontuação)
