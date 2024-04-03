from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow import keras
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('../dataset/dataset.csv')

perguntas = df['Pergunta']

tokenizer = Tokenizer(num_words=10000)  # Limita o vocabulário a 10.000 palavras
tokenizer.fit_on_texts(perguntas)
sequences = tokenizer.texts_to_sequences(perguntas)

X = pad_sequences(sequences)  # Assume um comprimento máximo de 10 para as perguntas
y = df['LGPD']

# Suponha que `X` são suas sequências tokenizadas e `y` são os rótulos (0 ou 1)
X_padded = pad_sequences(X, maxlen=100)  # Garantir que todas as sequências tenham o mesmo tamanho

# Construir o modelo
model = Sequential()
model.add(Embedding(input_dim=10000, output_dim=128))  # Ajuste conforme necessário
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
#model.add(Dense(64, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(32, activation='relu'))
model.add(Dense(64, activation='sigmoid'))
model.add(Dense(1, activation='sigmoid', use_bias= True))

# Compilar o modelo
model.compile(loss='binary_crossentropy', optimizer='Adam', metrics=['accuracy'])

# Treinar o modelo
historico = model.fit(X_padded, y, batch_size=32, epochs=100, validation_split=0.2)

# GRAFICO
# fig, ax = plt.subplots(1,2, figsize=(14,5))
# ax[0].plot(historico.history['loss'], color='#111487', linewidth=3, label="Perda de treinamento")
# ax[0].plot(historico.history['val_loss'], color='#EFA316', linewidth=3, label="Perda da validação",axes =ax[0])
# legend = ax[0].legend(loc='best', shadow=True)
#
# ax[1].plot(historico.history['accuracy'], color='#111487', linewidth=3, label="Acurácia de treinamento")
# ax[1].plot(historico.history['val_accuracy'], color='#EFA316', linewidth=3, label="Acurácia de validação")
# legend = ax[1].legend(loc='best', shadow=True)
#
# plt.suptitle('Desempenho do treinamento', fontsize = 18)
# plt.show()

#pergunta = 'O que é banco de dados?'
pergunta = 'O que significa LGPD?'
#pergunta = 'Qual orgão é responsável por fiscalizar a LGPD?'
#pergunta = 'como criar um modelo de Redes Neurais para classificação'

# new_tokenizer = Tokenizer()
# nova_pergunta = new_tokenizer.texts_to_sequences([pergunta]) # CONVERTE TEXTOS EM NÚMEROS INTEIROS
# nova_pergunta = pad_sequences(nova_pergunta, maxlen=100) # GARANTE QUE TODAS AS SEQUÊNCIAS DE TEXTOS TENHAM O MESMO COMPRIMENTO PARA PODER ALIMENTAR O MODELO

nova_pergunta = tokenizer.texts_to_sequences([pergunta]) # CONVERTE TEXTOS EM NÚMEROS INTEIROS
nova_pergunta = pad_sequences(nova_pergunta, maxlen=100) # GARANTE QUE TODAS AS SEQUÊNCIAS DE TEXTOS TENHAM O MESMO COMPRIMENTO PARA PODER ALIMENTAR O MODELO NEURAL
previsao = model.predict(nova_pergunta)


previsao = (previsao > 0.5).astype('int32') # retorna uma matriz

print(previsao[0][0])