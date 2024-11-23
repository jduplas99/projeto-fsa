lista = []
try:
    while True:
        item = input("Digite (a) para adicionar algo à lista, (m) para mostrar a lista, (r) para remover e (s) para sair: ").lower()
        
        if item not in ['a', 'm', 'r', 's']:
            print('Letra não conhecida!')
            continue

        if item == 'a':
            item_adicionar = input("Digite algo para adicionar na lista: ").lower()
            lista.append(item_adicionar)
        elif item == 'r':
            item_remover = input('Digite o que deseja remover da lista: ')
            if item_remover in lista:
                lista.remove(item_remover)
            else:
                print(f'{item_remover} não está na lista.')
        elif item == 'm':
            print("Lista atual:")
            for i, elem in enumerate(lista, start=1):
                print(f"{i}: {elem}")
        elif item == 's':
            print(f'Você encerrou o programa. Sua lista:')
            for i, elem in enumerate(lista, start=1):
                print(f"{i}: {elem}")
            break
except Exception as e:
    print(f'Você digitou algo errado. Reinicie o programa. Erro: {e}')
