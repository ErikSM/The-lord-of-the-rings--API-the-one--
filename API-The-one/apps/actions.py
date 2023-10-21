from objects.Book import Book
from objects.Chapter import Chapter
from objects.Character import Character
from objects.Movie import Movie
from objects.Quote import Quote


def processing_data(menu_selected, id_selected):
    info_tuple = tuple
    if menu_selected == 'all books':
        info_tuple = processing_book(id_selected)
    elif menu_selected == 'all movies':
        info_tuple = processing_movie(id_selected)
    elif menu_selected == 'all characters':
        info_tuple = processing_character(id_selected)
    elif menu_selected == 'all quotes':
        info_tuple = processing_quote(id_selected)
    elif menu_selected == 'all chapters':
        info_tuple = processing_chapter(id_selected)

    return info_tuple


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
