endpoints = dict()


def create_endpoints(id_research=''):
    endpoints['research id'] = id_research

    endpoints['all books'] = ('/book', 'List of all "The Lord of the Rings" books',
                              True, ['about book', 'chapters of book'])
    endpoints['about book'] = (f'/book/{endpoints["research id"]}', 'Request one specific book',
                               False)
    endpoints['chapters of book'] = (f'/book/{endpoints["research id"]}/chapter', 'Request all chapters of one '
                                                                                  'specific book',
                                     False)

    endpoints['all movies'] = ('/movie', 'List of all movies, including the "The Lord of the Rings" and the "The '
                                         'Hobbit" trilogies',
                               True, ['about movie', 'quotes of movie'])
    endpoints['about movie'] = (f'/movie/{endpoints["research id"]}', 'Request one specific movie',
                                False)
    endpoints['quotes of movie'] = (f'/movie/{endpoints["research id"]}/quote', 'Request all movie quotes for one '
                                                                                'specific movie (only working for the '
                                                                                'LotR trilogy '
                                    , False)

    endpoints['all characters'] = ('/character', 'List of characters including metadata like name, gender, realm, '
                                                 'race and more',
                                   True, ['about character', 'quotes of character'])
    endpoints['about character'] = (f'/character/{endpoints["research id"]}', 'Request one specific character',
                                    False)
    endpoints['quotes of character'] = (f'/character/{endpoints["research id"]}/quote', 'Request all movie quotes of '
                                                                                        'one specific character',
                                        False)

    endpoints['movies quotes'] = ('/quote', 'List of all movie quotes',
                                  True, ['about quote'])
    endpoints['about quote'] = (f'/quote/{endpoints["research id"]}', 'Request one specific movie quote',
                                False)

    endpoints['books chapters'] = ('/chapter', 'List of all book chapters',
                                   True, ['about chapter'])
    endpoints['about chapter'] = (f'/chapter/{endpoints["research id"]}', 'Request one specific book chapter',
                                  False)

    return endpoints
