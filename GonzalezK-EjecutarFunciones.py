# ----------------------------------------------------------------------------------------
# PROGRAMA: <<nombre del programa>>
# ----------------------------------------------------------------------------------------
# Descripción: <<breve descripción>>
# ----------------------------------------------------------------------------------------
# Autor: Luis Carlos Díaz
# Version: 2.0
# [18.07.2020]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
from operacionesAlternativas import * # modulo de python para este ejemplo (se usara para mostrar la fecha)
# https://www.delftstack.com/es/howto/python/python-import-from-parent-directory/#:~:text=Para%20importar%20un%20m%C3%B3dulo%20usando,el%20enfoque%20de%20paquete%20relativo.
# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# ----------------------------------------------------------------------------------------

# << aqui una explicación concreta >>

# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------

# << aqui una explicación concreta >>

# ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------
# listar aqui los parámetros

# <<Escriba desde aqui el código del programa...>>
opcion = ''

def validarInput (mensaje):
    seguirPreguntando = True
    while seguirPreguntando:
        opcionIngresada = input(mensaje)
        if (opcionIngresada == '1' or '2' or '3' or '4' or '0'):
            seguirPreguntando = False
        else:
            print('El valor ingresado no es válido')
    return opcionIngresada

while (opcion != '0'):
    print('\n')
    print('Seleccione una opción:')
    print('1. Digitos por derecha')
    print('2. Digitos por izquierda')
    print('3. Multiplicaciòn Rusa')
    print('4. Máximo Común Divisor')
    print('0. Salir')
    opcion = validarInput('Ingrese opción: ')

    if (opcion == '1'):
        digitosPorDerecha()
    if (opcion == '2'):
        digitosPorIzquierda()




# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------