import random

entrada = input ("DIGITE AS PALAVRAS SEPARADAS POR ESPAÇO:").split()

if entrada:

    palavara_aleatoria = random.choice(entrada)

    print("A PALAVRA ALEATORIA É",palavara_aleatoria)
    
else:
    print("NENHUMA PALAVRA FOI DIGITADA")