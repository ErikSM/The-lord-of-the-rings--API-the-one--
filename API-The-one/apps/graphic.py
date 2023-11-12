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

    cont = 0
    for i in data_dict:
        x_axle, y_axle = data_dict[i][0], data_dict[i][1]
        plt.plot(x_axle, y_axle, color=list_colors[cont], width=1.0)
        cont += 1

    plt.title("{}".format(graphic_name), font="Times New Roman", color="black", fontsize=14)
    plt.xlabel("{}".format('name'), font="Consolas", color="black", fontsize=9)
    plt.ylabel("{}".format('data'), font="Consolas", color="black", fontsize=9)

    plt.show()


# ---------------------  ---------------  -------------------  --------------------

def make_bar_graphic(data_list: list, graphic_name='graphic: Bar'):
    if len(data_list) > 42:
        plt.figure(figsize=(14, 6), facecolor=colors['dark_green'])

        plt.axes().set_facecolor(colors['black'])
        plt.tick_params(axis='x', labelsize=8)
        plt.tick_params(axis='y', labelsize=4)

    elif 42 >= len(data_list) >= 25:
        plt.figure(figsize=(14, 5), facecolor=colors['dark_green'])

        plt.axes().set_facecolor(colors['black'])
        plt.tick_params(axis='x', labelsize=8)
        plt.tick_params(axis='y', labelsize=6)
    else:
        plt.figure(figsize=(14, 4), facecolor=colors['dark_green'])

        plt.axes().set_facecolor(colors['black'])
        plt.tick_params(axis='x', labelsize=8)
        plt.tick_params(axis='y', labelsize=8)

    for i in data_list:
        if i[0] == 0:
            pass
        else:
            x_axle, y_axle = i[1], i[0]

            plt.barh(x_axle, y_axle, align='center')

    plt.title("{}".format(graphic_name), font="Times New Roman", color="white", fontsize=17)
    plt.xlabel("{}".format('Numbers:'), font="Consolas", color="black", fontsize=7, loc='right')
    plt.ylabel("{}".format('Names:'), font="Consolas", color="black", fontsize=7, loc="top")

    plt.show()
