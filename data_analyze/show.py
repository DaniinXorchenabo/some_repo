

def show(data, labels=[], title="", xlabel="", ylabel="", dotted=False, namefile=None, datax=None):

    import matplotlib.pyplot as plt
    plt.title(title)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    while len(labels) < len(data):
        labels.append("1")
    labels = iter(labels)
    #   plt.legend(tuple([plt.plot(el) for el in data]), tuple(legends), loc = 'best')
    for i, el in enumerate(data):
        next_label = next(labels)
        plt.plot(el, label=next_label)
        if dotted:
            plt.scatter(x=range(len(el)) if not datax else datax[i], y=el, label=next_label)


    plt.legend(loc="lower left")

    plt.grid()
    #
    if namefile:
        plt.savefig('{namefile}.png'.format(namefile=namefile), format='png')
    else:
        plt.show()
    plt.clf()


def histogram(arr, title="", namefile=None, yrange=None):

    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 1)
    plt.title(title)
    axes.bar(range(len(arr)), arr)

    axes.set_facecolor('seashell')
    fig.set_facecolor('floralwhite')
    fig.set_figwidth(12)  # ширина Figure
    fig.set_figheight(6)  # высота Figure
    if yrange:
        plt.ylim(yrange)

    if namefile:
        plt.savefig('{namefile}.png'.format(namefile=namefile), format='png')
    else:
        plt.show()
    plt.clf()