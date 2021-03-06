import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

data = pd.read_csv("https://raw.githubusercontent.com/Davi-ldc/machine-learnig/master/data/census.csv")

variaveis_previsoras = data.iloc[:, 0:14].values
classes = data.iloc[:, 14].values


onehotencoder = OneHotEncoder()
variaveis_previsoras = onehotencoder.fit_transform(variaveis_previsoras)

print(variaveis_previsoras.shape)
print(variaveis_previsoras)
label = LabelEncoder()
classes = label.fit_transform(classes)


variaveis_previsoras_treinamento, variaveis_previsoras_teste, classes_treinamento, classes_teste = train_test_split(variaveis_previsoras, classes, test_size=0.3, random_state=0)


import keras.callbacks
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.callbacks import TensorBoard

rede_neural = Sequential()

print(variaveis_previsoras_treinamento.shape)

rede_neural.add(Dense(units=200, activation='relu', input_dim=22144))
rede_neural.add(Dropout(0.2))
rede_neural.add(Dense(units=200, activation='relu'))
rede_neural.add(Dropout(0.2))
rede_neural.add(Dense(units=200, activation='relu'))
rede_neural.add(Dropout(0.2))
rede_neural.add(Dense(units=200, activation='relu'))
rede_neural.add(Dropout(0.2))
rede_neural.add(Dense(units=200, activation='relu'))
rede_neural.add(Dropout(0.2))

rede_neural.add(Dense(units=1, activation='sigmoid'))

rede_neural.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
#tensorboard
tensorboard = TensorBoard(log_dir='logs/graficos', write_images=True)



rede_neural.fit(variaveis_previsoras_treinamento, classes_treinamento, epochs=100, batch_size=490, callbacks=[tensorboard])

erro, acuracia = rede_neural.evaluate(variaveis_previsoras_teste, classes_teste)
print(erro, acuracia)#83%

