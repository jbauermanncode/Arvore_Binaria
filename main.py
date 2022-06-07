from arvore_binaria import Arvore

arvore = Arvore()

tipo_ordem = [arvore.pre_ordem, arvore.em_ordem, arvore.pos_ordem]
ordem = tipo_ordem[int(input('Escolha a ordem que você deseja imprimir a árvore: \nPré Ordem [0]\nEm Ordem  [1]\nPós Ordem [2]:'))]

if (ordem == arvore.pre_ordem):
    ordem_escolhida = 'Pré Ordem'
elif (ordem == arvore.em_ordem):
    ordem_escolhida = 'Ordem'
elif (ordem == arvore.pos_ordem):
    ordem_escolhida = 'Pós Ordem'

print(f'Imprime a árvore em {ordem_escolhida}')

arvore.inserir(8)
ordem(arvore._raiz)
print('--'*20+'\n')
arvore.inserir(5)
ordem(arvore._raiz)
print('--'*20+'\n')
arvore.inserir(1)
ordem(arvore._raiz)
print('--'*20+'\n')
arvore.inserir(7)
ordem(arvore._raiz)
print('--'*20+'\n')
arvore.inserir(15)
ordem(arvore._raiz)
print('--'*20+'\n')
arvore.inserir(12)
ordem(arvore._raiz)
print('--'*20+'\n')
arvore.inserir(18)
ordem(arvore._raiz)
print('--'*20+'\n')

print(f'Imprime a árvore em {ordem_escolhida}')
ordem(arvore.get_raiz())
print('--'*20+'\n')
buscar = input('Deseja fazer busca de elemento?(S/N) ')
while(buscar == 'S'): 
    print('--'*20+'\n')
    arvore.buscar(int(input('Buscar chave: ')))
    print('--'*20+'\n')
    print(f'Imprime a árvore em {ordem_escolhida}')
    ordem(arvore.get_raiz())
    print('--'*20+'\n')
    buscar = input('Deseja fazer busca por nova chave?(S/N) ')
else:
    print('--'*20+'\n')
    print(f'Imprime a árvore em {ordem_escolhida}')
    ordem(arvore.get_raiz())

print('--'*5+'FIM!'+'--'*5)