from access.request import make_request
from objects.Book import Book


class Chapter:

    def __init__(self, code_id):

        self.__info = make_request('about chapter', code_id)

        self.__code_id = self.__info['docs'][0]['_id']
        self.__name = self.__info['docs'][0]['chapterName']

        self.__which = {'book': self.__info['docs'][0]['book']}
        self.__details = {'details': 'No further details found'}
        self.__basic_info = dict()

    def __str__(self):
        return self.__name

    def organize_information(self):
        self.__basic_info['id'] = self.__code_id
        self.__basic_info['title'] = self.__name

    @property
    def name(self):
        return self.__name

    @property
    def code_id(self):
        return self.__code_id

    @property
    def which(self):
        return self.__which

    @property
    def details(self):
        return self.__details

    @property
    def basic_info(self):
        return self.__basic_info
