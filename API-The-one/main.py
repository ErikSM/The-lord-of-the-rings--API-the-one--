from access.request import make_request
from objects.Character import Character
from objects.Movie import Movie


def print_test(address, id_code=''):
    requested = make_request(address, id_code)

    dictionary_test = requested

    return dictionary_test


teste = print_test('about character', '5cd99d4bde30eff6ebccfbbf')
personagem = Character(teste[0])
print(personagem.personal_details())

teste2 = print_test('about movie', '5cd95395de30eff6ebccde5b')
filme = Movie(teste2[0])
print(filme.tecnical_details())
