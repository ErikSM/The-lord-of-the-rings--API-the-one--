from tkinter import *

from access.endpoint import create_endpoints
from access.api_info import string_about_api
from access.request import make_request
from apps.configurations import colors
from apps.actions import processing_data
from apps.graphic import make_bar_graphic
from apps.all_generators import statistic_generator_dict
from objects.Character import Character
from objects.Movie import Movie
from statistics.others import movies_to_others_list, characters_with_most_quotes_per_movie
from statistics.quantitative_filters import organize_movies_dict, movies_numbers_list
from statistics.races_genders_realms import realms_founded, race_of_characters, genders_data, statistic_list


def _do_graphic(window, string_and_title: tuple, statistic: dict):
    make_bar_graphic(statistic[string_and_title[1]], string_and_title[0])
    window.destroy()


def _close_window(window):
    window.destroy()


def make_temporary_window(title, string, statistic):
    size = "150x150+400+200"

    top_window = Toplevel()
    top_window.title(title)
    top_window.resizable(False, False)
    top_window.geometry(size)

    Label(top_window, text='\n\nShow graphic??...').pack()

    Button(top_window, text='yes',
           command=lambda: _do_graphic(top_window, (title, string), statistic)).pack()
    Button(top_window, text='no',
           command=lambda: _close_window(top_window)).pack()

    return top_window


