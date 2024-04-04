def inserir_item(lista):
    novo_item = input("Digite o novo item: ")
    lista.append(novo_item)
    print("Item inserido com sucesso!")

def excluir_item(lista):
    item_a_excluir = input("Digite o item a excluir: ")
    if item_a_excluir in lista:
        lista.remove(item_a_excluir)
        print("Item excluído com sucesso!")
    else:
        print("O item não está na lista.")

def mostrar_lista(lista):
    print("Lista atual:", lista)
    
def gravar_lista(lista):
    gravar_arq = input("Digite o nome do arquivo")
    with open(gravar_arq,"w") as arquivo:
        for item in lista:
            arquivo.write(item + "\n")
    print("GRAVADO",gravar_arq)        

def main():
    lista = []
    menu = {
        '1': inserir_item,
        '2': excluir_item,
        '3': mostrar_lista,
        '4': gravar_lista,
        '5': lambda _: print("Programa encerrado.") 
    }
    
    while True:
        print("\n1. Inserir novo item na lista")
        print("2. Excluir item da lista")
        print("3. Mostrar lista atual")
        print("4. gravar lista")
        print("5. Sair")
        
        escolha = input("\nEscolha uma opção: ")
        
        if escolha in menu:
            menu[escolha](lista)
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
