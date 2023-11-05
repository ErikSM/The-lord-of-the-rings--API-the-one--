from access.request import make_request
from apps.graphic import make_bar_graphic


def races_of_characters(request, code_id=''):
    request = make_request(request, code_id)

    total_amount = {'races': list()}
    races_characters = dict()
    races = set()

    for i in request['docs']:
        for j in i:
            if j == 'race':
                races.add(i[j])
                races_characters[i[j]] = list()

    for i in request['docs']:
        races_characters[i['race']].append(i)

    for i in races_characters:
        number, name = len(races_characters[i]), i
        if name == '':
            name = 'undefined'
        total_amount['races'].append((int(number), name))

    print(f'\n\n((races)) total:{len(races)}')
    print('-' * 30)
    for i in races:
        print(i)
    print(f'\n\ntotal for each: {len(races_characters)}')
    print('-' * 30)
    print(total_amount)

    make_bar_graphic(total_amount['races'])


def realms_founded(request, code_id=''):
    request = make_request(request, code_id)

    total_amount = {'realms': list()}
    characters_realms = dict()
    realms = set()

    for i in request['docs']:
        for j in i:
            if j == 'realm':
                realms.add(i[j])
                characters_realms[i[j]] = list()

    for i in request['docs']:
        if i['realm'] in characters_realms:
            characters_realms[i['realm']].append(i['name'])

    for i in characters_realms:
        number, name = len(characters_realms[i]), i
        if name == '':
            name = 'undefined'
        total_amount['realms'].append((int(number), name))

    print(f'\n\n((realms)) total:{len(realms)}')
    print('-' * 30)
    for i in realms:
        print(i)
    print(f'\n\n((realms_ dict)) total:{len(characters_realms)}')
    print('-' * 30)
    print(total_amount)

    make_bar_graphic(total_amount['realms'])


def time_of_death(request, code_id=''):
    request = make_request(request, code_id)
    death = set()
    for i in request['docs']:
        for j in i:
            if j == 'death':
                death.add(i[j])

    print(f'\n\n((death)) total:{len(death)}')
    print('-' * 30)
    for i in death:
        print(i)


def time_of_birth(request, code_id=''):
    request = make_request(request, code_id)
    birth = set()
    for i in request['docs']:
        for j in i:
            if j == 'birth':
                birth.add(i[j])

    print(f'\n\n((birth)) total:{len(birth)}')
    print('-' * 30)
    for i in birth:
        print(i)


def genders_data(request, code_id=''):
    request = make_request(request, code_id)
    total = 0

    genders = set()

    female = list()
    male = list()
    others = list()

    for i in request['docs']:
        total += 1

        for j in i:
            if j == 'gender':
                genders.add(i[j])
                if i[j] in ['Male', 'male', 'Males', 'Most likely male']:
                    male.append(i[j])
                elif i[j] == 'Female':
                    female.append(i[j])
                else:
                    others.append(i[j])

    print(f'\n\n((gender)) total:{total}')
    print('-' * 30)
    print(f'total famale = {len(female)}')
    print(f'total male = {len(male)}')
    print(f'Undefined: {len(others)}')
    print('-' * 30)

    for i in genders:
        print(i)


races_of_characters('all characters')
realms_founded('all characters')

"""time_of_death('all characters')
time_of_birth('all characters')
genders_data('all characters')"""
