# data = pd.read_csv('../dataset/dataset.csv')
import pandas as pd
import spacy
from sklearn.metrics.pairwise import cosine_similarity


def resposta_similar(pergunta):
        nlp = spacy.load("pt_core_news_sm")

        df = pd.read_csv('../dataset/dataset.csv')
        perguntas_lgpd = df.loc[df['LGPD'] == 1]  # LISTA DE APENAS PERGUNTAS QUE ESTÃO NO CONTEXTO DA LGPD

        conjunto_de_dados = perguntas_lgpd['Pergunta'] # Pega apenas a coluna Perguntas

        data = list(zip(perguntas_lgpd['Pergunta'].tolist(), perguntas_lgpd['Resposta'].tolist())) # CONVERTE O DF PARA LISTA

        vetor_texto = []
        vetor_similaridade = []

        #conteudo = "quais os problemas com o não cumprimento da LGPD?" #PERGUNTA QUE NÃO TEM NA BASE DE DADOS - SEMELHANTE
        #conteudo = 'O que é a LGPD?' #PERGUNTA QUE NÃO TEM NA BASE DE DADOS - IDENTICA
        conteudo = pergunta#'O que é a LGPD?'
        #conteudo = 'Qual a Diferença entre controlador e operador de dados na LGPD?' # PERGUNTA QUE NÃO TEM NA BASE DE DADOS
        #conteudo = 'Como utilizar algoritmos de IA?' # PERGUNTA NADA HAVER
        #conteudo = 'Cite três tipos de Banco de Dados.' # PERGUNTA NADA HAVER
        # resposta = resposta_similar(data)
        # print('---------------PERGUNTA SIMILAR ENCONTRADA---------------------------')
        # print(f'Pergunta: {resposta[0]}')
        # print(f'Resposta: {resposta[1]}')
        conteudo_vetor = nlp(conteudo).vector

        # Convertendo os textos em vetores de incorporação de palavras
        for i in conjunto_de_dados:
                vetor_texto.append(nlp(i).vector)

        #print(vetor_texto)
        for i in vetor_texto:
                #similaridade = cosine_similarity([conteudo_vetor], [i])[0][0]
                vetor_similaridade.append(cosine_similarity([conteudo_vetor], [i])[0][0])
                #print(f'Similaridade {i} - {vetor_similaridade}')
        p = 0
        for i in vetor_similaridade:
                print(f'pergunta {p} - Similaridade: {i}')
                p = p + 1

        def resposta_similar(lista):
                maior = 0
                position = 0
                j = 0
                for i in vetor_texto:
                        similaridade = cosine_similarity([conteudo_vetor], [i])[0][0]
                        if similaridade > maior:
                                maior = similaridade
                                position = j
                        j = j + 1
                        #vetor_similaridade.append(cosine_similarity([conteudo_vetor], [i])[0][0])
                resposta = lista[position]
                return resposta


        resposta = resposta_similar(data)
        return resposta
        print('---------------PERGUNTA SIMILAR ENCONTRADA---------------------------')
        print(f'Pergunta: {resposta[0]}')
        print(f'Resposta: {resposta[1]}')