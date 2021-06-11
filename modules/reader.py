def reader(file):
    file_ = open(r'orders/{}'.format(file), 'r')
    line = file_.readlines()
    line = list(map(lambda l: l.rstrip('\n'), line)) #This line strip all \n in the element from the list
    return line