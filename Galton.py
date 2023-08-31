import numpy as np
import matplotlib.pyplot as plt
from random import randint

def simulate_galton_machine(total_canicas, niveles):
    """
    Simula el funcionamiento de una máquina de Galton.

    Args:
        total_canicas (int): El número total de canicas a utilizar.
        niveles (int): El número de niveles en la máquina.

    Returns:
        list: Una lista que representa la distribución de canicas en los contenedores.
    """
    canales = [0] * (niveles + 1)
    print("Distribución inicial de los contenedores:", canales)

    for h in range(total_canicas):
        almacenado = 0
        for j in range(niveles):
            almacenado += randint(0, 1)
        canales[almacenado] += 1

    print(total_canicas, "canicas fueron utilizadas en total.")
    print("Distribución Final de los contenedores:", canales)
    return canales

def plot_histogram(X, canales, niveles):
    """
    Grafica un histograma de la distribución de canicas en los contenedores.

    Args:
        X (numpy.ndarray): Valores en el eje X (contenedores).
        canales (list): Distribución de canicas en los contenedores.
        niveles (int): El número de niveles en la máquina.

    Returns:
        None
    """
    plt.title('Simulación de Máquina de Galton - Histograma')
    plt.suptitle('Gráfica de Galton')
    plt.xlabel('Contenedor')
    plt.ylabel('Cantidad de Canicas')
    plt.bar(X, canales, width=0.8)
    plt.show()

def main():
    total_canicas = 3000
    niveles = 11

    # Simular el funcionamiento de la máquina de Galton
    canales = simulate_galton_machine(total_canicas, niveles)

    # Preparar datos para la gráfica
    X = np.arange(0, niveles + 1)

    # Graficar el histograma de la distribución de canicas
    plot_histogram(X, canales, niveles)

if __name__ == "__main__":
    main()
