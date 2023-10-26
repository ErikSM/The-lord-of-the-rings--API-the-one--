from access.request import make_request
from apps.graphic import make_lines_graphic, make_bar_graphic


def ohter_line():
    print('\n')
    print(f'{"-" * 30}')
    print('\n')


def consulting_all_movies():
    all_movies = make_request('all movies')

    print(f'{"-" * 20}')
    for i in all_movies:
        if i == 'docs':
            print(f'({i})')
            for j in all_movies[i]:
                print(j)
        else:
            print(f'({i})')
            print(all_movies[i])


def analyzing_dictionary(request, code_id=''):
    request = make_request(request, code_id)
    keys = set()
    for i in request['docs']:
        for j in i:
            keys.add(j)

    for i in keys:
        print(i)


def organize_movies_dict(graphic_list):
    all_movies = make_request('all movies')

    movies_dict = dict()
    premium_dictonary = dict()
    for i in all_movies['docs']:
        data_list = list()
        for j in i:

            if not j == 'name' and not j == '_id':
                info = j, i[j]
                data_list.append(info)

                premium_dictonary[j] = list()

        movies_dict[i['name']] = data_list

    for i in movies_dict:
        print(f'({i})')
        print(movies_dict[i])
        for j in movies_dict[i]:
            premium_dictonary[j[0]].append((int(j[1]), i))

    ohter_line()

    for i in premium_dictonary:
        print(f'{i}')
        print(premium_dictonary[i])

        make_bar_graphic(premium_dictonary[i], i)


# analyzing_dictionary('all movies')
# consulting_all_movies()


organize_movies_dict("academyAwardWins")


lista_teste = [
    "runtimeInMinutes",
    "budgetInMillions",
    "boxOfficeRevenueInMillions",
    "academyAwardNominations",
    "academyAwardWins",
    "rottenTomatoesScore"
    ]