#from llm import Llm
from similaridade import resposta_similar
#
# class Main:
#     pass
#
#     llm = Llm()
#     resposta = llm.pergunta_llm('O que é a LGPD')
#     print(resposta)

#conteudo = "quais os problemas com o não cumprimento da LGPD?" #PERGUNTA QUE NÃO TEM NA BASE DE DADOS - SEMELHANTE
#conteudo = 'O que é a LGPD?' #PERGUNTA QUE NÃO TEM NA BASE DE DADOS - IDENTICA
#conteudo = 'Qual a Diferença entre controlador e operador de dados na LGPD?' # PERGUNTA QUE NÃO TEM NA BASE DE DADOS
#conteudo = 'Como utilizar algoritmos de IA?' # PERGUNTA NADA HAVER
#conteudo = 'Cite três tipos de Banco de Dados.' # PERGUNTA NADA HAVER

pergunta = 'O que é banco de dados?'
maior_similaridade, position, dados = resposta_similar(pergunta)

if(maior_similaridade >= 0.75):
    print(f'Maior Similaridade: {maior_similaridade}')
    print(f'Posição: {position}')
    print(f'Dados: {dados[position]}')
else:
    print('Vai pesquisar na llm do Sabiá 2')

