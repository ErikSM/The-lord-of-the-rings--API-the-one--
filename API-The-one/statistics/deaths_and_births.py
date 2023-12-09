from access.request import make_request


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

    return total_amount


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

    return total_amount
