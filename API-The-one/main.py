from access.request import make_request


def print_test(address, id_code=''):
    requested = make_request(address, id_code)

    dictionary_test = requested[0]
    print(dictionary_test)

    for i in dictionary_test:
        if i == 'docs':
            print(i)
            for j in dictionary_test[i]:
                print(j)
        else:
            print(i)
            print(dictionary_test[i])


print_test('all movies')
