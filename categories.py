from marketplaces import Marketplace


class Category:
    __id: int
    __name: str
    __mkp: int
    __father: int

    def __init__(self, name, mkp, id, father):
        self.__name = name
        self.__mkp = mkp
        self.__id = id
        self.__father = father

    def set_father(self, father):
        self.__father = father

    def get_name(self):
        return self.__name
    
    def __str__(self):
        if(self.__father == 0):
            return f'{self.__id}: {self.__name} ({self.__mkp})'
        else:
            return f'{self.__id}: {self.__name} >> {self.__father}'

    def is_mkp(self, mkp) -> bool:
        return self.__mkp == mkp

    def is_son(self, father) -> bool:
        return self.__father == father

    def is_cat(self) -> bool:
        if self.__father == 0:
            return True
        else:
            return False

 
