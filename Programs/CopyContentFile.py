with open('content.txt', 'r') as src:
    with open('copy.txt', 'w') as dest:
        line = src.readline()
        while line:
            dest.write(line)
            line = src.readline()
