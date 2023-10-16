def create_endpoints(id_research=''):
    endpoints = dict()
    endpoints['research id'] = id_research

    endpoints['all books'] = ('/book',
                              'List of all "The Lord of the Rings" books',
                              False)
    endpoints['book selected'] = (f'/book/{endpoints["research id"]}', 'Request one specific book',
                                  True, 'all books')
    endpoints['chapters of book selected'] = (f'/book/{endpoints["research id"]}/chapter',
                                              'Request all chapters of one specific book',
                                              True, 'all books')

    endpoints['all movies'] = ('/movie',
                               'List of all movies, including the "The Lord of the Rings" and the "The Hobbit" '
                               'trilogies',
                               False)
    endpoints['movie selected'] = (f'movie/{endpoints["research id"]}', 'Request one specific movie',
                                   True, 'all movies')
    endpoints['quotes of movie selected'] = (f'/movie/{endpoints["research id"]}/quote',
                                             'Request all movie quotes for one specific movie (only working for the '
                                             'LotR trilogy '
                                             , True, 'all movies')

    endpoints['all characters'] = ('/character',
                                   'List of characters including metadata like name, gender, realm, race and more',
                                   False)
    endpoints['character selected'] = (f'/character/{endpoints["research id"]}', 'Request one specific character',
                                       True, 'all characters')
    endpoints['quotes of character selected'] = (f'/character/{endpoints["research id"]}/quote',
                                                 'Request all movie quotes of one specific character',
                                                 True, 'all characters')

    endpoints['movies quotes'] = ('/quote', 'List of all movie quotes',
                                  False)
    endpoints['quote selected'] = (f'/quote/{endpoints["research id"]}', 'Request one specific movie quote',
                                   True, 'movies quotes')

    endpoints['books chapters'] = ('/chapter', 'List of all book chapters',
                                   False)
    endpoints['chapter selected'] = (f'/chapter/{endpoints["research id"]}', 'Request one specific book chapter',
                                     True, 'books chapters')

    return endpoints
