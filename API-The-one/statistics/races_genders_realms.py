from access.request import make_request


statistic_list = ['realms', 'race', 'genders']


def race_of_characters():
    request = make_request('all characters')

    total_amount = {'race': list()}
    race_characters = dict()
    races = set()

    for i in request['docs']:
        for j in i:
            if j == 'race':
                races.add(i[j])
                race_characters[i[j]] = list()

    for i in request['docs']:
        race_characters[i['race']].append(i)

    for i in race_characters:
        number, name = len(race_characters[i]), i
        if name == '':
            name = 'undefined'
        total_amount['race'].append((int(number), name))

    return total_amount


def realms_founded():
    request = make_request('all characters')

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
        if name == '' or name == 'NaN' or name == 'TA 2':
            name = 'Undefined[x20]'
            number += number
            total_amount['realms'].append((int(number) / 20, name))
        else:
            total_amount['realms'].append((int(number), name))

    return total_amount


def genders_data():
    request = make_request('all characters')

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

    return total_amount