class App:

    def __init__(self):
        self.primaries_endpoints = list()

        self.ids_to_select = dict()
        self.menu_selected = str
        self.item_selected = str

        self.window = Tk()
        self.window.title("The Lord of the rings App")
        self.window.geometry("+300+200")
        self.window.resizable(False, False)
        self.window.config(bg=colors['black'], bd=15)

        self.menu = Menu(self.window)
        self.window.config(menu=self.menu)

        self.menu.add_command(label='Initial setting', command=self.initial_settings)

        self.menu_statistic = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Statistics", menu=self.menu_statistic)
        for i in statistic_list:
            self.menu_statistic.add_command(label=i.title(),
                                            command=lambda string=i: self.processing_statistic(string))

        self.menu_movies_numbers = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Numbers of movies", menu=self.menu_movies_numbers)
        for i in movies_numbers_list:
            self.menu_movies_numbers.add_command(label=i.title(),
                                                 command=lambda string=i: self.processing_movies_numbers(string))

        self.menu_others = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Characters with the most quotes", menu=self.menu_others)
        for i in movies_to_others_list:
            self.menu_others.add_command(label=f"{Movie(i)}",
                                         command=lambda string=i: self.processing_others(string))

        self.entry_path = Entry(self.window, bd=7, disabledbackground=colors['black'], width=156)
        self.entry_path.config(state=DISABLED)
        self.entry_path.grid(row=0, column=0, columnspan=11)

        self.list_left = Listbox(self.window, bd=3, height=10, width=90)
        self.list_left.config(bg=colors['green'], fg=colors['ice'], selectbackground=colors['gold'])
        self.list_left.grid(row=1, rowspan=9, column=1, columnspan=7)
        y_list_left = Scrollbar(self.window, orient=VERTICAL, command=self.list_left.yview)
        y_list_left.grid(row=1, rowspan=9, column=0, sticky=N + S)
        self.list_left.config(yscrollcommand=y_list_left.set)

        self.list_right = Listbox(self.window, bd=4, height=10, width=40, state=DISABLED)
        self.list_right.config(bg=colors['dark_green'], fg=colors['ice'])
        self.list_right.grid(row=1, rowspan=9, column=10, columnspan=11)
        y_list_right = Scrollbar(self.window, orient=VERTICAL, command=self.list_right.yview)
        y_list_right.grid(row=1, rowspan=9, column=9, sticky=N + S)
        self.list_right.config(yscrollcommand=y_list_right.set)

        self.button_one = Button(self.window, text='', bd=2, width=15)
        self.button_two = Button(self.window, text='', bd=2, width=15, )
        self.button_three = Button(self.window, text='', bd=2, width=15)
        self.button_four = Button(self.window, text='', bd=2, width=15)
        self.button_five = Button(self.window, text='', bd=2, width=15)

        self.buttons_list = list()
        self.buttons_list.append(self.button_one)
        self.buttons_list.append(self.button_two)
        self.buttons_list.append(self.button_three)
        self.buttons_list.append(self.button_four)
        self.buttons_list.append(self.button_five)

        self.text = Text(self.window, bd=3, height=20, width=132)
        self.text.config(bg=colors['dark_green'], fg=colors['ice'], selectbackground=colors['gold'])
        self.text.grid(row=10, column=1, columnspan=10)
        y_axis_text = Scrollbar(self.window, orient=VERTICAL, command=self.text.yview)
        y_axis_text.grid(row=10, column=0, sticky=N + S)
        self.text.config(yscrollcommand=y_axis_text.set)

        self.setting_menus()
        self.setting_buttons()

        self.window.mainloop()

    def _clear(self, field='all'):
        if field == "list left":
            self.list_left.delete(0, END)

        elif field == "list right":
            self.list_right.config(state=NORMAL)
            self.list_right.delete(0, END)
            self.list_right.config(state=DISABLED)

        elif field == "text":
            self.text.delete(1.0, END)

        elif field == "entry path":
            self.entry_path.config(state=NORMAL)
            self.entry_path.delete(0, END)
            self.entry_path.config(state=DISABLED)

        else:
            self.text.delete(1.0, END)
            self.list_left.delete(0, END)

            self.list_right.config(state=NORMAL)
            self.list_right.delete(0, END)
            self.list_right.config(state=DISABLED)

    def _write_text(self, message, field='text'):

        if field == "list left":
            self.list_left.insert(END, message)

        elif field == "list right":
            self.list_right.config(state=NORMAL)
            self.list_right.insert(END, message)
            self.list_right.config(state=DISABLED)

        elif field == "entry path":
            self.entry_path.config(state=NORMAL)
            self.entry_path.insert(END, f'{message}>')
            self.entry_path.config(state=DISABLED)

        elif field == "text not space":
            self.text.insert(END, '\n')
            self.text.insert(END, message)

        else:
            self.text.insert(END, '\n\n')
            self.text.insert(END, message)
            self.text.insert(END, '\n\n')

    def initial_settings(self):
        self.text.config(state=NORMAL)

        self._clear('entry path')
        self._clear()

        self.menu_selected = None
        self.primaries_endpoints = list()
        self.ids_to_select = dict()

        self.setting_menus()
        self.setting_buttons('initial')

    def setting_menus(self):
        self._write_text(string_about_api, 'text not space')
        self._write_text('menu', 'entry path')

        endpoints = create_endpoints()
        for i in endpoints:
            if i == 'research id' or not endpoints[i][1]:
                pass
            else:
                self.primaries_endpoints.append(i)

        for i in self.primaries_endpoints:
            self._write_text(i, 'list left')

    def setting_buttons(self, config='initial'):
        if config == 'initial':
            for i in self.buttons_list:
                i.config(text='', state=DISABLED)
            self.buttons_list[0].config(text='research', command=self.do_research, state=NORMAL)
            self.buttons_list[1].config(text='')

        elif config == 'finish':
            self.buttons_list[0].config(text='back to start', command=self.initial_settings)

        else:
            self.buttons_list[0].config(text=f'about {config[4:-1]}', command=self.do_search_about_item)

        cont = 2
        while cont < 7:
            for i in self.buttons_list:
                i.config(bg=colors['gold'], fg=colors['black'])
                i.grid(row=cont, column=8)
                cont += 1

    def do_research(self):
        capture = self.list_left.get(ANCHOR)

        try:
            requested = make_request(capture)
        except KeyError:
            self._clear('text')
            self._write_text('Error: You have to select a menu item')
        else:
            self.menu_selected = capture
            self.setting_buttons(capture)

            self._clear()
            self._write_text(capture, 'entry path')

            self._show_research(requested)

    def _show_research(self, requested):
        self._write_text(f'--(({self.menu_selected}))--')

        for i in requested:
            if not i == 'docs':
                self._write_text(f'--({i})--', 'list right')
                self._write_text(requested[i], 'list right')

        for i in requested['docs']:
            self._write_text(i)

            if self.menu_selected == 'all chapters':
                name = i['chapterName']
            elif self.menu_selected == 'all quotes':
                name = i['dialog']
            else:
                name = i['name']

            self.ids_to_select[name] = i['_id']

        for i in self.ids_to_select:
            self._write_text(i, 'list left')

    def do_search_about_item(self):
        capture = self.list_left.get(ANCHOR)

        try:
            id_selected = self.ids_to_select[capture]
        except KeyError:
            self._clear('text')
            self._write_text('Error: You have to select a menu item', 'text')
        else:
            self.item_selected = capture
            data_tuple = processing_data(self.menu_selected, id_selected)

            self._clear()
            self._write_text(self.item_selected, 'entry path')

            self._show_search_about_item(data_tuple)

    def _show_search_about_item(self, data_tuple):
        text_data, list_right_data, list_left_data = data_tuple[0], data_tuple[1], data_tuple[2]

        self._write_text(f'  *{self.menu_selected[4:-1]} selected:'.title())
        for i in text_data:
            self._write_text(f'-[{i}]: {text_data[i]}', 'text not space')

        for i in list_right_data:
            self._write_text(f'---({i})---', 'list right')
            self._write_text(f'{list_right_data[i]}', 'list right')
            self._write_text(f'\n', 'list right')

        for i in list_left_data:
            self.ids_to_select = dict()
            self.ids_to_select[list_left_data[i]] = i
            self._write_text(f'{list_left_data[i]}', 'list left')

        self.setting_buttons('finish')
        self.text.config(state=DISABLED)

    #  ---  ------------ in progress  ----------  --------
        #  *obs: execucao esta muito lenta
    def processing_others(self, string):

        title_dict = {"5cd95395de30eff6ebccde5b": "The Two Towers",
                      "5cd95395de30eff6ebccde5c": "The Fellowship of the Ring",
                      "5cd95395de30eff6ebccde5d": "The Return of the King"}

        title = title_dict[string]
        statistic_dict = characters_with_most_quotes_per_movie()

        self._clear('text')
        self._write_text(title, 'text')

        self._do_statistic(title, string, statistic_dict)
        self.setting_buttons('others')

    #  ---------------------------------------------------

    def processing_statistic(self, string):
        title = None
        statistic_dict = None

        if string == 'realms':
            title = "Population of each Realm"
            statistic_dict = realms_founded()
        elif string == 'race':
            title = "Number of Characters by Race"
            statistic_dict = race_of_characters()
        elif string == 'genders':
            title = "Number of Characters per Gender"
            statistic_dict = genders_data()

        self._clear('text')
        self._write_text(title, 'text')

        self._do_statistic(title, string, statistic_dict)

    def processing_movies_numbers(self, string):
        title = None
        movies_numbers_dict = organize_movies_dict()

        if string == 'runtimeInMinutes':
            title = "Runtime In Minutes"
        elif string == 'budgetInMillions':
            title = "Budget In Millions"
        elif string == 'boxOfficeRevenueInMillions':
            title = "Box Office Revenue In Millions"
        elif string == "academyAwardNominations":
            title = "Academy Award Nominations"
        elif string == "academyAwardWins":
            title = "Academy Award Wins"
        elif string == "rottenTomatoesScore":
            title = "Rotten Tomatoes Score"

        self._clear('text')
        self._write_text(title, 'text')

        self._do_statistic(title, string, movies_numbers_dict)

    def _do_statistic(self, title, string, statistic: dict):

        if string in movies_to_others_list:
            test_dict_dois = statistic_generator_dict(statistic[string])
            self._clear('list left')

            for i in test_dict_dois:
                text = f"{i[1]}:  ({i[0]})"
                self._write_text(text, 'text not space')

                self._write_text(i, 'list left')

            #  make_temporary_window(title, string, statistic)

        else:
            test_dict = statistic_generator_dict(statistic[string])

            for i in test_dict:
                text = f"{i[1]}:  ({i[0]})"
                self._write_text(text, 'text not space')

            make_bar_graphic(statistic[string], title)
