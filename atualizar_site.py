import sys

def atualizar_mensagem(versiculo, referencia, reflexao):
    file_path = 'index.html'
    
    with open(file_path, 'r', encoding='utf-8') as file:
        conteudo = file.read()

    # Localiza o bloco da mensagem do padre no script
    # Buscamos pelo padrão exato que deixamos no código
    import re
    
    novo_bloco = f"""const mensagemDoPadre = {{
            versiculo: '"{versiculo}"',
            referencia: "{referencia}",
            reflexao: "{reflexao}"
        }};"""

    # Expressão regular para encontrar o objeto mensagemDoPadre e substituir
    padrao = r"const mensagemDoPadre = \{.*?\};"
    novo_conteudo = re.sub(padrao, novo_bloco, conteudo, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(novo_conteudo)
    
    print("\n[SUCESSO] O site da paróquia foi atualizado!")

if __name__ == "__main__":
    if len(sys.argv) > 3:
        atualizar_mensagem(sys.argv[1], sys.argv[2], sys.argv[3])