import time

# --- Apresentação ---
print("-"*30)
print("Bem vindo ao Quiz")
print("-"*30)
print("Temos dois Temas: \n1- Geografia \n2- História")

tema = int(input("Escolha um tema: "))

# --- Organização do Quiz ---
print("Carregando...")
time.sleep(1)
print("-"*30)
acertos = 0
while tema not in [1, 2]:
    print("Por favor, escolha um tema VÁLIDO!")
    tema = int(input("Escolha um tema: "))

# --- Pergunta e Resposta ---
if tema == 1:
    print("Você escolheu \033[33mGeografia!\033[m")
    print("-"*30)
    print("1º Pergunta: Qual é a capital do Brasil?")
    resposta = input("Resposta: ").capitalize()
    if resposta == "Brasília" or resposta =="Brasilia":
        print("\033[32mResposta correta!\033[m")
        acertos += 1
    else:
        print("\033[31mResposta errada!\033[m A resposta correta é Brasília.")
    
    print("-"*30)
    print("2º Pergunta: Qual é o maior país do mundo?")
    resposta = input("Resposta: ").capitalize()
    if resposta == "Rússia" or resposta == "Russia":
        print("\033[32mResposta correta!\033[m")
        acertos += 1
    else:
        print("\033[31mResposta errada!\033[m A resposta correta é Rússia.")

    print("-"*30)
    print("3º Pergunta: Qual continente o Egito fica?")
    resposta = input("Resposta: ").capitalize()
    if resposta == "África" or resposta == "Africa":
        print("\033[32mResposta correta!\033[m")
        acertos += 1
    else:
        print("\033[31mResposta errada!\033[m A resposta correta é África.")

elif tema == 2:
    print("Você escolheu \033[36mHistória!\033[m")
    print("-"*30)
    print("1º Pergunta: Quando acabou a Segunda Guerra Mundial?")
    resposta = input("Resposta: ")
    if resposta == "1945":
        print("\033[32mResposta correta!\033[m")
        acertos += 1
    else:
        print("\033[31mResposta errada!\033[m A resposta correta é 1945.")
    
    print("-"*30)
    print("2º Pergunta: Qual foi a primiera capital do Brasil?")
    resposta = input("Resposta: ").capitalize()
    if resposta == "Salvador":
        print("\033[32mResposta correta!\033[m")
        acertos += 1
    else:
        print("\033[31mResposta errada!\033[m A resposta correta é Salvador")

    print("-"*30)
    print("3º Pergunta: Aonde aconteceu a Revolução Francesa?")
    resposta = input("Resposta: ").capitalize()
    if resposta == "França":
        print("\033[32mResposta correta!\033[m")
        acertos += 1
    else:
        print("\033[31mResposta errada!\033[m A resposta correta é França.")

print("-"*30)
if acertos > 1:
    print("Você acertou {}! \033[32mParabéns!\033[m".format(acertos))
else:
    print("Que pena você acertou apenas {}! \033[31m TENTE NOVAMENTE!\033[m".format(acertos))
