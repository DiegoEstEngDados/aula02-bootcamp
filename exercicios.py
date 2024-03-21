import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# n1 = int(input("digite um número: "))
# n2 = int(input("digite outro número: "))
# soma = n1 + n2
# print(f"soma {soma}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# dividendo = int(input("digite um dividendo: "))
# DIVISOR = 5
# resto = dividendo % DIVISOR
# print(f"O resta da divisão é {resto}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# multiplicador = int(input("Qual é o número multiplicador: "))
# n1 = int(input("digite um número: "))
# resultado = multiplicador * n1
# print(f"o resultado é:  {resultado}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# numero_01 = int(input("Inserir um numero inteiro: "))
# numero_02 = int(input("Inserir outro numero inteiro: "))
# resultado = numero_01 // numero_02
# print(resultado)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# for i in (range(0,4)):
#     n1 = int(input("digite um nímero: "))
#     resultado = n1 ** 2
#     print(resultado)


# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

# n1 = float(input("digite um decimal: "))
# n2 = float(input("digite outro decimal: "))
# soma = n1 + n2
# resultado = (f"resultado {soma}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# n1 = float(input("digite um decimal: "))
# n2 = float(input("digite outro decimal: "))
# media =  (n1 + n2) / 2
# resultado = (f"resultado {media}")


# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# base = float(input("digite a base: "))
# expoente = int(input("digite o expoente: "))
# resultado = base ** expoente
# print(f"o resultado de {base}  elevado a  {expoente}  é de  {resultado}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# def celsius_para_fahrenheit(celsius):
#     return (9/5) * celsius + 32

# # Solicita ao usuário a temperatura em Celsius
# temperatura_celsius = float(input("Digite a temperatura em Celsius: "))
# # Converte a temperatura para Fahrenheit usando a função celsius_para_fahrenheit
# temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
# # Imprime o resultado
# print("A temperatura de", temperatura_celsius, "Celsius equivale a", temperatura_fahrenheit, "Fahrenheit.")


# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# raio_do_circulo = float(input("Digite o raio: "))
# area_do_circulo = math.pi * raio_do_circulo ** 2
# area_do_circulo_formatada = "{:.2f}".format(area_do_circulo)
# print(f"{area_do_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# texto = str(input("digite uma palavra: "))
# texto_upper = texto.upper()
# print(texto_upper)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# texto = str(input("digite uma palavra: "))
# texto_lower = texto.lower()
# print(texto_lower)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# Solicita ao usuário uma frase
# frase_usuario = input("Digite uma frase: ")
# # Remove espaços em branco do início e do final da frase usando o método strip()
# frase_sem_espacos = frase_usuario.strip()
# # Imprime a frase sem espaços em branco no início e no final
# print("Frase sem espaços em branco no início e no final:", frase_sem_espacos)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# Solicita ao usuário uma data no formato "dd/mm/aaaa"
# data = input("Digite uma data no formato 'dd/mm/aaaa': ")
# # Divide a data em dia, mês e ano usando o método split()
# dia, mes, ano = data.split("/")
# # Imprime o dia, mês e ano separadamente
# print("Dia:", dia)
# print("Mês:", mes)
# print("Ano:", ano)

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# Solicita ao usuário duas strings
# string1 = input("Digite a primeira string: ")
# string2 = input("Digite a segunda string: ")
# # Concatena as duas strings usando o operador de concatenação '+'
# string_concatenada = string1 + string2
# # Imprime a string resultante da concatenação
# print("As duas strings concatenadas são:", string_concatenada)


# data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
# lista_de_dia_mes_ano = data_do_usuario.split("/")
# print(f"O elemento 1 e o: {lista_de_dia_mes_ano[0]}")
# print(f"O elemento 2 e o: {lista_de_dia_mes_ano[1]}")
# print(f"O elemento 3 e o: {lista_de_dia_mes_ano[2]}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# # Solicita ao usuário duas expressões booleanas
# expressao1 = input("Digite a primeira expressão booleana (True ou False): ").lower()
# expressao2 = input("Digite a segunda expressão booleana (True ou False): ").lower()
# # Converte as entradas do usuário para booleanos
# expressao1 = expressao1 == "true"
# expressao2 = expressao2 == "true"
# # Avalia a operação AND entre as expressões booleanas
# resultado_and = expressao1 and expressao2
# # Imprime o resultado da operação AND
# print("O resultado da operação AND entre", expressao1, "e", expressao2, "é:", resultado_and)


# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# Solicita ao usuário dois valores booleanos
# valor1 = input("Digite o primeiro valor booleano (True ou False): ").lower()
# valor2 = input("Digite o segundo valor booleano (True ou False): ").lower()
# # Converte as entradas do usuário para booleanos
# valor1 = valor1 == "true"
# valor2 = valor2 == "true"
# # Avalia a operação OR entre os valores booleanos
# resultado_or = valor1 or valor2
# # Imprime o resultado da operação OR
# print("O resultado da operação OR entre", valor1, "e", valor2, "é:", resultado_or)


# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# Solicita ao usuário um valor booleano
# valor_booleano = input("Digite um valor booleano (True ou False): ").lower()
# # Converte a entrada do usuário para um valor booleano
# valor_booleano = valor_booleano == "true"
# # Inverte o valor booleano usando o operador de negação 'not'
# valor_booleano_invertido = not valor_booleano
# # Imprime o valor booleano invertido
# print("O valor booleano invertido é:", valor_booleano_invertido)


# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# Solicita ao usuário dois números
# numero1 = float(input("Digite o primeiro número: "))
# numero2 = float(input("Digite o segundo número: "))

# # Compara se os dois números são iguais
# if numero1 == numero2:
#     print("Os dois números são iguais.")
# else:
#     print("Os dois números são diferentes.")


# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# # Solicita ao usuário dois números
# numero1 = float(input("Digite o primeiro número: "))
# numero2 = float(input("Digite o segundo número: "))
# # Compara se os dois números são diferentes
# if numero1 != numero2:
#     print("Os dois números são diferentes.")
# else:
#     print("Os dois números são iguais.")


# #### try-except e if

# 21: Conversor de Temperatura
# def celsius_para_fahrenheit(celsius):
#     return (9/5) * celsius + 32

# while True:
#     try:
#         # Solicita ao usuário a temperatura em Celsius
#         temperatura_celsius = float(input("Digite a temperatura em Celsius: "))

#         # Converte a temperatura para Fahrenheit usando a função celsius_para_fahrenheit
#         temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)

#         # Imprime o resultado
#         print("A temperatura de", temperatura_celsius, "Celsius equivale a", temperatura_fahrenheit, "Fahrenheit.")
#         break  # Saímos do loop se a entrada for válida
#     except ValueError:
#         print("Por favor, insira um valor numérico válido para a temperatura.")


# 22: Verificador de Palíndromo
# def verifica_palindromo(palavra):
#     # Remove espaços em branco e converte para minúsculas
#     palavra = palavra.replace(" ", "").lower()
#     # Compara a palavra original com sua inversa
#     return palavra == palavra[::-1]

# # Solicita ao usuário uma palavra para verificar se é um palíndromo
# palavra = input("Digite uma palavra para verificar se é um palíndromo: ")

# # Verifica se a palavra é um palíndromo
# if verifica_palindromo(palavra):
#     print("A palavra", palavra, "é um palíndromo.")
# else:
#     print("A palavra", palavra, "não é um palíndromo.")


# # 23: Calculadora Simples
# def adicao(valores):
#     return sum(valores)

# def subtracao(valores):
#     resultado = valores[0]
#     for valor in valores[1:]:
#         resultado -= valor
#     return resultado

# def multiplicacao(valores):
#     resultado = 1
#     for valor in valores:
#         resultado *= valor
#     return resultado

# def divisao(valores):
#     resultado = valores[0]
#     for valor in valores[1:]:
#         if valor != 0:
#             resultado /= valor
#         else:
#             return "Erro: divisão por zero!"
#     return resultado

# while True:
#     print("Selecione a operação:")
#     print("1. Adição")
#     print("2. Subtração")
#     print("3. Multiplicação")
#     print("4. Divisão")

#     # Solicita ao usuário a escolha da operação
#     escolha = input("Digite sua escolha (1/2/3/4): ")

#     # Solicita ao usuário os valores para a operação
#     valores_operacao = []
#     while True:
#         valor = float(input("Digite um valor para a operação (ou digite 0 para finalizar): "))
#         if valor == 0:
#             break
#         valores_operacao.append(valor)

#     # Realiza a operação selecionada
#     if escolha == '1':
#         print("Resultado da adição dos valores:", adicao(valores_operacao))
#     elif escolha == '2':
#         print("Resultado da subtração dos valores:", subtracao(valores_operacao))
#     elif escolha == '3':
#         print("Resultado da multiplicação dos valores:", multiplicacao(valores_operacao))
#     elif escolha == '4':
#         print("Resultado da divisão dos valores:", divisao(valores_operacao))
#     else:
#         print("Escolha inválida!")

#     continuar = input("Deseja realizar outra operação? (sim/não): ")
#     if continuar.lower() != 'sim':
#         break


# 24: Classificador de Números
# def classificar_numero(numero):
#     if numero % 2 == 0:
#         return "par"
#     else:
#         return "ímpar"

# def verificar_positivo_negativo(numero):
#     if numero > 0:
#         return "positivo"
#     elif numero < 0:
#         return "negativo"
#     else:
#         return "zero"

# # Solicita ao usuário um número
# numero = float(input("Digite um número: "))

# # Classifica o número
# classificacao_paridade = classificar_numero(numero)
# classificacao_positivo_negativo = verificar_positivo_negativo(numero)

# # Imprime a classificação do número
# print("O número é", classificacao_paridade + ", " + classificacao_positivo_negativo + ".")


# 25: Conversão de Tipo com Validação
def converter_para_inteiro(valor):
    try:
        return int(valor)
    except ValueError:
        return None


def converter_para_float(valor):
    try:
        return float(valor)
    except ValueError:
        return None


while True:
    entrada = input("Digite um valor numérico: ")

    # Tenta converter para inteiro

    valor_inteiro = converter_para_inteiro(entrada)
    if valor_inteiro is not None:
        print("Valor inteiro:", valor_inteiro)
        break

    # Tenta converter para ponto flutuante
    valor_float = converter_para_float(entrada)
    if valor_float is not None:
        print("Valor de ponto flutuante:", valor_float)
        break

    print("Entrada inválida. Por favor, digite um valor numérico válido.")
