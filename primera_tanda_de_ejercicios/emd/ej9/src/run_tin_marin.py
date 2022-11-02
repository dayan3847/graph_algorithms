from tinmarin import TinMarin


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
