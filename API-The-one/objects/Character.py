

class Character:

    def __init__(self, info):

        self.__info = info

        self.__personal_details = dict()
        self.__code_id = None
        self.__name = None

        docs_info = self.__info['docs'][0]
        for i in docs_info:
            if i == 'name':
                self.__name = docs_info[i]
            elif i == '_id':
                self.__code_id = docs_info[i]
            else:
                self.__personal_details[i] = docs_info[i]

    def __str__(self):
        return self.__name

    def personal_details(self):
        return self.__personal_details

    @property
    def nome(self):
        return self.__name

    @property
    def code_id(self):
        return self.__code_id
