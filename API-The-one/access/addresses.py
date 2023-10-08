

def create_endpoints(id_research=''):
    endpoints = dict()
    endpoints['research id'] = id_research

    endpoints['all books'] = ('/book',
                              'List of all "The Lord of the Rings" books',
                              False)
    endpoints['specific book'] = (f'/book/{endpoints["research id"]}', 'Request one specific book', True)
    endpoints['chapters of specific book'] = (f'/book/{endpoints["research id"]}/chapter',
                                              'Request all chapters of one specific book',
                                              True)

    endpoints['all movies'] = ('/movie',
                               'List of all movies, including the "The Lord of the Rings" and the "The Hobbit" '
                               'trilogies',
                               False)
    endpoints['specific movie'] = (f'movie/{endpoints["research id"]}', 'Request one specific movie', True)
    endpoints['quotes of movie'] = (f'/movie/{endpoints["research id"]}/quote',
                                    'Request all movie quotes for one specific movie (only working for the LotR trilogy'
                                    , True)

    endpoints['all characters'] = ('/character',
                                   'List of characters including metadata like name, gender, realm, race and more',
                                   False)
    endpoints['specific character'] = (f'/character/{endpoints["research id"]}', 'Request one specific character', True)
    endpoints['quotes of character'] = (f'/character/{endpoints["research id"]}/quote',
                                        'Request all movie quotes of one specific character',
                                        True)

    endpoints['movies quotes'] = ('/quote', 'List of all movie quotes', False)
    endpoints['specific movie quote'] = (f'/quote/{endpoints["research id"]}', 'Request one specific movie quote', True)

    endpoints['books chapters'] = ('/chapter', 'List of all book chapters', False)
    endpoints['specific book chapter'] = (f'/chapter/{endpoints["research id"]}', 'Request one specific book chapter',
                                          True)

    return endpoints

