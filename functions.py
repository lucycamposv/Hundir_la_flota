import numpy as np
import random

def pos_random_user():
    '''
    Pide al usuario si desea posicionar los barcos. `SI` o `NO`.

    Returns
    -------
    i_user : str
    '''

    i_user = input('¿Quieres posicionar tus barcos?\nIntroduce SI o NO\n').upper()
    while i_user!= 'SI' and i_user!='NO':
        i_user = input('No válido.\nIntroduce SI o NO\n').upper()
    
    if i_user == 'SI':
        return True
    else:
        return False

def inicio_partida(barcos,user_barcos,pythonisa_barcos):
    '''
    Inicia la partida posicionando los barcos en funcion de si el usuario lo quiere aleatorio

    Parameters
    ----------
    barcos : dic
    user_barcos : array
    pythonisa_barcos : array
    '''
    pos_user = pos_random_user()

    if pos_user==True:
        tablero_barcos_user(barcos,user_barcos)
        tablero_barcos_random(barcos,pythonisa_barcos)
    else:
        tablero_barcos_random(barcos,user_barcos)
        tablero_barcos_random(barcos,pythonisa_barcos)

def coor_random(disparos=[]):
    '''
    Genera coordenadas aleatorias `x,y` comprobando que no se hayan utilizado antes.
    
    Parameters
    ----------
    disparos : list (Defaul [])

    Returns
    -------
    x : int
    y : int
    '''
    x = np.random.randint(10)
    y = np.random.randint(10)

    while [x,y] in disparos:
        x = np.random.randint(10)
        y = np.random.randint(10)

    return x,y

def direc_random(val_dir):
    '''
    Selecciona una orientación aleatoria entre `N,S,E,O`.

    Returns
    -------
    orientacion : str
    '''
    direc= random.choice(val_dir)
    return direc

def coor_user(tablero):
    '''
    Pide valores al usuario para obtener las coordenadas `x,y` o `exit` para finalizar la partida.
    
    Parameters
    ----------
    tablero : array
    
    Returns
    -------
    x : int or str
    y : int or str
    '''
    x = input(f'Introduzca un valor de Fila.\nRango: 1-{len(tablero)}\n')
    while True:
        try:
            x = int(x)-1
            if -1<x<len(tablero):
                y = input(f'Introduzca un valor de Columna.\nRango: 1-{len(tablero)}\n')
                while True:
                    try:
                        y = int(y)-1
                        if -1<y<len(tablero): break
                        else: y = input('Número fuera de rango.\nIntroduzca la Columna:\n')
                    except:
                        if y=='exit':break
                        y = input('No válido.\nIntroduzca la columna:\n')
                break             
            else: x = input('Número fuera de rango.\nIntroduzca la Fila:\n')
        except:
            if x=='exit':
                y = 0
                break
            x = input('No válido.\nIntroduzca un nuevo valor para la Fila:\n')

    return x,y

def direc_user():
    '''
    Pide la orientación al usuario entre `N,S,E,O`.

    Returns
    -------
    direc : str
    '''
    
    direc = input('Introduzca la orientación de su barco -> N,S,E,O\n').upper()
    val_dir = ['N','S','E','O']
    while direc not in val_dir:
        direc = input('No válido.\nIntroduzca la orientación de su barco -> N,S,E,O\n').upper()
    
    return direc

def coind_barco(x,y,direc,eslora,tablero):
    '''
    Busca la coincidencia con otro barco y retorna un `bool`.
    
    Parameters
    ----------
    x : int
    y : int
    direc : str
    eslora : int
    tablero : array
    
    Returns
    -------
    coind : bool
    '''
    num = 0
    if direc=='S':
        if x-1>=0:
            f=x-1
        else:
            f=0

        if y-1>=0:
            c=y-1
        else:
            c=0
        
        for i in tablero[f:x+eslora+1,c:y+2]:
            for j in i:
                if j=='■':
                    num+=1
    elif direc=='N':
        if x-eslora>=0:
            f=x-eslora
        else:
            f=0

        if y-1>=0:
            c=y-1
        else:
            c=0

        for i in tablero[f:x+2,c:y+2]:
            for j in i:
                if j=='■':
                    num+=1
    elif direc=='E':
        if x-1>=0:
            f=x-1
        else:
            f=0

        if y-1>=0:
            c=y-1
        else:
            c=0

        for i in tablero[f:x+2,c:y+eslora+1]:
            for j in i:
                if j=='■':
                    num+=1
    elif direc=='O':
        if x-1>=0:
            f=x-1
        else:
            f=0

        if y-eslora>=0:
            c=y-eslora
        else:
            c=0

        for i in tablero[f:x+2,c:y+2]:
            for j in i:
                if j=='■':
                    num+=1

    if num!=0:
        return True
    else:
        return False
    
