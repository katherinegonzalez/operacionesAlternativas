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

def numeroIngresado():
    numero = validarInput('Ingrese un número entero: ', esNumero)
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
    numero = numeroIngresado()
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
    numero = numeroIngresado()
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
    print('multiplicación Rusa')

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