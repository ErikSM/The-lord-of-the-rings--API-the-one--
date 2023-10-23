from access.request import make_request


def requesting_test(request, code_id=''):
    request = make_request(request, code_id)
    for i in request:
        if i == 'docs':
            print(f'({i}')
            for j in request[i]:
                print(j)
        else:
            print(f'({i})')
            print(request[i])


# requesting_test('quotes of movie', '5cd95395de30eff6ebccde5b')
requesting_test('all books')

