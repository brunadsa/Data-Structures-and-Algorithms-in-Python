

class Node(object):

    def __init__(self, valor):
        self.candidato = valor
        self.votos = 1
        self.next = None

class listaDeCandidatos(object):

    def __init__(self):
        self.head = None
        self.size = 0
        self.maior = 0
        self.candi = 0

    def insertStart(self, value):  # O(1)
        self.size += 1 #tamanho da lista
        newNode = Node(value)  # instance the class Node for create a new Node
        if not self.head:  # if isn't have a head
            self.head = newNode  # head pointer points to newNode
        else:  # else
            newNode.next = self.head  # nextNode pointer of the newNode
            # points to the Node what the head had have point
            self.head = newNode  # In the end, it updates the head for a newNode

    def verificaCandidato(self, candidato2):

        currentNode = self.head
        while currentNode is not None and currentNode.candidato != candidato2:
            currentNode = currentNode.next
        if currentNode is not None:
            currentNode.votos = currentNode.votos + 1
            if self.maior < currentNode.votos:
                self.maior = currentNode.votos
                self.candi = currentNode.candidato
            return True
        else:
            return False

    def size1(self):  # O(1)
        return self.size


votos = [1, 2, 3, 4, 5, 2, 5, 6, 5, 3, 5, 1, 5, 5]
# n = 14
# k = 6
# 1, 2, 3, 4, 5, 6

# 1
# 1, 2
# 1, 2, 3
# 1, 2, 3, 4
# 1, 2, 3, 4, 5

#Exemplo
# n = 3000
# k = 10
# 10*10 < 3000 -> 100 < 3000

#Contra Exemplo
# n = 5
# k = 4
# 4*4 > 5 -> 16 > 5

# O(n + k^2)
apuracao = listaDeCandidatos()

for i in votos:
    veri = apuracao.verificaCandidato(i)
    if veri is False:
        apuracao.insertStart(i)

print apuracao.candi