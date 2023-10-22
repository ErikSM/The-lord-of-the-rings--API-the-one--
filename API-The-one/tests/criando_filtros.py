from access.request import make_request


def races_of_characters(request, code_id=''):
    request = make_request(request, code_id)
    # all races of characters
    races = set()
    for i in request['docs']:
        for j in i:
            if j == 'race':
                races.add(i[j])

    print(f'\n\n((races)) total:{len(races)}')
    print('-' * 30)
    for i in races:
        print(i)


def realms_founded(request, code_id=''):
    request = make_request(request, code_id)
    # all realms
    realms = set()
    for i in request['docs']:
        for j in i:
            if j == 'realm':
                realms.add(i[j])

    print(f'\n\n((realms)) total:{len(realms)}')
    print('-' * 30)
    for i in realms:
        print(i)


races_of_characters('all characters')
realms_founded('all characters')
