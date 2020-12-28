from marketplaces import Marketplace
from categories import Category

def read_marketplaces(nome:str)->list:
    lista = []
    arquivo = open(nome, 'r')
    for linha in arquivo:
        linha.strip("\n")
        lista.append(Marketplace(linha, len(lista)+1))
    arquivo.close()
    return lista

def read_categories(nome:str)->list:
    lista = []
    cont = 1
    arquivo = open(nome, 'r')
    for linha in arquivo:
        linha = linha.strip("\n")
        linha = linha.split(";")
        cat = Category(linha[2],int(linha[1]),cont,int(linha[0]))
        cont += 1
        lista.append(cat)
    arquivo.close()
    return lista

mkp_list = read_marketplaces('marketplaces/entradas/marketplaces.txt')

cat_list = read_categories('marketplaces/entradas/categorias.txt')

def print_list(one_list):
    for one in one_list:
        print(str(one))

def fill_categories() -> list:

    cat_list = list()
    i = 1

    for key in cat_names:
        temp = cat_names[key]

        for t in temp:
            cat_list.append(Category(t, key, i))
            i += 1

    return cat_list

def fill_subcategories() -> list:

    subcat_list = list()
    i = 1

    for key in subcat_names:
        subcat = subcat_names[key]
        cat = Category(subcat, 0, i)
        cat.set_father(int(key))
        print(cat)
        subcat_list.append(cat)
        i += 1

    return subcat_list



def show_menu() -> int:

    option = input(
                    '''
                    What do you want to do?
                    1 - List Marketplaces
                    2 - List Categories by Marketplace
                    3 - List Subcategories by Categories
                    0 - Ends
                    '''
                )

    return option

def print_cat_by_mkp(cat_list, mkp) -> list:

    lista = []
    for cat in cat_list:
        if cat.is_mkp(mkp):
            lista.append(cat)
    
    return lista

def print_subcat_by_cat(subcat_list, cat) -> list:
    lista = []

    for subcat in subcat_list:
        if subcat.is_son(cat):
            lista.append(subcat)
    
    return lista

def only_cats(cat_list) -> list:
    lista = []
    for cat in cat_list:
        if cat.is_cat():
            lista.append(cat)
    return lista

if __name__ == '__main__':

    option = -1

    while(option != 0):
        option = int(show_menu())

        if option == 1: 
            print_list(mkp_list)
        elif option == 2:
            print("Choose a marketplace id")
            print_list(mkp_list)
            mkp_id = int(input())
            lista = print_cat_by_mkp(cat_list, mkp_id)
            print_list(lista)

        elif option == 3:
            print("Choose a category id")
            print_list(only_cats(cat_list))
            cat_id = int(input())
            lista = print_subcat_by_cat(cat_list, cat_id)
            print_list(lista)
        elif option == 0:
            print("See you soon!")
            exit()
        else:
            print("Invalid option!")