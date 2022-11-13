class Node:
    __data: str

    def __init__(self, data: str):
        self.__data = data

    def __str__(self) -> str:
        return self.__data
