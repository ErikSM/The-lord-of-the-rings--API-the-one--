from objects.Book import Book
from objects.Chapter import Chapter
from objects.Character import Character
from objects.Movie import Movie
from objects.Quote import Quote


def processing_book(code_id):
    book = Book(code_id)
    book.capture_chapters()
    book.organize_information()

    return book, book.basic_info, (book.all_chapters, 'chapters')


def processing_movie(code_id):
    movie = Movie(code_id)
    movie.capture_quotes()
    movie.organize_information()

    return movie, movie.basic_info, (movie.all_quotes, 'quotes')


def processing_character(code_id):
    character = Character(code_id)
    character.organize_information()

    return character, character.baisc_info, (character.personal_details, 'personal details')


def processing_quote(code_id):
    quote = Quote(code_id)
    quote.organize_information()

    return quote, quote.basic_info, (quote.which, 'which movie and character')


def processing_chapter(code_id):
    chapter = Chapter(code_id)
    chapter.organize_information()

    return chapter, chapter.basic_info, (chapter.which, 'which book')
