def quantidadeValor(string):
    valor = 0;
    for num in string:
        valor += 1
    return valor

string = input()

print (quantidadeValor(string))