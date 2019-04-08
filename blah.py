def extract():
    barcodeRead = 45693287
    #barcodeRead = input("please scan for ol' betsy: ")
    #print (barcodeRead)
    id = 0 # bin number
    mass = 0 # bin weight
    file = open("itemID.txt", "r") #will be binID as this is Judging 
    with file as f:
        for line in f:
            if line.startswith(barcodeRead):
                #line = line.split()
                id = line[0]
                mass = line[1]
                print("the mass is:")
                print(mass)
    return

extract()