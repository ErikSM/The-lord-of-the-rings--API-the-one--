from access.request import make_request


class Character:

    def __init__(self, code_id):
        self.__info = make_request('about character', code_id)

        self.__name = self.__info['docs'][0]['name']
        self.__code_id = self.__info['docs'][0]['_id']

        self.__which = {'book': 'unidentified book', 'movie': 'unidentified movie'}
        self.__personal_details = dict()

        self.__basic_info = dict()

    def __str__(self):
        return self.__name

    def organize_information(self):
        self.__basic_info['id'] = self.__code_id
        self.__basic_info['title'] = self.__name

        for i in self.__info['docs'][0]:
            if not i == 'name' or i == '_id':
                self.__personal_details[i] = self.__info['docs'][0][i]

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
    def personal_details(self):
        return self.__personal_details

    @property
    def baisc_info(self):
        return self.__basic_info
