from filetail import FileTail


def mc_to_dc():
    tail = FileTail("../mscs/worlds/survival/console.out")
    for line in tail:
        return line
