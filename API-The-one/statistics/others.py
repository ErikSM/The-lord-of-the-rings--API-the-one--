from access.request import make_request


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

    return total_amount
