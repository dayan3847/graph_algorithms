

class nodoA:
    def __init__(self, val):
        self.dato = val
        self.padre = None
        self.izq = None
        self.der = None
    def __repr__(self):
        return str(self.dato)

class Arbol:
    def __init__(self):
        self.raiz = None
    def inserta(self, val):
        n = nodoA(val)
        y = None
        if self.raiz == None:
            self.raiz = n
        else:
            x = self.raiz
            while x != None:
                y = x
                if n.dato < x.dato:
                    x = x.izq
                else:
                    x = x.der
            if n.dato < y.dato:
                y.izq = n
            else:
                y.der = n
            n.padre = y
    def busca(self, val):
        x = self.raiz
        while x != None:
            if val == x.dato:
                break    
            if val < x.dato:
                x = x.izq
            else:
                x = x.der
        return x
    def _inorder(self, x):
        if x == None:
            return
        self._inorder(x.izq)
        print(x.dato)
        self._inorder(x.der)
    def inorder(self):
        self._inorder(self.raiz)


T = Arbol()

L = [40,20,60,10,70,30,50,5,55,45,35]
M = [40,21,60,17,70,33,50,59,55,45,135]

for i in L:
    T.inserta(i)

for i in M:
    x = T.busca(i)
    if x != None:
        print ("Encontramos el valor ",x.dato, " en el árbol")
    else:
        print ("No encontramos el valor ", i ," en el árbol")

T.inorder()





    
