def comparar_numeros(a , b):
    resultado = ""
    
    if a > b:
        resultado = f" O número {a} é maior que {b}."
    elif a < b:
        resultado = f"O número {a} é menor que {b}."
    else:
        resultado = "Os números são iguais."
    
    return resultado





def multiplicar_tres_numeros(a, b, c):
    resultado = a * b * c
    return resultado




def calcular_potencia(base, expoente):
    return base ** expoente

resultado = calcular_potencia(4,3)
print(resultado)


def verificar_idade():
    idade = int(input("Digite sua idade: "))
    if idade == 18:
        print("Parabéns! Você atingiu a maioridade.")
    else:
        print("Sua idade é:", idade)

verificar_idade()

from datetime import date

def calcular_idade(dia: int, mes: int, ano: int) -> int:
    """Calcula a idade de uma pessoa com base na data de nascimento."""
    hoje = date.today()
    idade = hoje.year - ano - ((hoje.month, hoje.day) < (mes, dia))
    return idade



dia_nasc, mes_nasc, ano_nasc = 15, 8, 2000
idade = calcular_idade(dia_nasc, mes_nasc, ano_nasc)
print(f"A pessoa tem {idade} anos.")



