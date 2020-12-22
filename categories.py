from marketplaces import Marketplace


class Category:
    __id: int
    __name: str
    __mkp: int
    __father: int

    def __init__(self, name, mkp, id):
        self.__name = name
        self.__mkp = mkp
        self.__id = id
        self.__father = 0

    def set_father(self, father):
        self.__father = father
    
    def __str__(self):
        if(self.__father == 0):
            return f'{self.__id}: {self.__name}'
        else:
            return f'{self.__id}: {self.__name} >> {self.__father}'

    def is_mkp(self, mkp) -> bool:
        return self.__mkp == mkp

    def is_son(self, father) -> bool:
        return self.__father == father


 
