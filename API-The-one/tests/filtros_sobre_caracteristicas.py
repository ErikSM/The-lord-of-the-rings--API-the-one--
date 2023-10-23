from access.request import make_request


def races_of_characters(request, code_id=''):
    request = make_request(request, code_id)
    races = set()
    for i in request['docs']:
        for j in i:
            if j == 'race':
                races.add(i[j])

    print(f'\n\n((races)) total:{len(races)}')
    print('-' * 30)
    for i in races:
        print(i)


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


def realms_founded(request, code_id=''):
    request = make_request(request, code_id)
    realms = set()
    for i in request['docs']:
        for j in i:
            if j == 'realm':
                realms.add(i[j])

    print(f'\n\n((realms)) total:{len(realms)}')
    print('-' * 30)
    for i in realms:
        print(i)


def genders_data(request, code_id=''):
    request = make_request(request, code_id)
    total = 0
    female = list()
    male = list()
    others = list()
    genders = set()
    for i in request['docs']:
        total += 1

        for j in i:
            if j == 'gender':
                genders.add(i[j])
                if i[j] == 'Male':
                    male.append(i[j])
                elif i[j] == 'Female':
                    female.append(i[j])
                else:
                    others.append(i[j])

    print(f'\n\n((gender)) total:{total}')
    print('-' * 30)
    print(f'total famale = {len(female)}')
    print(f'total male = {len(male)}')
    print(f'others: {len(others)}')
    print('-' * 30)
    for i in genders:
        print(i)


'''races_of_characters('all characters')
realms_founded('all characters')
time_of_death('all characters')
time_of_birth('all characters')'''
genders_data('all characters')
