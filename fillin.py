from marketplaces import Marketplace
from categories import Category

mkp_names = ('Submarino', 'Americanas', 'Mercado Livre')

cat_names = {
                1: ["Smartphones", "Livros", "Informática"],
                2: ["Utilidades Domésticas", "Infantil", "Cama, Mesa e Banho"],
                3: ["Animais", "Vestuário", "Ferramentas"]
            }

subcat_names = {
                "1": "Dual Chip", 
                "2": "Policial",
                "3": "Notebooks"
            }


def fill_marketplaces(mkp_names) -> list:

    mkp_list = list()

    for mkp in mkp_names:
        mkp_list.append(Marketplace(mkp, len(mkp_list)+1))

    return mkp_list


def print_list(one_list):
    for one in one_list:
        print(str(one))

def fill_categories(cat_names) -> list:

    cat_list = list()
    i = 1

    for key in cat_names:
        temp = cat_names[key]

        for t in temp:
            cat_list.append(Category(t, key, i))
            i += 1

    return cat_list

def fill_subcategories(subcat_names) -> list:

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

def print_cat_by_mkp(cat_list, mkp):

    for cat in cat_list:
        if cat.is_mkp(mkp):
            print(cat)

def print_subcat_by_cat(subcat_list, cat):

    for subcat in subcat_list:
        if subcat.is_son(cat):
            print(subcat)


if __name__ == '__main__':
    mkp_list = fill_marketplaces(mkp_names)
    cat_list = fill_categories(cat_names)
    subcat_list = fill_subcategories(subcat_names)
    option = -1

    while(option != 0):
        option = int(show_menu())

        if option == 1: 
            print_list(mkp_list)
        elif option == 2:
            print("Choose a marketplace id")
            print_list(mkp_list)
            mkp_id = int(input())
            print_cat_by_mkp(cat_list, mkp_id)
        elif option == 3:
            print("Choose a category id")
            print_list(cat_list)
            cat_id = int(input())
            print_subcat_by_cat(subcat_list, cat_id)
        elif option == 0:
            print("See you soon!")
            exit()
        else:
            print("Invalid option!")

