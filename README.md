# UnidadM3

El siguiente proyecto se realizo una maquina de Galton que es una demostración física que ayuda a comprender cómo se distribuyen aleatoriamente las partículas o eventos y cómo esta distribución se acerca a una distribución normal a medida que aumenta el número de repeticiones.


En resumen, este código simula el funcionamiento de una Máquina de Galton, realiza una simulación de múltiples canicas que caen a través de la máquina y luego visualiza la distribución resultante en forma de histograma. Las bibliotecas NumPy y Matplotlib son esenciales para realizar cálculos y visualizaciones eficientes en el proceso.
   
Voy a describir el código de forma general para que se entienda 

1- Importación de Bibliotecas:
    import numpy as np
    import matplotlib.pyplot as plt
    from random import randint
  
  En este paso, se importan las bibliotecas necesarias:
    numpy (alias np) se utiliza para operaciones numéricas eficientes y para crear arreglos multidimensionales.
    matplotlib.pyplot (alias plt) se utiliza para crear visualizaciones, en este caso, un histograma.
    randint se importa desde random para generar números enteros aleatorios.
    
2.-Función simulate_galton_machine:
  def simulate_galton_machine(total_canicas, niveles):
  
  Esta función simula el funcionamiento de la Máquina de Galton.Los pasos dentro de la función son:

  Se crea una lista llamada canales que representa los contenedores en la máquina, inicializados con 0 canicas en cada uno.
  Se imprime la distribución inicial de los contenedores.
  Luego, se inicia un bucle que simula el proceso de dejar caer canicas en la máquina. En cada iteración:
  Se inicializa una variable almacenado a 0 para rastrear el nivel en el que se almacena la canica.
  Se realiza otro bucle para cada nivel en la máquina.
  En cada nivel, se genera un número aleatorio (0 o 1) usando randint(0, 1) para simular el rebote de la canica a la izquierda o derecha.
  Se actualiza el valor de almacenado según el resultado de los rebotes en todos los niveles.
  Se incrementa el contador del contenedor correspondiente en la lista canales según el nivel en el que se haya almacenado la canica.
  Después de que todas las canicas se han dejado caer, se imprime el número total de canicas utilizadas y la distribución final de los contenedores. Finalmente, se   devuelve la lista canales que contiene la distribución de canicas.
  
3.-Función plot_histogram:
  def plot_histogram(X, canales, niveles):
  
  Esta función crea y muestra un histograma que representa la distribución de canicas en los contenedores.Los pasos dentro de la función son:
  
  Se establece el título y las etiquetas de los ejes para el gráfico.
  Se utiliza plt.bar para crear el histograma, donde X representa los valores en el eje X (los contenedores) y canales contiene la cantidad de canicas en cada    
  contenedor.
  Finalmente, se muestra el gráfico utilizando plt.show().
  
4.- Función main:
  def main():
  Esta función es la entrada principal del programa. Aquí se configuran los parámetros iniciales, se llama a simulate_galton_machine para realizar la simulación y
  luego se llama a plot_histogram para mostrar la visualización.
  
5.Bloque Principal:
  if __name__ == "__main__":
    main()
  Este bloque verifica si el script se está ejecutando como programa principal. Si es así, llama a la función main para iniciar la simulación y mostrar el
  histograma.




Personalmente, este proyecto fue todo un desafío, ya que tuve dificultades en su desarrollo. Esto se debió a que inicialmente abordé el proyecto de manera bastante general y no utilicé funciones desde el principio. Además, tuve dificultades para comprender el funcionamiento de la Máquina de Galton, lo que incluye el concepto de distribución binomial. Para llevar a cabo el proyecto, tuve que leer e incluso consultar con mi tutor sobre cómo funcionaba. Todo iba bien hasta que me encontré con la situación en la que mi código no distribuía las canicas de manera proporcional en los contenedores, generando una distribución desigual. Afortunadamente, con la ayuda de mi tutor y algunos ejemplos, pude corregir mi código. En general, siento que las lecciones de este módulo fueron un tanto generales y que faltaba contenido para reforzar el aprendizaje.

