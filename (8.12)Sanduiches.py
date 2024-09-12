def make_sanduiche(*ingredientes):
    lista_ingredientes = [] 
    while True:
        quest = input('Deseja adicionar um ingrediente?(s/n)')
        if quest == 's':
            ingrediente = input('digite os ingredientes que deseja: ')
            lista_ingredientes.append(ingrediente)
        elif quest == 'n':
            print(f"Os ingredientes para seu sanduiche são estes:")
            for ing in lista_ingredientes:
                print(f"-{ing}")
            break
        else:
            print('Por favor digite uma resposta válida')

make_sanduiche()