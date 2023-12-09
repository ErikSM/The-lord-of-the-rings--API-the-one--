from access.request import make_request


movies_numbers_list = ["runtimeInMinutes", "budgetInMillions",
                       "boxOfficeRevenueInMillions", "academyAwardNominations",
                       "academyAwardWins", "rottenTomatoesScore"]


def organize_movies_dict():
    all_movies = make_request('all movies')

    movies_dict = dict()
    premium_dictionary = dict()

    for i in all_movies['docs']:
        data_list = list()
        for j in i:
            if not j == 'name' and not j == '_id':
                info = j, i[j]
                data_list.append(info)
                premium_dictionary[j] = list()
        movies_dict[i['name']] = data_list

    for i in movies_dict:
        for j in movies_dict[i]:
            premium_dictionary[j[0]].append((int(j[1]), i))

    return premium_dictionary
