# Hundir la flota

Proyecto - Bootcamp The Bridge

Instrucciones del juego:
* Tablero de 10x10 casillas con 4 barcos de eslora 1, 3 barcos de eslora 2, 2 barcos de eslora 3 y 1 barco de eslora 4. El jugador puede posicionar sus barcos indicando las coordenadas `x,y` o puede posicionarlos aleatoriamente. Los barcos no podrán posicionarse juntos, deberán dejar como mínimo un cuadrado de distancia.
* El juego se realiza por turnos. El jugador empieza y si acierta, seguirá jugando, en caso contrario, le tocará a Pythonisa, la máquina. Pythonisa dispara a un punto aleatorio y sigue jugando hasta fallar.
* La partida termina cuando el jugador o Pythonisa hunden todos los barcos del contrincante o cuando el jugador pone `exit`.

Implementaciones del juego:
1. La partida inicia mostrando un mensaje al usuario y pidiendo un nombre de usuario.
2. El usuario decidirá si desea posicionar manualmente sus barcos o si desea que se genere un tablero aleatorio. No se admiten posiciones que no respeten el cuadrado de distancia. El jugador irá viendo la colocación de sus barcos en el tablero a medida que lo va realizando. En el caso de Pythonisa, su tablero de barcos se generará aleatoriamente respetando el cuadrado de distancia.
3. Si el usuario introduce coordenadas o direcciones incorrectas, se le avisará del error (número fuera de rango o carácter no válido) y le pedirá nuevamente el valor. 
4. Con cada disparo, se informará al jugador de si ha habido fallo ('Agua') o acierto ('Barco tocado' o 'Barco Hundido'). Del mismo modo, irá viendo en su tablero los aciertos ('X') y fallos ('○').
