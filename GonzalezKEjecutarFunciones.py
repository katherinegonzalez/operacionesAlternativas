# ----------------------------------------------------------------------------------------
# PROGRAMA: Operaciones Matemáticas Alternativas
# ----------------------------------------------------------------------------------------
# Descripción: Este programa presenta un menú con 4 operaciones alternativas: encontrar
# digitos por derecha, encontrar digitos por izquierda, multiplicación rusa y máximo común
# divisor. Se ejecutrá la opción que el usuario seleccione.

# ----------------------------------------------------------------------------------------
# Autor: Katherine Xiomar González Santacruz
# Version: 1.0
# [05.09.2022]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
from GonzalezKOperacionesAlternativas import *  # modulo de python para este ejemplo (se usara para mostrar la fecha)

# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# ----------------------------------------------------------------------------------------

# Variables de entrada: (str) opcionIngresada
# pre-condiciones: opcionIngresada debe ser '1', '2', '3', '4', ó '0'
#                  salir != 'si'

# Variables auxiliares: (str) opcion
#                       opcion != '0'
#
# Explicación: opción es una variable auxiliar que guarda la opción ingresada por el usuario,
#              y se encarga de detener el ciclo cuando la opció seleccionada es '0'.
#              Si opcion es '0', el programa dejará de ejecutarse.
#              Si opcionIngresada es '1', se ejecuta la función digitosPorDerecha() del módulo importado
#              Si opcionIngresada es '2', se ejecuta la función digitosPorIzquierda() del módulo importado
#              Si opcionIngresada es '3', se ejecuta la función multiplicacionRusa() del módulo importado
#              Si opcionIngresada es '4', se ejecuta la función maxCD() del módulo importado
#              Si opcionIngresada es '0', se detiene el programa.
#
# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------
# Salida: Mensaje (str) informando los resultados de los cálculos realziados de acuerdo a
# la selección del usuario.

# Si opcionIngresada es un valor diferente de '0', '1', '2', '3' ó '4' mostrar un mensaje
# en pantalla, y solicitar el valor nuevamente.
# Si opcion == '0' , fin del programa.

# ----------------------------------------------------------------------------------------

opcion = ''

def condicionInput (opcionIngresada):
    return opcionIngresada == '1' or opcionIngresada == '2' or \
           opcionIngresada == '3' or opcionIngresada == '4' or opcionIngresada == '0'

while (opcion != '0'):
    print('\n')
    print('Programa Para Calcular Operaciones Matemáticas Alternativas')
    print('Seleccione una opción:')
    print('1. Dígitos por derecha')
    print('2. Dígitos por izquierda')
    print('3. Multiplicación Rusa')
    print('4. Máximo Común Divisor')
    print('0. Salir')
    opcion = validarInput('Ingrese opción: ', condicionInput)

    print('\n')
    if (opcion == '1'):
        digitosPorDerecha()
    elif (opcion == '2'):
        digitosPorIzquierda()
    elif (opcion == '3'):
        multiplicacionRusa()
    elif (opcion == '4'):
        maxCD()

# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------
