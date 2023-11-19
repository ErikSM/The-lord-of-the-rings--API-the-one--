from access.request import make_request
from apps.graphic import make_bar_graphic


# --------  RACES and REALMS  ---------------

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

    make_bar_graphic(total_amount['races'], 'Races')


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

    make_bar_graphic(total_amount['realms'], 'Realms')


#  -------------   DEATH and BIRTH  ------------
YT = "Years of the Trees"
FA = "The First Age"
SA = "Second Age"
TA = "Third Age"
FO = "Fourth Age"
SR = "The Shire Reckoning was the calendar kept by the hobbits " \
     "of the Shire, very close to the King's Reckoning"
ages_string = [YT, FA, SA, TA, SR, FO]


def time_of_death(request, code_id=''):
    request = make_request(request, code_id)

    total_amount = dict()
    death = list()
    ages = set()

    for i in request['docs']:
        for j in i:
            if j == 'death':
                death.append(i[j])

    for i in death:
        if i[2:3] == ' ':
            ages.add(i[:2])

    frequency_of_death = {i: list() for i in ages}

    for i in death:
        if i[:2] in ages:
            frequency_of_death[i[:2]].append(i)

    total_amount['death'] = [(len(frequency_of_death[i]), i) for i in frequency_of_death]

    print(f'\n\n((death)) total:{len(death)}')
    print('-' * 30)
    for i in death:
        if i != '' and i != 'NaN':
            print(i)
    print(":::::::::::::::::::::")
    for i in frequency_of_death:
        print(f'{i}({len(frequency_of_death[i])}): {frequency_of_death[i]}')
    print('\n')
    print(total_amount)

    make_bar_graphic(total_amount['death'], 'Deaths')


def time_of_birth(request, code_id=''):
    request = make_request(request, code_id)

    birth = set()
    ages = set()
    total_amount = dict()

    for i in request['docs']:
        for j in i:
            if j == 'birth':
                birth.add(i[j])

    for i in birth:
        if i[2:3] == ' ':
            if i[:2] == 'c.' or i[:2] == 'b.' or i[:2] == '22':
                ages.add('TA')
            else:
                ages.add(i[:2])

    frequency_of_birth = {i: list() for i in ages}

    for i in birth:
        if i[:2] in ages:
            if i[:2] == 'c.':
                frequency_of_birth['TA'].append(i)
            elif i[:2] == 'b.':
                frequency_of_birth['TA'].append(i)
            elif i[:2] == '22':
                frequency_of_birth['TA'].append(i)
            else:
                frequency_of_birth[i[:2]].append(i)

    total_amount['birth'] = [(len(frequency_of_birth[i]), i) for i in frequency_of_birth]

    print(f'\n\n((birth)) total:{len(birth)}')
    print('-' * 30)
    for i in birth:
        if i != '' and i != 'NaN':
            print(i)
    print(":::::::::::::::::::::")
    for i in frequency_of_birth:
        print(f'{i}({len(frequency_of_birth[i])}): {frequency_of_birth[i]}')
    print('\n')
    print(total_amount)

    make_bar_graphic(total_amount['birth'], 'Births')


#  ----------------  GENDERS  ----------------

def genders_data(request, code_id=''):
    request = make_request(request, code_id)

    total_amount = dict()
    genders = set()
    female, male, others = list(), list(), list()

    total = 0
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

    total_amount['genders'] = [(len(female), 'Female'), (len(male), 'Male'), (len(others), 'Others')]

    print(f'\n\n((gender)) total:{total}')
    print('-' * 30)
    print(f'total famale = {len(female)}')
    print(f'total male = {len(male)}')
    print(f'Undefined: {len(others)}')
    print('-' * 30)
    for i in genders:
        print(i)
    print('::::::::::::::::::')
    print(total_amount)

    make_bar_graphic(total_amount['genders'], 'Genders')


races_of_characters('all characters')
realms_founded('all characters')

time_of_death('all characters')
time_of_birth('all characters')

genders_data('all characters')
