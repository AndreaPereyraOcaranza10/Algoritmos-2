class AVLTree:
    root = None
class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None
    h = 0

#PrintTree
def get_height(node):
    if node is None:
        return -1
    return node.h

def get_balance(node):
    if node is None:
        return 0
    return get_height(node.leftnode) - get_height(node.rightnode)

def print_tree(node, level=0):
    if node is not None:
        print_tree(node.rightnode, level + 1)
        bf = get_balance(node)
        print('    ' * level + f"Key: {node.key} | Altura: {node.h} | BF: {bf}")
        print_tree(node.leftnode, level + 1)


#RotateLeft
#Entrada: Recibe un AVL Tree y un AVL node sobre el cual se va a operar la rotación a la izquierda
#Salida: Devuelve la nueva raíz del AVL node

"""El hijo derecho de la raíz, pasará a ser la nueva raíz, la raíz anterior será el hijo izquierdo, y si la raíz nueva tenia un hijo izquierdo pasara a ser hijo derecho de la raiz vieja
si tenía unn hijo derecho, continuará siendo su hijo derecho"""

def rotateLeft(tree, node):
    new_root = node.rightnode
    node.rightnode = new_root.leftnode
    
    if new_root.leftnode is not None:
        new_root.leftnode.parent = node
    new_root.parent = node.parent

    if node.parent is None:
        tree.root = new_root
    elif node == node.parent.leftnode:
        node.parent.leftnode = new_root
    else:
        node.parent.rightnode = new_root

    new_root.leftnode = node
    node.parent = new_root

    updateHandBF(node)
    updateHandBF(new_root)

    return new_root

#RotateRight
#Entrada: Recibe un AVL Tree y un AVL node sobre el cual se va a operar la rotación a la derecha
#Salida: Devuelve la nueva raíz del AVL node

def rotateRight(tree, node):
    new_root = node.leftnode
    node.leftnode = new_root.rightnode

    if new_root.rightnode is not None:
        new_root.rightnode.parent = node
    new_root.parent = node.parent

    if node.parent is None:
        tree.root = new_root
    elif node == node.parent.rightnode:
        node.parent.rightnode = new_root
    else:
        node.parent.leftnode = new_root

    new_root.rightnode = node
    node.parent = new_root

    updateHandBF(node)
    updateHandBF(new_root)

    return new_root

#UpdateHandBF
#Entrada: Recibe un AVL node al cual se le actualizará la altura y el balance factor
#Salida: No devuelve nada en especifico

def updateHandBF(node):
    if node is None:
        return
    
    if node.leftnode is not None:
        lefth = node.leftnode.h
    else:
        lefth =  -1
    
    if node.rightnode is not None:
        righth = node.rightnode.h
    else:
        righth = -1
    
    node.h = max(lefth, righth) + 1
    node.bf = lefth-righth

#CalculateBalance
#Entrada: Recibe un AVL tree
#Salida: Devuelve el AVL tree con los valores de balancefactor de cada subárbol

def calculateBalance(tree):
    if tree is None:
        return -1
    calculateBalanceR(tree.root)
    return tree

def calculateBalanceR(node):
    if node is None:
        return -1
    
    h_izq = calculateBalanceR(node.leftnode)
    h_der = calculateBalanceR(node.rightnode)
    node.h = max(h_izq, h_der) + 1
    node.bf = h_izq-h_der
    return node.h
    

#Rebalance
#Entrada: Recibe un AVL tree
#Salida: Devuelve el AVL tree balanceado

def rebalance(tree):
    if tree.root is None:
        return tree
    
    updateHandBF(tree.root)
    bf = tree.root.bf

    if bf > 1:
        if tree.root.leftnode >= 0:
            tree.root = rotateRight(tree, tree.root)
        else:
            tree.root.leftnode = rotateLeft(tree, tree.root.leftnode)
            tree.root = rotateRight(tree, tree.root)

    elif bf < -1:
        if tree.root.rightnode >= 0:
            tree.root = rotateLeft(tree, tree.root)
        else:
            tree.root.rightnode = rotateRight(tree, tree.root.rightnode)
            tree.root = rotateLeft(tree, tree.root)

    return tree





#Prueba................
# Crear árbol y nodos
tree = AVLTree()

# Crear nodos
n1 = AVLNode()
n1.key = 10
n1.value = "A"

n2 = AVLNode()
n2.key = 5
n2.value = "B"
n2.parent = n1
n1.leftnode = n2

n3 = AVLNode()
n3.key = 15
n3.value = "C"
n3.parent = n1
n1.rightnode = n3

n4 = AVLNode()
n4.key = 3
n4.value = "D"
n4.parent = n2
n2.leftnode = n4

n5 = AVLNode()
n5.key = 7
n5.value = "E"
n5.parent = n2
n2.rightnode = n5

# Asignar raíz
tree.root = n1
    
calculateBalance(tree)
print_tree(tree.root)












