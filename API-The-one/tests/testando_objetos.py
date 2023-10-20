from access.request import make_request
from objects.Book import Book
from objects.Chapter import Chapter
from objects.Character import Character
from objects.Movie import Movie
from objects.Quote import Quote

"""character = Character('5cd99d4bde30eff6ebccfbbf')
print(character.personal_details())

movie = Movie('5cd95395de30eff6ebccde5b')
print(movie.all_quotes())
quote = Quote('5cd96e05de30eff6ebcce9b8')
print(quote.dialog)

book = Book('5cf5805fb53e011a64671582')
print(book.all_chapters)
chapter = Chapter('6091b6d6d58360f988133b8b')
print(chapter.name)"""


def requesting_test(request, code_id):
    request = make_request(request, code_id)
    for i in request:
        print(f'({i})')
        print(request[i])


requesting_test('quotes of movie', '5cd95395de30eff6ebccde5b')
