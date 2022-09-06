# ----------------------------------------------------------------------------------------
# MODULO: <<nombre asociado al cojunto de funciones>>
# ----------------------------------------------------------------------------------------
# Descripción: <<breve descripción del módulo>>
# ----------------------------------------------------------------------------------------
# Autor: Katherine Xiomar González Santacruz
# Version: 2.0
# [18.07.2020]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS (un módulo puede importar otros módulos)

# import <<nombre modulo>>   # otro modulo propio o de Python que se quiera usar!

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
# FUNCIÓN: <<nombre de la función 1>>
# ----------------------------------------------------------------------------------------
# Descripcion: <<breve descripción de la función
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# ----------------------------------------------------------------------------------------


def esNumero(numero):
    return numero.isdigit()

def numeroIngresado(mensaje):
    numero = validarInput(mensaje, esNumero)
    return int(numero)
# ----------------------------------------------------------------------------------------
# FUNCIÓN: <<nombre de la función 1>>
# ----------------------------------------------------------------------------------------
# Descripcion: <<breve descripción de la función
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# ----------------------------------------------------------------------------------------
def digitosDeNumero(numero):
    digitos = []
    for i in range(len(str(numero))):
        digito = numero % 10
        numero = numero // 10
        digitos.append(digito)
    return digitos

# ----------------------------------------------------------------------------------------
# FUNCIÓN: <<nombre de la función 1>>
# ----------------------------------------------------------------------------------------
# Descripcion: <<breve descripción de la función
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# ----------------------------------------------------------------------------------------
def digitosPorIzquierda():
    print('Dígitos por Izquierda: ')
    numero = numeroIngresado('Ingrese un número entero: ')
    print('Los dígitos del número ' + str(numero) + ' de izquierda a derecha son: ')
    for digito in digitosDeNumero(numero)[::-1]:
        print(digito)

# ----------------------------------------------------------------------------------------
# FUNCIÓN: <<nombre de la función 2>> ... Y ASI PARA TODAS LAS FUNCIONES ...
# ----------------------------------------------------------------------------------------
# Descripcion: <<breve descripción de la función
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# ----------------------------------------------------------------------------------------

def digitosPorDerecha():
    print('Dígitos por Derecha: ')
    numero = numeroIngresado('Ingrese un número entero: ')
    print('Los dígitos del número ' + str(numero) + ' de derecha a izquierda son: ')
    for digito in digitosDeNumero(numero):
        print(digito)

# ----------------------------------------------------------------------------------------
# FUNCIÓN: <<nombre de la función 2>> ... Y ASI PARA TODAS LAS FUNCIONES ...
# ----------------------------------------------------------------------------------------
# Descripcion: <<breve descripción de la función
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
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
# FUNCIÓN: <<nombre de la función 2>> ... Y ASI PARA TODAS LAS FUNCIONES ...
# ----------------------------------------------------------------------------------------
# Descripcion: <<breve descripción de la función
# ----------------------------------------------------------------------------------------
# PARAMETROS & PRE-CONDICIONES
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
# ----------------------------------------------------------------------------------------

def maxCD():
    print('máximo común divisor')


# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------