# EjercicioDados
Simulador de Dados con Python

Aplicación interactiva de consola que simula el lanzamiento de 
dados de distintos tipos (D4, D6, D8, D10, D12, D20). 

El programa permite al usuario:

 ● Seleccionar el tipo de dado.

 ● Indicar cuántos dados lanzar.

 ● Mostrar los resultados de manera visual y colorida usando la librería rich.

 ● Incluir una animación que simule el proceso de lanzar los dados.

 ● Guardar un historial de tiradas y presentarlo en una tabla visual.

Flujo funcional del programa (qué implementar)

- Mostrar menú para seleccionar tipo de dado (D4, D6, D8, D10, D12, D20).
- Pedir al usuario cuántos dados lanzar (validando que sea un entero positivo, límite razonable p.ej. <= 100).
- Simular la tirada (generar números aleatorios según número de caras).
- Mostrar animación que simule el lanzar.
- Mostrar resultados visuales y coloridos con rich (tabla, panel, emojis, barras, etc.).
- Guardar la tirada en un historial persistente (JSON o SQLite).
- Permitir ver el historial en una tabla rich y/o exportarlo.

Desarrollo:

- Instalamos con python -m pip install rich el paquete rich para que reconozca los imports, y nos aseguramos
con Ctrl + Shift + p en VS code en el campo Python: Python interpreter que está seleccionado el entorno correcto.

tirar_dado.py:

Utilizamos rich.console para texto bonito en la terminal, rich.table para mostrar varias tiradas en una tabla, rich.live para actualizar la pantalla constantemente, rich.sleep que controla la velocidad de esa animación y luego importamos random para generar los valores aleatorios de los dados.

1ª Funcion tirar_dado : 

sides indicará el número de caras, count el número de dados a lanzar. random randint generará un número aleatorio entre 1 y "sides". 

La list comprehension que va indicada entre [] generará todas las tiradas en una lista, teniendo en cuenta el número de dados tirados "range(count)".

Luego devuelve el resultado en "results" para llamarlo desde dados.py

2ª Funcion animacion_tirada:

Utiliza Live para crear un panel actualizandose en tiempo real en la consola.

Luego el refresh sirve para que se actualice la pantalla en el tiempo establecido.

Establecemos un bucle de ese dado rodando 20 pasos y actualizamos ese live.