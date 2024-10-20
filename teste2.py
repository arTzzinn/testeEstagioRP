def contar_a(string):

    count = string.lower().count('a')
    
    if count > 0:
        return f"A letra 'a' aparece {count} vez(es) na string."
    else:
        return "A letra 'a' não foi encontrada na string."

entrada = input("Digite uma string: ")
resultado = contar_a(entrada)
print(resultado)
