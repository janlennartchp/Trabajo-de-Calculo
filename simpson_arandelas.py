"""
Trabajo de Investigacion Formativa - Calculo Integral
Metodo numerico: Regla de Simpson 1/3 compuesta
Aplicacion: Volumen de un solido de revolucion por arandelas

Problema usado:
La region entre R(x)=1+e^(-x/2) y r(x)=x/4, en [0,2], gira alrededor del eje x.
V = pi * integral_a^b [R(x)^2 - r(x)^2] dx

No se usan funciones de integracion numerica predefinidas.
"""

import math
import time


def radio_exterior(x):
    """R(x): radio exterior de la arandela."""
    return 1 + math.exp(-x / 2)


def radio_interior(x):
    """r(x): radio interior de la arandela."""
    return x / 4


def integrando_volumen(x):
    """Funcion que se integra para volumen por arandelas: R(x)^2 - r(x)^2."""
    R = radio_exterior(x)
    r = radio_interior(x)
    return R**2 - r**2


def simpson_un_tercio_compuesto(f, a, b, n):
    """
    Aproxima la integral definida de f(x) en [a,b] usando Simpson 1/3 compuesto.

    Parametros:
        f: funcion a integrar
        a: limite inferior
        b: limite superior
        n: numero de subintervalos, debe ser par y positivo

    Retorna:
        Aproximacion numerica de la integral
    """
    if n <= 0:
        raise ValueError("El numero de subintervalos debe ser positivo.")
    if n % 2 != 0:
        raise ValueError("Para Simpson 1/3, el numero de subintervalos debe ser par.")

    h = (b - a) / n
    suma = f(a) + f(b)

    for i in range(1, n):
        x_i = a + i * h
        if i % 2 == 0:
            suma += 2 * f(x_i)
        else:
            suma += 4 * f(x_i)

    return (h / 3) * suma


def volumen_arandelas_simpson(a, b, n):
    """Calcula el volumen aproximado: V = pi * integral [R^2-r^2] dx."""
    integral_aprox = simpson_un_tercio_compuesto(integrando_volumen, a, b, n)
    return math.pi * integral_aprox


def volumen_exacto():
    """
    Solucion analitica del problema propuesto.

    V = pi * integral_0^2 [(1+e^(-x/2))^2 - (x/4)^2] dx
      = pi * [41/6 - e^(-2) - 4e^(-1)]
    """
    return math.pi * (41 / 6 - math.exp(-2) - 4 * math.exp(-1))


def ejecutar_caso_base():
    """Ejecuta el caso principal con varios valores de n para comparar errores."""
    a = 0
    b = 2
    exacto = volumen_exacto()
    valores_n = [4, 8, 16, 32, 64, 100]

    print("METODO DE SIMPSON 1/3 - VOLUMEN POR ARANDELAS")
    print("Problema: R(x)=1+e^(-x/2), r(x)=x/4, intervalo [0,2]")
    print(f"Valor exacto del volumen: {exacto:.12f}\n")
    print(" n       Aproximacion        Error absoluto        Error relativo (%)")
    print("--------------------------------------------------------------------")

    for n in valores_n:
        inicio = time.perf_counter()
        aproximado = volumen_arandelas_simpson(a, b, n)
        fin = time.perf_counter()
        error_abs = abs(exacto - aproximado)
        error_rel = (error_abs / abs(exacto)) * 100
        print(f"{n:3d}   {aproximado:16.12f}   {error_abs:16.12e}   {error_rel:16.12e}")
        # El tiempo esta disponible si se desea analizar eficiencia:
        # print(f"Tiempo para n={n}: {fin - inicio:.8f} segundos")


def ejecutar_con_datos_usuario():
    """Permite al usuario ingresar limites y numero de subintervalos para el mismo modelo."""
    print("\nIngrese datos para calcular V = pi * integral [R(x)^2 - r(x)^2] dx")
    print("Se usara R(x)=1+e^(-x/2) y r(x)=x/4")
    a = float(input("Limite inferior a: "))
    b = float(input("Limite superior b: "))
    n = int(input("Numero de subintervalos n (par): "))

    volumen = volumen_arandelas_simpson(a, b, n)
    print(f"Volumen aproximado: {volumen:.12f}")


if __name__ == "__main__":
    ejecutar_caso_base()

    opcion = input("\nDesea probar otros limites con el mismo modelo? (s/n): ").strip().lower()
    if opcion == "s":
        ejecutar_con_datos_usuario()
