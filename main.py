from functions import *
from variables import dimensiones,barcos
from clases import Tablero

print('\nBienvenido/a al juego de Hundir la Flota\n¿Podrás ganar a Pythonisa?\n¡Adelante!\n')

id = input('¿Cómo te llamas?\n')
print(f'\n¡Comenzemos {id}!\n')

pythonisa = Tablero('Pythonisa',dimensiones,barcos)
user = Tablero(id,dimensiones,barcos)

inicio_partida(barcos,user.t_barcos,pythonisa.t_barcos)

print(f'\nEmpieza tu turno {user.id}\n')

if contar_barcos(user.t_barcos)==20:
    while contar_barcos(user.t_barcos)!=0 and contar_barcos(pythonisa.t_barcos)!=0:
        mostrar_tablero(user.t_tiros,user.t_barcos,pythonisa.t_tiros,pythonisa.t_barcos)
        x,y = coor_user(user.t_tiros)
        if x=='exit' or y=='exit':break
        coind = user.buscar_coord(pythonisa.t_barcos,x,y)
        while coind==True:
            if contar_barcos(user.t_barcos)==0 or contar_barcos(pythonisa.t_barcos)==0: break
            aviso_user(coind,x,y,pythonisa.t_barcos)
            mostrar_tablero(user.t_tiros,user.t_barcos,pythonisa.t_tiros,pythonisa.t_barcos)
            x,y = coor_user(user.t_tiros)
            if x=='exit' or y=='exit':break
            coind = user.buscar_coord(pythonisa.t_barcos,x,y)
        if x=='exit' or y=='exit':break
        aviso_user(coind,x,y,pythonisa.t_barcos)

        x,y = coor_random(pythonisa.tiros)
        num = 0
        while pythonisa.buscar_coord(user.t_barcos,x,y)==True:
            x,y = coor_random(pythonisa.tiros)
            num+=1
        print(f'\nPythonisa ha acertado {num} veces\n¡Tu turno!\n')

if contar_barcos(pythonisa.t_barcos)!=0:
    print('\nGame over :(\nPythonisa ha ganado\n')
else:
    print('\n¡Enhorabuena! Has derrotado a Pythonisa\n')

print(f'\nLa partida ha quedado así:\n')
mostrar_tablero(user.t_tiros,user.t_barcos,pythonisa.t_tiros,pythonisa.t_barcos,True)