def coloc_barco(x,y,direc,eslora,tablero,user=False):
    '''
    Posiciona el barco en el tablero probando todas las orientaciones `user=False` o la orientación indicada por el usuario `user=True`. Retorna un `bool`.

    Parameters
    ----------
    x : int
    y : int
    direc : str
    eslora : int
    tablero : array
    user : bool (Default False)
    
    Returns
    -------
    bool
        
    '''
    val_dir = ['N','S','E','O']
    
    while len(val_dir)>1:
        coind = coind_barco(x,y,direc,eslora,tablero)

        if direc=='S' and x+(eslora-1)<len(tablero) and coind==False:
            tablero[x:x+eslora,y] = '■'
            a = True
            break
        elif direc=='N' and x-(eslora-1)>=0 and coind==False:
            tablero[x-(eslora-1):x+1,y] = '■'
            a = True
            break
        elif direc=='E' and y+(eslora-1)<len(tablero) and coind==False:
            tablero[x,y:y+eslora] = '■'
            a = True
            break
        elif direc=='O' and y-(eslora-1)>=0 and coind==False:
            tablero[x,y-(eslora-1):y+1] = '■'
            a = True
            break
        else:
            a = False
            if user==False:
                val_dir.remove(direc)
                direc = direc_random(val_dir)
            else:
                break
    
    return a

def tablero_barcos_random(barcos,tablero):
    '''
    Posiciona todos los barcos en el tablero de forma aleatoria, evitando coincidencias entre ellos y con periferia mínima de 1.

    Parameters
    ----------
    barcos : dic
    tablero : array

    '''
    for index,val in barcos.items():
        a = index
        while a>0:
            x,y = coor_random()
            direc = direc_random(['N','S','E','O'])
            while coloc_barco(x,y,direc,val,tablero)==False:
                x,y = coor_random()
                direc = direc_random(['N','S','E','O'])
            a-=1

def tablero_barcos_user(barcos,tablero):
    '''
    Posiciona todos los barcos en el tablero pidiendo las coordenadas y orientación al usuario.

    Parameters
    ----------
    barcos : dic
    tablero : array
    '''
    x,y = 0,0
    for index,val in barcos.items():
        a = index
        while a>0:
            print(f'\nIntroduzca las coordenadas para el barco de eslora {val}\n')
            x,y = coor_user(tablero)
            if x=='exit' or y=='exit':break
            if val!=1:
                    direc = direc_user()
            while coloc_barco(x,y,direc,val,tablero,True)==False:
                print(f'\nCoordenadas incorrectas.\n')
                x,y = coor_user(tablero)
                if x=='exit' or y=='exit':break
                if val!=1:
                    direc = direc_user()
            if x=='exit' or y=='exit':break
            print('\nBarco posicionado\n')
            print(tablero)
            a-=1
        if x=='exit' or y=='exit':break

def contar_barcos(tablero):
    '''
    Cuenta los ■ dentro del tablero. Devuelve un `int`.

    Parameters
    ----------
    tablero : array
    '''
    num = 0
    for i in tablero:
        for j in i:
            if j=='■':
                num+=1
    return num

def aviso_user(tiros,x,y,tablero):
    '''
    Muestra un mensaje del tiro realizado por el usuario.

    Parameters
    ----------
    tiros : bool
    '''
    if tiros == True:
        if coind_barco(x,y,'N',1,tablero)==False:
            print('\n¡Has hundido un barco!\nSigue jugando\n')
        else:  
            print('\n¡Has tocado un barco!\nSigue jugando\n')
    elif tablero[x,y]=='X':
        print('\nCoordendas reptidas.\nTurno de Pythonisa')
    else:
        print('\n¡Agua!\nTurno de Pythonisa\n')

def mostrar_tablero(user_disparos,user_barcos,pythonisa_disparos,pythonisa_barcos,fin=False):
    '''
    Muestra los tableros de los jugadores.
    
    Parameters
    ----------
    user_disparos : array
    user_barcos : array
    pythonisa_disparos : array
    pythonisa_barcos : array
    fin : bool (Default True)
    '''
    print(f'\nTus disparos\n{user_disparos}\nTus barcos\n{user_barcos}\n')
    if fin == True:
        print(f'\nPythonisa disparos\n{pythonisa_disparos}\nPythonisa barcos\n{pythonisa_barcos}\n')
        print('\nFIN DEL JUEGO') 
