from access.endpoint import create_endpoints
from access.request import make_request


class Book:

    def __init__(self, code_id):
        self.__info = make_request('about book', code_id)

        self.__title = self.__info['docs'][0]['name']
        self.__code_id = self.__info['docs'][0]['_id']

        self.__all_chapters = dict()
        self.__details = {'details': 'No further details found'}

        self.__basic_info = dict()

    def __str__(self):
        return self.__title

    def organize_information(self):
        self.__basic_info['id'] = self.__code_id
        self.__basic_info['title'] = self.__title

    def capture_chapters(self):
        request = make_request('chapters of book', self.__code_id)

        for i in request['docs']:
            if not i == 'name' or i == '_id':
                self.__all_chapters[i['_id']] = i['chapterName']

    @property
    def title(self):
        return self.__title

    @property
    def code_id(self):
        return self.__code_id

    @property
    def all_chapters(self):
        return self.__all_chapters

    @property
    def details(self):
        return self.__details

    @property
    def basic_info(self):
        return self.__basic_info
