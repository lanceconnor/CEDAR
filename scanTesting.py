def extract():
    extractBar = 0
    extractBar = input()
    
    x = 0 # bin number
    y = 0 # bin weight
    file = open("itemID.txt", "r")
    with file as f:
        for line in f:
            if line.startswith(extractBar):
                line = line.split()
                x = int(line[1])
                y = int(line[2])
    return y