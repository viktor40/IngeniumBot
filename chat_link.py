from filetail import FileTail
tail = FileTail("../mscs/worlds/survival/console.out")
for line in tail:
    print(line, end="")
