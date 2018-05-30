#!/usr/bin/env python3
import os
import sys


class Node:
    def __init__(self, value):
        self.value = value; #la valeur du noeud
        self.isRoot = False; #détermine si le noeud est racine. 
        self.parent = None #le noued parent de ce noeud
        self.rightChild = None
        self.leftChild = None

class BinarySearchTree:
    
    def __init__(self, rootNode):
        self.rootNode = rootNode
        
    def addNode(self, node):
        tampon = self.rootNode
        if self.rootNode.value < node.value:
            if not self.rootNode.rightChild is None:
                self.rootNode = self.rootNode.rightChild
                self.addNode(node)
        elif self.rootNode.value > node.value:
            if not self.rootNode.leftChild is None:
                self.rootNode = self.leftChild
                self.addNode(node)            
        
        self.rootNode = tampon
    
    def deleteNode(node):
        pass
    
    def search(node):
       pass #BOUCHON
   
    

if __name__ == "__main__":
    
    main()
    
    def main():
        valeur = int(input("Valeur de la racine : "))
        rootNode = Node(valeur)
        rootNode.isRoot = True
        rootNode.parent = None
        tree = BinarySearchTree(rootNode)
        
        #ajout:
        valeur = int(input("Valeur du noeud : "))
        tree.addNode(Node(valeur))
                
        
           
    
        
    
    