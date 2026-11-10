print('Cálculo da média de notas.: ')

notas = []
#Cria uma lista vazia e guarda na variável notas.

while len(notas) < 3:
    #Essa linha cria um laço que repete enquanto a lista notas tiver menos de 3 itens.

    try:
        #Abre um bloco de código que pode gerar erro. O Python executa o que está dentro dele normalmente. Se ocorrer um erro, ele para na hora e pula para o except.

        nota = float(input(f"Digite a nota {len(notas) + 1}: "))
        #Lê o que o usuário digita e converte em número:
        
        
        if 0 <= nota <= 10:
            #Verifica se a nota está entre 0 e 10
            notas.append(nota)
        else:
            #Executa quando a nota é um número, mas está fora do intervalo (por exemplo, 15 ou -2).
            print("Valor inválido! Por favor, insira um número inferior a 10.")


    except ValueError:
        #Se o usuário digitar algo que não seja número (como abc), o float() gera um ValueError e o programa vai direto para o except.
        print("Valor inválido! Por favor, insira um valor numérico.")

media = round(sum(notas)/len(notas), 2)
    #Calcula a média das notas e arredonda o resultado.
    #Round(..., 2) = arredonda para 2 casas decimais
    #Sum = Soma todos os valores da lista.
    #Len = Conta quantos itens a lista.

for i, nota in enumerate(notas, start=1):
    #Percorre a lista pegando a posição e o valor de cada nota ao mesmo tempo:
    #enumerate(notas) entrega pares: (posição, valor).
    #start=1 faz a contagem começar em 1. Sem ele, começaria em 0.
    #i recebe a posição (1, 2, 3) e nota recebe o valor.

    print(f'Nota-{i}: {nota}')

print("Média das notas informadas::", media)