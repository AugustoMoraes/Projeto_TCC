import pandas as pd
import spacy
from sklearn.metrics.pairwise import cosine_similarity
import time

data = pd.read_csv('../dataset/dataset.csv')
def resposta_similar(df, pergunta):
        nlp = spacy.load("pt_core_news_sm")

        perguntas_lgpd = df.loc[df['LGPD'] == 1]  # LISTA DE APENAS PERGUNTAS QUE ESTÃO NO CONTEXTO DA LGPD

        conjunto_de_dados = perguntas_lgpd['Pergunta'] # Pega apenas a coluna Perguntas

        data = list(zip(perguntas_lgpd['Pergunta'].tolist(), perguntas_lgpd['Resposta'].tolist())) # CONVERTE O DF PARA LISTA

        vetor_texto = []
        vetor_similaridade = []

        conteudo = pergunta

        conteudo_vetor = nlp(conteudo).vector

        # Convertendo os textos em vetores de incorporação de palavras
        for i in conjunto_de_dados:
                vetor_texto.append(nlp(i).vector)

        for i in vetor_texto:
                vetor_similaridade.append(cosine_similarity([conteudo_vetor], [i])[0][0])

        def resposta(lista):
                maior = 0
                position = 0
                j = 0
                for i in vetor_texto:
                        similaridade = cosine_similarity([conteudo_vetor], [i])[0][0]
                        if similaridade > maior:
                                maior = similaridade
                                position = j
                        j = j + 1

                return maior, position, lista


        result = resposta(data)

        return result
inicio = time.time()
resposta = resposta_similar(data, 'quais os problemas com o não cumprimento da LGPD?')
fim = time.time()

print(resposta)

print(f'Tempo de execução: {fim-inicio}')