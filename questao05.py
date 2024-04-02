def string_reverse(string):
    inverted_string = ""
    for i in range(len(string) -1, -1 , -1):
        inverted_string += string[i]
    return inverted_string

inputText = input("Digite uma frase: ")
resultReverse = string_reverse(inputText)

print("String invertida: ", resultReverse)