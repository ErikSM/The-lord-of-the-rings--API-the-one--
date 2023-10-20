from access.request import make_request


class Movie:

    def __init__(self, code_id):

        self.__info = make_request('about movie', code_id)

        self.__name = self.__info['docs'][0]['name']
        self.__code_id = self.__info['docs'][0]['_id']

        self.__all_quotes = dict()

        self.__tecnical_details = dict()
        self.__basic_info = dict()

    def __str__(self):
        return self.__name

    def organize_information(self):
        self.__basic_info['id'] = self.__code_id
        self.__basic_info['title'] = self.__name

        for i in self.__info['docs'][0]:
            self.__tecnical_details[i] = self.__info['docs'][0][i]

    def capture_quotes(self):
        request = make_request('quotes of movie', self.__code_id)
        for i in request['docs']:
            self.__all_quotes[i['_id']] = i['dialog']

    @property
    def name(self):
        return self.__name

    @property
    def code_id(self):
        return self.__code_id

    @property
    def all_quotes(self):
        return self.__all_quotes

    @property
    def tecnical_details(self):
        return self.__tecnical_details

    @property
    def basic_info(self):
        return self.__basic_info
