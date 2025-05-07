# Este programa recebe 3 números inteiros e mostra :
# O maior número, O menor Numero e a media dos dois numero.

# Solicitar ao usuario os tres números a serem digitados.
num1 = int(input("DIGITE O PRIMEIRO NÚMERO: "))
num2 = int(input("DIGITE O SEGUNDO NÚMERO: "))
num3 = int(input("DIGITE O TERCEIRO NÚMERO: "))

#Verificar qual é o maior número entres os tres.
if (num1 > num2) and (num1 > num3):
    maior = num1

elif (num2 > num1) and (num2 > num3):
    maior = num2

else: 
    maior = num3

#Verificar qual é o menor número entre os tres.

if (num1 < num2) and (num1 < num3):
    menor = num1

elif (num2 < num1) and (num2 < num3):
    menor = num2

else: menor= num3

    #Calcula a media dos tres numeros.
media =(num1 + num2 + num3 ) / 3

    #Resulato

print("---------------RESULTADO------------------------")

print("O MAIOR NUMERO É", maior)
print("O MENOR NUMERO É ",menor)
print ("A MÉDIA DOS TRES VALORE", media)

print("-------------------------------------------------")
print("-----PROGRAMA FOI FINALIZADO COM SUCESSO!!!----")

    
