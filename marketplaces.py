class Marketplace:
    __id: int
    __name:  str
    __categories: list
    __subcategories: list

    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def __str__(self):
        return f'{self.__id}: {self.__name}'

    