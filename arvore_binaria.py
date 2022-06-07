from elemento import Elemento

class Arvore:
    
    def __init__(self):
        self._raiz = None

    def arvore_vazia(self):
        return self._raiz == None

    def inserir(self, valor):
        novoElemento = Elemento(valor)
        if (self._raiz == None):
            self._raiz = novoElemento
            print(f'Criei a arvore com o elemento {novoElemento.get_valor()}')
        else: 
            atual = self._raiz
            while(True):
                if (novoElemento.get_valor() < atual.get_valor()):
                    if(atual.get_esquerda() != None):
                        atual = atual.get_esquerda()
                       
                    else:
                        atual.set_esquerda(novoElemento)
                        print(f'Foi inserido o elemento {novoElemento.get_valor()} à esquerda de {atual.get_valor()}')
                        break
                else:
                    if (atual.get_direita() != None):
                        atual = atual.get_direita()
                        
                    else:
                        atual.set_direita(novoElemento)
                        print(f'Foi inserido o elemento {novoElemento.get_valor()} à direita de {atual.get_valor()}')
                        break

    #buscar elemento na arvore
    def buscar(self, valor):
        atual = self._raiz
        paiAtual = None

        while(atual != None):
            if(atual.get_valor() == valor):
                print(f'Chave {atual.get_valor()} Encontrada')
                self.remover(atual, paiAtual)
                break
           
            elif (valor < atual.get_valor()):
                paiAtual = atual
                atual = atual.get_esquerda()
            else:
                paiAtual = atual
                atual = atual.get_direita()
            
        else:
            print('Chave não encontrada!')
            inserir = input('Deseja inserir elemento na árvore?(S/N) ')
            if (inserir == 'S'):
                self.inserir(valor)

    #remover elemento da arvore
    def remover(self, atual, paiAtual=None):

        #pergunta se o usuario deseja a remoção da chave
        if(atual != None):
            remover = input(f'Deseja remover a chave {atual.get_valor()}?(S/N) ')
            #se a resposta for sim, remover chave 
            if remover == 'S':

                #elemento tem 2 filhos ou elemento tem somente filho a direita
                if (atual.get_direita() != None):
                    substituto = atual.get_direita()
                    paiSubstituto = atual
                    while (substituto.get_esquerda() != None):
                        paiSubstituto= substituto
                        substituto = substituto.get_esquerda()

                    substituto.set_esquerda(atual.get_esquerda())
                    
                    if (paiAtual != None):
                        if (atual.get_valor() < paiAtual.get_valor()):
                            paiAtual.set_esquerda(substituto) 
                        else:
                            paiAtual.set_direita(substituto)
                    
                    else:
                        self._raiz = substituto
                    
                    if (substituto.get_valor() < paiSubstituto.get_valor()):
                        paiSubstituto.set_esquerda(None)
                    else:
                        paiSubstituto.set_direita(None)

                
                
                #tem filho somente a esquerda
                elif (atual.get_esquerda() != None):
                    substituto = atual.get_esquerda()
                    paiSubstituto = atual
                    while (substituto.get_direita() != None):
                        paiSubstituto= substituto
                        substituto = substituto.get_direita()
                    
                    if (paiAtual != None):
                        if (atual.get_valor() < paiAtual.get_valor()):
                            paiAtual.set_esquerda(substituto) 
                        else:
                            paiAtual.set_direita(substituto)
                    else:
                        self._raiz = substituto
                    
                    if (substituto.get_valor() < paiSubstituto.get_valor()):
                        paiSubstituto.set_esquerda(None)
                    else:
                        paiSubstituto.set_direita(None)
                else: #não tem filho
                    if(paiAtual != None):
                        if (atual.get_valor() < paiAtual.get_valor()):
                            paiAtual.set_esquerda(None) 
                        else:
                            paiAtual.set_direita(None)
                    else:
                        self._raiz = None
                

    
    
    def get_raiz(self):
        return self._raiz

    def pre_ordem(self, atual):
        
        if (atual != None):
            print(atual.get_valor())
            self.pre_ordem(atual.get_esquerda())
            self.pre_ordem(atual.get_direita())

    def em_ordem(self, atual):

        if (atual != None):
            self.em_ordem(atual.get_esquerda())
            print(atual.get_valor())
            self.em_ordem(atual.get_direita())

    def pos_ordem(self, atual):

        if (atual != None):
            self.pos_ordem(atual.get_esquerda())
            self.pos_ordem(atual.get_direita())
            print(atual.get_valor())


 