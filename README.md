# EjercicioDados
Simulador de Dados con Python

Aplicación interactiva de consola que simula el lanzamiento de 
dados de distintos tipos (D4, D6, D8, D10, D12, D20). El programa permite 
al usuario:
 ● Seleccionar el tipo de dado.
 ● Indicar cuántos dados lanzar.
 ● Mostrar los resultados de manera visual y colorida usando la 
librería rich.
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