class Nodo( ):
    def __init__( self, val ):
        self.val = val
        self.sig = None
    def Dar_sig( self, sig ):
        self.sig = sig
    def Ret_val( self ):
        return self.val
    def Ret_sig( self ):
        return self.sig

class Pila( ):
    def __init__( self ):
        self.cim = None
    def Ins( self, val ):
        aux = Nodo( val )
        if self.cim != None:
            aux.Dar_sig( self.cim )
            self.cim = aux
        else:
            self.cim = aux
    def Ext( self ):
        if self.cim != None:
            aux = self.cim
            self.cim = self.cim.Ret_sig( )
            del aux;
        else:
            print( "Pila vacia" )
    def Mos( self ):
        aux = self.cim
        while aux != None:
            print( aux.Ret_val( ) )
            aux = aux.Ret_sig( )

n = Pila( )
n.Ins( 4 )
n.Ins( 2 )
n.Ins( 5 )
n.Ins( 7 )
n.Mos( )
print( " -------- " )
n.Ext( )
n.Mos( )
print( " -------- " )

-holaaaaaaaa-
