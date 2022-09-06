# ----------------------------------------------------------------------------------------
# MODULO: Operaciones Alternativas
# ----------------------------------------------------------------------------------------
# Descripción: En este módulo se encuentran las funciones de las operaciones: encontrar
# dígitos por derecha, encontrar dígitos por izquierda, multiplicación rusa y máximo común
# divisor. También se encuentran algunas funciones auxiliares: validarInput, esNumero, y
# numeroIngresado
# ----------------------------------------------------------------------------------------
# Autor: Katherine Xiomar González Santacruz
# Version: 1.0
# [05.09.2022]
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# FUNCIÓN: validarInput
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para validar el valor ingresado por el usuario
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (str) mensaje, (function) condicion
#       variable auxiliar: (bool) seguirPreguntando
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Si seguir preguntando es false, el ciclo se rompe y se retorna el valor ingresado
#           por el usuario.
#           Si la condición no se cumple imprime un mensaje en pantalla
#       Valor de retorno: (str) opcionIngresada
# ----------------------------------------------------------------------------------------
def validarInput (mensaje, condicion):
    seguirPreguntando = True
    while seguirPreguntando:
        opcionIngresada = input(mensaje)
        if (condicion(opcionIngresada)):
            seguirPreguntando = False
        else:
            print('El valor ingresado no es válido')
    return opcionIngresada

# ----------------------------------------------------------------------------------------
# FUNCIÓN: esNumero
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para validar si el valor recibido es un número
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (str) número
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Si es numero retorna True, de lo contrario retorna False
#       Valor de retorno: bool (True o False)
# ----------------------------------------------------------------------------------------
def esNumero(numero):
    return numero.isdigit()

# ----------------------------------------------------------------------------------------
# FUNCIÓN: numeroIngresado
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para capturar el numero ingresado por el usuario y
# convertirlo en entero
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (str) mensaje (mensaje a mostrar en el input)
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       Valor de retorno: int (numero)
# ----------------------------------------------------------------------------------------
def numeroIngresado(mensaje):
    numero = validarInput(mensaje, esNumero)
    return int(numero)

# ----------------------------------------------------------------------------------------
# FUNCIÓN: digitosDeNumero
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para encontrar los dígitos de un número
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (int) numero
#       variable auxiliar: (list) digitos, (int) digito
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Retornar una lista de los digitos del número ingresado (de derecha a izquierda)
#       Valor de retorno: (list) digitos
# ----------------------------------------------------------------------------------------
def digitosDeNumero(numero):
    digitos = []
    for i in range(len(str(numero))):
        digito = numero % 10
        numero = numero // 10
        digitos.append(digito)
    return digitos

# ----------------------------------------------------------------------------------------
# FUNCIÓN: digitosPorIzquierda
# ----------------------------------------------------------------------------------------
# Descripción: función que imprime los dígitos de un número ingresado por el usuario, de
# izquierda a derecha
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (int) numero
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Se imprimen los dígitos del número ingresado de izquierda a derecha
#           Si el valor ingresado no es un número entero, se muestra un mensaje y se vuelve a
#           pedir el número
# ----------------------------------------------------------------------------------------
def digitosPorIzquierda():
    print('Dígitos por Izquierda: ')
    numero = numeroIngresado('Ingrese un número entero: ')
    print('Los dígitos del número ' + str(numero) + ' de izquierda a derecha son: ')
    for digito in digitosDeNumero(numero)[::-1]:
        print(digito)

# ----------------------------------------------------------------------------------------
# FUNCIÓN: digitosPorDerecha
# ----------------------------------------------------------------------------------------
# Descripción: función que imprime los dígitos de un número ingresado por el usuario, de
# derecha a izquierda
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (int) numero
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Se imprimen los dígitos del número ingresado de derecha a izquierda
#           Si el valor ingresado no es un número entero, se muestra un mensaje y se vuelve a
#           pedir el número
# ----------------------------------------------------------------------------------------
def digitosPorDerecha():
    print('Dígitos por Derecha: ')
    numero = numeroIngresado('Ingrese un número entero: ')
    print('Los dígitos del número ' + str(numero) + ' de derecha a izquierda son: ')
    for digito in digitosDeNumero(numero):
        print(digito)

# ----------------------------------------------------------------------------------------
# FUNCIÓN: multiplicacionRusa
# ----------------------------------------------------------------------------------------
# Descripción: función que calcula e imprime el resultado de la multiplicación rusa de dos
# números ingresados por el usuario.
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (int) multiplicador, (int) multiplicando
#       Variables auxiliares: (str) multiplicacion, (int) sumaMultiplicandos
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Se imprimen en pantalla el resultado de la multiplicación rusa de los números ingresados.
#           Si los valores ingresados no son un números enteros, se muestra un mensaje y se vuelven a
#           pedir los números
# ----------------------------------------------------------------------------------------
def multiplicacionRusa():
    print('Multiplicación Rusa: ')
    multiplicador = numeroIngresado('Ingrese el multiplicador (debe ser un numero entero): ')
    multiplicando = numeroIngresado('Ingrese el multiplicando (debe ser un numero entero): ')
    multiplicacion = str(multiplicador) + 'x' + str(multiplicando)

    sumaMultiplicandos = 0

    while (multiplicador != 1):

        if (multiplicador % 2 != 0):
            sumaMultiplicandos = sumaMultiplicandos + multiplicando

        multiplicando = multiplicando * 2
        multiplicador = multiplicador // 2

    if (multiplicador == 1):
        sumaMultiplicandos = sumaMultiplicandos + multiplicando

    print('El resultado de la multiplicación Rusa de ', multiplicacion, ' es: ', str(sumaMultiplicandos))

# ----------------------------------------------------------------------------------------
# FUNCIÓN: encontrarMaxCD
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para retornar el máximo común divisor de dos números
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (int) numeroMayor, (int) numero1, (int) numero2
#       Variables auxiliares: (int) divisor
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Si el módulo de los dos números ingresados por el divisor es cero, retornar número
#           (Máximo común divisor)
#       Valor de retorno: (int) divisor (máximo común divisor)
# ----------------------------------------------------------------------------------------
def encontrarMaxCD (numeroMayor, numero1, numero2):
    for i in range(numeroMayor):
        divisor = numeroMayor - i
        if (numero1 % divisor == 0 and numero2 % divisor == 0):
            return divisor

# ----------------------------------------------------------------------------------------
# FUNCIÓN: maxCD
# ----------------------------------------------------------------------------------------
# Descripción: función que calcula e imprime el máximo común divisor de dos números
# ingresados por el usuario.
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (int) numero1, (int) numero2
#       Variables auxiliares: (int) maximoComunDivisor
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Se imprime en pantalla el máximo común divisor de los números ingresados
#           Si los valores ingresados no son un números enteros, se muestra un mensaje y se vuelven a
#           pedir los números.
# ----------------------------------------------------------------------------------------
def maxCD():
    print('Máximo Común Divisor: ')
    print('Ingrese dos números para calcular el máximo común divisor: ')
    numero1 = numeroIngresado('Ingrese el primer número (debe ser un numero entero): ')
    numero2 = numeroIngresado('Ingrese el segundo número (debe ser un numero entero): ')

    if (numero1 > numero2):
        numeroMayor = numero1
    else:
        numeroMayor = numero2

    maximoComunDivisor = encontrarMaxCD(numeroMayor, numero1, numero2)

    print('El máximo común divisor de ', numero1, ' y ', numero2, ' es: ', maximoComunDivisor)

# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------