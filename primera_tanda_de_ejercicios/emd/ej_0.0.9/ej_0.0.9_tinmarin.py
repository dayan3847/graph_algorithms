from typing import List


class TinMarin:
    __last_select_person_index: int

    __phrases_count: int

    people_circle: List[str]

    def __init__(self, phrases_count: int, people_count: int):
        self.__last_select_person_index = 0
        self.__phrases_count = phrases_count
        self.people_circle = []
        for i in range(1, people_count + 1):
            self.people_circle.append(f'Person_{i}')

    def select_next_person(self) -> str:
        people_count: int = len(self.people_circle)
        next_person_index = self.__last_select_person_index + self.__phrases_count - 1
        next_person_index_mod = next_person_index % people_count
        self.__last_select_person_index = next_person_index_mod
        return self.people_circle.pop(next_person_index_mod)


def run_tin_marin():
    phrases_count: int = int(input('Insert the number of phrases in the couplet: '))
    people_count: int = int(input('Insert the number of people: '))

    tin_marin = TinMarin(phrases_count, people_count)

    print('People in the circle:')
    print(tin_marin.people_circle)

    team1 = []

    fist_team_size: int = int(people_count / 2)
    for i in range(0, fist_team_size):
        i_person = tin_marin.select_next_person()
        team1.append(i_person)
    print('Team1:')
    print(team1)
    print('Team2:')
    print(tin_marin.people_circle)


if __name__ == '__main__':
    run_tin_marin()
