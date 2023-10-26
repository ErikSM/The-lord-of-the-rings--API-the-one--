import matplotlib.pyplot as plt

from apps.configurations import colors


def make_lines_graphic(data_dict: dict, graphic_name='graphic: Line'):
    plt.figure(figsize=(10, 6), facecolor=colors['dark_green'])
    plt.axes().set_facecolor(colors['black'])

    plt.tick_params(axis='x', labelsize=6)
    plt.tick_params(axis='y', labelsize=6)

    list_colors = list()
    for i in colors:
        if not i == 'black':
            list_colors.append(colors[i])

    # grafico de linhas(vermelho)
    cont = 0
    for i in data_dict:
        x_axle, y_axle = data_dict[i][0], data_dict[i][1]
        plt.plot(x_axle, y_axle, color=list_colors[cont], width=1.0)
        cont += 1

    plt.title("{}".format(graphic_name), font="Times New Roman", color="black", fontsize=14)
    plt.xlabel("{}".format('name'), font="Consolas", color="black", fontsize=9)
    plt.ylabel("{}".format('data'), font="Consolas", color="black", fontsize=9)

    plt.show()


def make_bar_graphic(data_list: list, graphic_name='graphic: Line'):
    plt.figure(figsize=(5, 3), facecolor=colors['dark_green'])
    plt.axes().set_facecolor(colors['black'])

    plt.tick_params(axis='x', labelsize=6)
    plt.tick_params(axis='y', labelsize=6)

    list_colors = ['blue', 'red', 'yellow', 'pink',
                   'purple', 'white', 'grey', 'blue', 'red', 'pink']

    # grafico de linhas(vermelho)
    cont = 0
    for i in data_list:
        if i[0] == 0:
            pass
        else:
            x_axle, y_axle = i[1], i[0]
            plt.bar(x_axle, y_axle, color=list_colors[cont], width=1.0)
            cont += 1

    plt.title("{}".format(graphic_name), font="Times New Roman", color="black", fontsize=14)
    plt.xlabel("{}".format('name'), font="Consolas", color="black", fontsize=9)
    plt.ylabel("{}".format('data'), font="Consolas", color="black", fontsize=9)

    plt.show()
