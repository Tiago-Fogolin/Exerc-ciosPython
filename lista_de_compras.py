
print("-"*5,"Lista de Compras","-"*5)
print("Comandos:")
print("1: Ver lista")
print("2: Adicionar item")
print("3: Remover item")
print("4: Parar aplicação")

lista = []

while True:
    comando = input("Digite seu comando: ")
    try:
        comando = int(comando)
        if comando == 1:
            print("Lista de Compras: ")
            for z in lista:
                print(f"[X] {z}")

        elif comando == 2:
            item = input("Adicione seu item: ").split()
            for i in item:
                if i.capitalize() not in lista:
                    lista.append(i.capitalize())
                else:
                    print(f"{i} já adicionado à lista")
    
        elif comando == 3:
            item_remover = input("Item a ser removido: ").split()
            for x in item_remover:
                if x.capitalize() in lista:
                    lista.remove(x.capitalize())

        elif comando == 4:
            break

        else:
            print("Comando inválido")    
    except:
        print("Comando inválido")
    
   
