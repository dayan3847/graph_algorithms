from tinmarin import TinMarin


def run_tin_marin():
    phrases_count: int = 3
    people_count: int = 10
    tin_marin = TinMarin(phrases_count, people_count)

    fist_team_size: int = int(people_count / 2)
    for i in range(0, fist_team_size):
        i_person = tin_marin.select_next_person()
        print(i_person)


if __name__ == '__main__':
    run_tin_marin()
