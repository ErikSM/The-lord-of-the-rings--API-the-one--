from access.request import make_request
from apps.graphic import make_bar_graphic
from objects.Character import Character
from objects.Movie import Movie


def requesting_test(request, code_id=''):
    request = make_request(request, code_id)
    for i in request:
        if i == 'docs':
            print(f'({i})')
            for j in request[i]:
                print(j)
        else:
            print(f'({i})')
            print(request[i])


# requesting_test('quotes of movie', '5cd95395de30eff6ebccde5b')
# requesting_test('all movies')

def characters_with_most_quotes_per_movie():
    movies_request = make_request('all movies')

    movies_dict = dict()
    for i in movies_request['docs']:
        movies_dict[i['_id']] = list()

    for i in movies_dict:
        request = make_request('quotes of movie', i)
        for j in request['docs']:
            quote, character = j['_id'], j['character']
            info_tuple = (quote, character)
            movies_dict[i].append(info_tuple)

        # width = len(request['docs'])
        # print(Movie(i))
        # print(width)

    print('============================')

    cont = 1
    total_dict = dict()
    for i in movies_dict:
        total_dict[i] = dict()
        characters = set()
        for j in movies_dict[i]:
            if j[1] in characters:
                cont += 1
            else:
                characters.add(j[1])
            total_dict[i][j[1]] = cont

    total_amount = dict()
    for i in total_dict:
        has_dict = len(total_dict[i])
        if not has_dict == 0:
            total_amount[i] = list()
            for j in total_dict[i]:
                total_amount[i].append((total_dict[i][j], j))

    for i in total_dict:
        print(len(total_dict[i]))
    print('\n==========------')

    for i in total_amount:
        make_bar_graphic(total_amount[i], f'Movie: {Movie(i)}')


# characters_with_most_quotes_per_movie()

teste = make_request('all characters')
for i in teste['docs']:
    print(i)

