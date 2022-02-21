import numpy as np

class Tablero:
    '''
    Clase Tablero

    Returns
    -------
    tiros : list
    '''
    tiros = []

    def __init__(self,id,dim,barcos):
        '''
        Al iniciarse se crean los tableros
        
        Parameters
        ----------
        id : str
        dim : list(x,y)
        barcos : dic

        Returns
        -------
        id : str
        barcos : dic
        dim : list(x,y)
        t_barcos : array
        t_tiros : array
        '''
        self.id = id
        self.barcos = barcos
        self.dim = dim
        self.crear_tablero()
    
    def crear_tablero(self):
        '''
        Creación de los tableros para los barcos y los disparos.
        '''
        self.t_barcos = np.full(self.dim,' ')
        self.t_tiros = np.full(self.dim,' ')

    def buscar_coord(self,t_rival,x,y):
        '''
        Buscar las coordenadas en el tablero del rival, devuelve `bool`
        
        Parameters
        ----------
        t_rival : array
        x : int
        y : int
        
        Returns
        -------
        bool
        '''
        self.tiros.append([x,y])

        if t_rival[x,y]=='■':
            self.t_tiros[x,y]='X'
            t_rival[x,y]='X'
            return True
        elif t_rival[x,y]=='X':
            self.t_tiros[x,y]='X'
            t_rival[x,y]='X'
            return False
        else:
            self.t_tiros[x,y]='○'
            t_rival[x,y]='○'
            return False
            