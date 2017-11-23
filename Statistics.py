# -*- coding: utf-8 -*-

import statistics as stats

data = [2,2,5,6,8,8,8,9,7,8,5,2,6]
eleccion = 0



def mostrarMenu():
    print('-------OPCIONES-------')
    print('1. Mean (Media)')
    print('2. Harmonic_Mean')
    print('3. Median (Mediana)')
    print('4. Median_low')
    print('5. Median_high')
    print('6. Mode (Moda)')
    print('7. Pstdev (Desviación típica Poblacional)')
    print('8. Stdev (Desviación típica)')
    print('9. Pvariance (Varianza Poblacional)')
    print('10. Variance (Varianza)')


def introducir():
    print('Los valores por defecto son los siguientes: ')
    print('[2,2,5,6,8,8,8,9,7,8,5,2,6]')


while(eleccion == 0):
    introducir()
    mostrarMenu()
    prueba = input('Introduce la opción deseada: \n')

    if (prueba == '1'):
        resultado = stats.mean(data)
        print('La media de los datos es: %s' % resultado)
        print('Desea volver a ejecutar para realizar otra accion? 0 para si, cuaquier otro numero para no:')
        eleccion = input()

    if (prueba == '2'):
        resultado = stats.harmonic_mean(data)
        print('La media armónica de los datos es: %s' % resultado)
        print('Desea volver a ejecutar para realizar otra accion? 0 para si, cuaquier otro numero para no:')
        eleccion = input()

    if (prueba == '3'):
        resultado = stats.median(data)
        print('La mediana de los datos es: %s' % resultado)
        print('Desea volver a ejecutar para realizar otra accion? 0 para si, cuaquier otro numero para no:')
        eleccion = input()

    if (prueba == '4'):
        resultado = stats.median_low(data)
        print('La mediana_low de los datos es: %s' % resultado)
        print('Desea volver a ejecutar para realizar otra accion? 0 para si, cuaquier otro numero para no:')
        eleccion = input()

    if (prueba == '5'):
        resultado = stats.median_high(data)
        print('La mediana_high de los datos es: %s' % resultado)
        print('Desea volver a ejecutar para realizar otra accion? 0 para si, cuaquier otro numero para no:')
        eleccion = input()

    if (prueba == '6'):
        resultado = stats.mode(data)
        print('La moda de los datos es: %s' % resultado)
        print('Desea volver a ejecutar para realizar otra accion? 0 para si, cuaquier otro numero para no:')
        eleccion = input()

    if (prueba == '7'):
        resultado = stats.pstdev(data)
        print('La desviación típica pobacional de los datos es: %s' % resultado)
        print('Desea volver a ejecutar para realizar otra accion? 0 para si, cuaquier otro numero para no:')
        eleccion = input()

    if (prueba == '8'):
        resultado = stats.stdev(data)
        print('La desviación típica de los datos es: %s' % resultado)
        print('Desea volver a ejecutar para realizar otra accion? 0 para si, cuaquier otro numero para no:')
        eleccion = input()

    if (prueba == '9'):
        resultado = stats.pvariance(data)
        print('La variación poblacional de los datos es: %s' % resultado)
        print('Desea volver a ejecutar para realizar otra accion? 0 para si, cuaquier otro numero para no:')
        eleccion = input()

    if (prueba == '10'):
        resultado = stats.median(data)
        print('La variación estándar de los datos es: %s' % resultado)
        print('Desea volver a ejecutar para realizar otra accion? 0 para si, cuaquier otro numero para no:')
        eleccion = input()
