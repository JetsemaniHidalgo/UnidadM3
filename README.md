# UnidadM3

El siguiente proyecto se realizo una maquina de Galton que es una demostración física que ayuda a comprender cómo se distribuyen aleatoriamente las partículas o eventos y cómo esta distribución se acerca a una distribución normal a medida que aumenta el número de repeticiones, esto no ayudo a realizar mediante funsiones y usar numpy para las funciones matematicas  y matplotlib para las graficas 

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
