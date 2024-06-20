import pandas as pd
import maritalk
minha_chave = "100088405894968274443$48d83f597eed3dac55ca7ab70e8d6d46628784d793046bf36006985b4d18354e"
def pergunta_llm(pergunta):
    model = maritalk.MariTalk(
        key= minha_chave,
        model="sabia-2-medium"
    )

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
def update_dataset(df: pd.DataFrame, pergunta, resposta, classe):
    novo_registro = {'Pergunta': pergunta, 'Resposta': resposta, 'LGPD': classe}
    df = df._append(novo_registro, ignore_index = True)
    df.to_csv('../dataset/dataset.csv', index= False)

def add_time_llm(df: pd.DataFrame, pergunta, time, llm):
    novo_registro = {'pergunta': pergunta, 'tempo': time, 'llm': llm}
    df = df._append(novo_registro, ignore_index=True)
    df.to_csv('../dataset/tempo_de_resposta.csv', index=False)