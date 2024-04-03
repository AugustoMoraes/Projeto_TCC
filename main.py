from code.llm import Llm

class Main:
    pass

pergunta = Llm('O que é LGPD?')

#pergunta = llm.pergunta_llm('O que é LGPD?')
resposta = pergunta.pergunta_llm()
print(resposta)
