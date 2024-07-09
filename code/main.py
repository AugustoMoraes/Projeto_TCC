
#conteudo = "quais os problemas com o não cumprimento da LGPD?" #PERGUNTA QUE NÃO TEM NA BASE DE DADOS - SEMELHANTE
#conteudo = 'O que é a LGPD?' #PERGUNTA QUE NÃO TEM NA BASE DE DADOS - IDENTICA
#conteudo = 'Qual a Diferença entre controlador e operador de dados na LGPD?' # PERGUNTA QUE NÃO TEM NA BASE DE DADOS
#conteudo = 'Como utilizar algoritmos de IA?' # PERGUNTA NADA HAVER
#conteudo = 'Cite três tipos de Banco de Dados.' # PERGUNTA NADA HAVER

import pandas as pd
from similaridade import resposta_similar
from redeNeural import classifica_contexto
from llm import pergunta_llm, update_dataset

df = pd.read_csv('../dataset/dataset.csv')
pergunta = 'o que são teste de softwares?'#input("Faça sua pergunta: ")
classificado = classifica_contexto(df, pergunta)
maior_similaridade, position, dados = resposta_similar(df, pergunta)

if(classificado):
    if(maior_similaridade >= 0.75):
        print(f'Maior Similaridade: {maior_similaridade}')
        print(f'Posição: {position}')
        print(f'Dados: {dados[position]}')
    else:
        resposta = pergunta_llm(pergunta)
        print(resposta)
        update_dataset(df, pergunta, resposta, 1)

else:
    print('Pergunta inválida!\nRealizar pergunta que esteja no contexto da LGPD')