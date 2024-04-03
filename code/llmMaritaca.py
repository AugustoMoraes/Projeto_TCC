import maritalk

model = maritalk.MariTalk(
    key="100088405894968274443$48d83f597eed3dac55ca7ab70e8d6d46628784d793046bf36006985b4d18354e",
    model="sabia-2-medium"  # No momento, suportamos os modelos sabia-2-medium e sabia-2-small
)


def pergunta_llm(pergunta):
    messages = [
        {"role": "user", "content": f"{pergunta}"},

    ]

    resposta = model.generate(
        messages,
        do_sample=True,
        max_tokens=200,
        temperature=0.7,
        top_p=0.95)["answer"]

    return resposta
    #print(f"Resposta: {resposta}")

#print(pergunta_llm('O que é LGPD?'))