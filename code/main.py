import time

#conteudo = "quais os problemas com o não cumprimento da LGPD?" #PERGUNTA QUE NÃO TEM NA BASE DE DADOS - SEMELHANTE
#conteudo = 'O que é a LGPD?' #PERGUNTA QUE NÃO TEM NA BASE DE DADOS - IDENTICA
#conteudo = 'Qual a Diferença entre controlador e operador de dados na LGPD?' # PERGUNTA QUE NÃO TEM NA BASE DE DADOS
#conteudo = 'Como utilizar algoritmos de IA?' # PERGUNTA NADA HAVER
#conteudo = 'Cite três tipos de Banco de Dados.' # PERGUNTA NADA HAVER

'''
1. Quais são os direitos dos titulares de dados pessoais conforme a LGPD?
2. Como a LGPD se aplica a empresas estrangeiras que operam no Brasil?
3. O que são cookies e como a LGPD regulamenta o seu uso?
4. Como a LGPD afeta a coleta de dados biométricos?
5. Quais são as obrigações das empresas em relação à segurança da informação sob a LGPD?
6. Como a LGPD trata dados anonimizados que podem ser reidentificados?
7. O que são incidentes de segurança de dados e como devem ser gerenciados segundo a LGPD?
8. Como a LGPD influencia as políticas de privacidade e termos de uso das empresas?
9. Quais são os desafios de implementação da LGPD para pequenas e médias empresas?
10. Como a LGPD interage com outras legislações internacionais de proteção de dados, como o GDPR?
'''
import pandas as pd
from similaridade import resposta_similar
from redeNeural import classifica_contexto
from llm import pergunta_llm, update_dataset, add_time_llm

df = pd.read_csv('../dataset/dataset.csv')
df_time = pd.read_csv('../dataset/tempo_de_resposta.csv')
pergunta = 'Como a LGPD interage com outras legislações internacionais de proteção de dados, como o GDPR?' #input("Faça sua pergunta: ")
#classificado = classifica_contexto(df, pergunta)
#maior_similaridade, position, dados = resposta_similar(df, pergunta)

if(True):
    if(False):
        print('teste')
        #print(f'Maior Similaridade: {maior_similaridade}')
        # print(f'Posição: {position}')
        # print(f'Dados: {dados[position]}')
    else:
        inicio = time.time()
        resposta = pergunta_llm(pergunta)
        fim = time.time()
        print(resposta)
        tempo = fim - inicio
        print(f'Tempo de resposta do Sabiá2: {tempo}')
        #update_dataset(df, pergunta, resposta, 1)
        add_time_llm(df_time, pergunta, tempo, 'sabia2')
else:
    print('Pergunta inválida!\nRealizar pergunta que esteja no contexto da LGPD')