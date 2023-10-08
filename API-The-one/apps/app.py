from tkinter import *

from access.addresses import create_endpoints
from access.api_info import string_about_api
from access.request import make_request

colors = {'dark_green': '#021D09', 'white': '#C8DACE',
          'green': '#1C3926', 'gold': '#42340E', 'black': 'black'}


class App:

    def __init__(self):

        self.window = Tk()
        self.window.title("The Lord of the rings App")
        self.window.geometry("+300+200")
        self.window.resizable(True, True)
        self.window.config(bg=colors['black'])

        self.menu = Menu(self.window, bd=10)
        self.window.config(menu=self.menu)

        self.menu.add_command(label='Initial setting', command=lambda: self.welcome(True))

        self.entry = Entry(self.window, bd=5, disabledbackground=colors['black'], width=156)
        self.entry.config(state=DISABLED)
        self.entry.grid(row=0, column=0, columnspan=11)

        self.list_left = Listbox(self.window, bd=3, height=10, width=90)
        self.list_left.config(bg=colors['dark_green'], fg=colors['white'])
        self.list_left.grid(row=1, rowspan=9, column=1, columnspan=7)
        y_axis = Scrollbar(self.window, orient=VERTICAL, command=self.list_left.yview)
        y_axis.grid(row=1, rowspan=9, column=0, sticky=N + S)
        self.list_left.config(yscrollcommand=y_axis.set)

        self.list_right = Listbox(self.window, bd=3, height=10, width=40)
        self.list_right.config(bg=colors['dark_green'], fg=colors['white'])
        self.list_right.grid(row=1, rowspan=9, column=10, columnspan=11)
        y_axis = Scrollbar(self.window, orient=VERTICAL, command=self.list_right.yview)
        y_axis.grid(row=1, rowspan=9, column=9, sticky=N + S)
        self.list_right.config(yscrollcommand=y_axis.set)

        self.play = Button(self.window, text='play', bd=2, width=15)
        self.play.config(bg=colors['gold'], command=self.do_play)
        self.play.grid(row=2, column=8)

        cont = 3
        while cont < 7:
            Button(self.window, width=15, bg=colors['gold']).grid(row=cont, column=8)
            cont += 1

        self.text = Text(self.window, bd=3, height=20, width=132)
        self.text.config(bg=colors['dark_green'], fg=colors['white'])
        self.text.grid(row=10, column=1, columnspan=10)
        y_axis = Scrollbar(self.window, orient=VERTICAL, command=self.text.yview)
        y_axis.grid(row=10, column=0, sticky=N + S)
        self.text.config(yscrollcommand=y_axis.set)

        self.welcome()

        self.window.mainloop()

    def _clear(self, field='all'):
        if field == "list left":
            self.list_left.delete(0, END)
        elif field == "list right":
            self.list_right.delete(0, END)
        elif field == "text":
            self.text.delete(1.0, END)
        else:
            self.text.delete(1.0, END)
            self.list_right.delete(0, END)
            self.list_left.delete(0, END)

    def write_text(self, message, field='text'):
        if field == "list left":
            self.list_left.insert(END, message)
        elif field == "list right":
            self.list_right.insert(END, message)
        elif field == "text not space":
            self.text.insert(END, '\n')
            self.text.insert(END, message)
            self.text.insert(END, '\n')
        else:
            self.text.insert(END, '\n\n')
            self.text.insert(END, message)
            self.text.insert(END, '\n\n')

    def welcome(self, from_menu=False):
        if from_menu:
            self._clear()

        self.text.insert(END, string_about_api)

        test_dict = create_endpoints()
        for i in test_dict:
            if i == 'research id':
                pass
            elif test_dict[i][2]:
                pass
            else:
                self.list_left.insert(END, i)

    def do_play(self):

        capture = self.list_left.get(ANCHOR)
        request = make_request(capture)

        dictionary_opened = request[0]
        dict_string = request[1]

        self._clear()

        self.write_text(f'--(({capture}))--')
        for i in dictionary_opened:
            if i == 'docs':
                self.write_text(f'*{dict_string}:\n\n\n\n')
                for j in dictionary_opened[i]:
                    if capture == "movies quotes":
                        self.write_text(j['dialog'], "list left")
                        self.write_text(j, 'text not space')
                    elif capture == "books chapters":
                        self.write_text(j['chapterName'], "list left")
                        self.write_text(j, 'text not space')
                    else:
                        self.write_text(j['name'], "list left")
                        self.write_text(j, 'text not space')
            else:
                self.write_text(f'(({i}))', "list right")
                self.write_text(f'{dictionary_opened[i]}', "list right")


App()
