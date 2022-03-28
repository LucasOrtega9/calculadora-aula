
while True:
    num1 = input("qual o primeiro número? ")
    num2 = input("qual o segundo número? ")
    operacao = input("qual a operacao? (Opções: +, -, *). ")
    sair = input("quer sair? digite sim para sair ")
    
    if sair == 'sim':
        break
    if operacao == '+':
        print(int(num1) + int(num2))
    elif operacao == '-':
        print(int(num1) - int(num2))
    elif operacao == '*':
        print(int(num1) * int(num2)) 

    elif operacao == '/':
        print(int(num1) / int(num2))     

print('fora do loop')


