lista_numero = [12,31,54,68,0,-4684,1,58]

def ordenar_lista_numeros(numeros: list) -> list:
    nova_lista_numeros = numeros.copy()

    for i in range(len(nova_lista_numeros)):
        for j in range(i+1, len(nova_lista_numeros)):
            if nova_lista_numeros[i] > nova_lista_numeros[j]:
               nova_lista_numeros[i], nova_lista_numeros[j] =nova_lista_numeros[j], nova_lista_numeros[i]
    print(nova_lista_numeros)

lista_nova = ordenar_lista_numeros(lista_numero)

print(lista_nova)
