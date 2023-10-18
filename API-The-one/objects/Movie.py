

class Movie:

    def __init__(self, info):

        self.__info = info

        self.__tecnical_details = dict()
        self.__code_id = None
        self.__name = None

        dictionary = self.__info['docs'][0]
        for i in dictionary:
            if i == 'name':
                self.__name = dictionary[i]
            elif i == '_id':
                self.__code_id = dictionary[i]
            else:
                self.__tecnical_details[i] = dictionary[i]

    def __str__(self):
        return self.__name

    def tecnical_details(self):
        return self.__tecnical_details

    @property
    def name(self):
        return self.__name

    @property
    def code_id(self):
        return self.__code_id
