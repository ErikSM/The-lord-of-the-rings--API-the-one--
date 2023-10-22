from access.request import make_request
from objects.Character import Character
from objects.Movie import Movie


class Quote:

    def __init__(self, code_id):
        self.__info = make_request('about quote', code_id)

        self.__dialog = self.__info['docs'][0]['dialog']
        self.__code_id = self.__info['docs'][0]['_id']

        self.__which = {'movie': self.__info['docs'][0]['movie'], 'character': self.__info['docs'][0]['character']}
        self.__details = {'details': 'No further details found'}

        self.__basic_info = dict()

    def __str__(self):
        return self.__dialog

    def organize_information(self):
        self.__basic_info['id'] = self.__code_id
        self.__basic_info['title'] = self.__dialog

    @property
    def dialog(self):
        return self.__dialog

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
