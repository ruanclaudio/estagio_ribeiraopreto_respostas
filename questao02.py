def verify_fibonacci(number):
            fibonnaciList = [0, 1]
            
            while fibonnaciList[-1] < number:
                nextNum = fibonnaciList[-1] + fibonnaciList[-2]
                fibonnaciList.append(nextNum)
            if number in fibonnaciList:
                return f"O número {number} pertence a sequência de Fibonacci."
            else:
                return f"O número {number} não pertence a sequência de Fibonacci."
            
while True:
    try:    
        number = int(input("Informe o número que deseja saber se existe na sequência de Fibonacci: "))
        result = verify_fibonacci(number)
        print(result)
        
        answer = input("Deseja sair do sistema? Digite S ou N: ")
        if answer.upper() == "S":
            break   
        elif answer.upper() != "N":
            print("Resposta inválida. Digite somente S ou N.")
            
    except ValueError:
        print("Valor inválido, insira apenas números inteiros.")
