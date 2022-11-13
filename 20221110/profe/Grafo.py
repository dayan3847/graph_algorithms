#! /usr/bin/python3
# coding UTF-8


"""
Implementación de un grafo.

 Esta clase define de manera 'cándida' un grafo en python, y el objetivo es
 puramente didáctico. Por 'cándida' nos referimos a que se basa en la definición
 formal de lo que es un grafo, para su implementación.
 
 Un **grafo** $G$ consiste de un conjunto finito $V$ cuyos miembros son llamados **vértices** y un conjunto A compuesto por duplas de elementos de $V$, cuyos elementos conocemos como **aristas**. Usualmente escribimos $G=(V,A)$, y decimos que $V$ es el **conjunto de Vertices** y $A$ es el **conjunto de aristas**.

 Los conjuntos de vértices y aristas se almacenan en dos listas y el posible
 valor de ponderación asociado a un vértice se almacena en una lista.

 Las aristas se almacenan como tuplas con dos elementos que deben pertencer a
 al conjunto de vertices.

 El grafo puede ser definido como un grafo dirigido o no dirigio, definiendo
 el atributo tipo. El valor estandar es no dirigido. Los valores que debe tomar
 el atributo tipo son: "```Dirigido```" o "```noDirigido```"(default).

"""

class Grafo:
   def __init__(self):
      self.V = [] #Lista de vertices
      self.A = [] #Lista de Aristas
      self.P = {} #Ponderación de cada arista.
      self.tipo = "noDirigido"

   #Agregamnos un vértice al grafo
   def agregaVertice(self, v):
      if v not in self.V:
         self.V.append(v)

   #Agrega la arista que relaciona a
   #los vértices u y v.
   def agregaArista(self, u, v):
      if u in self.V and v in self.V and (u,v) not in self.A:
         if self.tipo != "noDirigido":
            self.A.append([u,v])
         else:
            if [v,u] not in self.A:
               self.A.append([u,v])

   def eliminaVertice(self, v):
      if v not in self.V:
         return
      for u in self.V:
         if [u, v] in self.A:
            self.A.remove([u,v]) 
         if [v, u] in self.A:
            self.A.remove((v,u))
      self.V.remove(v)

   def eliminaArista(self, u, v):
      if u in self.V and v in self.V:
         if [u,v] in self.A:
            self.A.remove([u,v])
         if self.tipo == "noDirigido":
            if (v,u) in self.A:
               self.A.remove((v,u))
               
   def existeVertice(self, v):
      return v in self.V
   
   def existeArista(self, u, v):
      if u in self.V and v in self.V:
         if self.tipo != "noDirigido":
            return [u, v] in self.A
         else:
            return [u, v] in self.A or [v, u] in self.A
   def valencia(self, v):
      acum=0
      if v in self.V:
         for u in self.V:
            if self.existeArista(u, v):
               acum += 1
         return acum
      else:
         return -1
   # Nos regresa la lista de nodos adyacentes al vertice u.
   def Ady(self, u):
      L=[]
      for v in self.V:
         if self.existeArista(u,v) == True:
            L.append(v)
      return L

if __name__ == "__main__":
   #Instanciamos un objeto de la clase grafo.
   A=Grafo()

   #Agregamos vértices a nuestro grafo.
   for i in [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
       A.agregaVertice(i)

   #Agregamos arístas a nuestro grafo
   A.agregaArista('A', 'B')
   A.agregaArista('A', 'E')
   A.agregaArista('A', 'F')
   A.agregaArista('B', 'F')
   A.agregaArista('B', 'C')
   A.agregaArista('C', 'G')
   A.agregaArista('C', 'D')
   A.agregaArista('D', 'G')
   A.agregaArista('D', 'H')
   A.agregaArista('G', 'F')
   A.agregaArista('G', 'H')

   #Imprimimos la valencia de cada vertice del grafo
   for v in A.V:
      print ("La valencia del vertices %s es %d"% (v, A.valencia(v)))


   # Probamos el método para determinar si existe una arista en el grafo,
   # así como para eliminar una arista del grafo.

   print("¿Existe una arista entre el vertice 'A' y el vertice 'F'?: ",A.existeArista('A','F'))
   print("Eliminamos la ariste que une a los vertices 'A' y 'F'")
   A.eliminaArista('A','F')
   print("¿Existe una arista entre el vertice 'A' y el vertice 'F'?: ",A.existeArista('A','F'))
   print(A.existeArista('A','F'))

   #Probamos el métodos que elimina un vertice del grafo
   print(A.V)
   print(A.A)
   A.eliminaVertice('d')
   print(A.V)
   print(A.A)


# Esto ultimo unicamente lo hacemos para mostrar como añadir información
# a las aristas del grafo.

   print()
   print ("A.A", A.A)
   print()
   for a in A.A:
      a.append(1.0)
   print ("A.A", A.A)
