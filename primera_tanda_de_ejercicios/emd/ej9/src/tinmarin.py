from typing import List


class TinMarin:

    __last_select_person_index: int

    __phrases_count: int

    __people_circle: List[str]

    def __init__(self, phrases_count: int, people_count: int):
        self.__last_select_person_index = 0
        self.__phrases_count = phrases_count
        self.__people_circle = []
        for i in range(1, people_count + 1):
            self.__people_circle.append(f'Person_{i}')

    def select_next_person(self) -> str:
        people_count: int = len(self.__people_circle)
        next_person_index = self.__last_select_person_index + self.__phrases_count - 1
        next_person_index_mod = next_person_index % people_count
        # if you continue with the next one that was selected
        # self.__last_select_person_index = next_person_index_mod
        # if you continue by the one before the one that was selected
        self.__last_select_person_index = (next_person_index_mod - 1) % people_count
        return self.__people_circle.pop(next_person_index_mod)
