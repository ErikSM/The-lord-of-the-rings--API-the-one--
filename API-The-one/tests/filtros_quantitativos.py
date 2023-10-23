from access.request import make_request


def analyzing_dictionary(request, code_id=''):
    request = make_request(request, code_id)
    keys = set()
    for i in request['docs']:
        for j in i:
            keys.add(j)

    for i in keys:
        print(i)


analyzing_dictionary('all movies')

