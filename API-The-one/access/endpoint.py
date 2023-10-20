endpoints = dict()


def create_endpoints(id_research=''):
    endpoints['research id'] = id_research

    endpoints['all books'] = ('/book', True)
    endpoints['about book'] = (f'/book/{endpoints["research id"]}', False)
    endpoints['chapters of book'] = (f'/book/{endpoints["research id"]}/chapter', False)

    endpoints['all movies'] = ('/movie', True)
    endpoints['about movie'] = (f'/movie/{endpoints["research id"]}', False)
    endpoints['quotes of movie'] = (f'/movie/{endpoints["research id"]}/quote', False)

    endpoints['all characters'] = ('/character', True)
    endpoints['about character'] = (f'/character/{endpoints["research id"]}', False)
    endpoints['quotes of character'] = (f'/character/{endpoints["research id"]}/quote', False)

    endpoints['all quotes'] = ('/quote', True)
    endpoints['about quote'] = (f'/quote/{endpoints["research id"]}', False)

    endpoints['all chapters'] = ('/chapter', True)
    endpoints['about chapter'] = (f'/chapter/{endpoints["research id"]}', False)

    return endpoints
