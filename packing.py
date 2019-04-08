
def main():
        orderWeight = 0
        binNumber = 0
        binNumber = input("please scan the bin you are packing: ")
        print("thank you, scan the bin again to close the order. you may not start packing your order.")
    
        orderWeight = pack(binNumber)
        
        print("the mass of your order is:")
        print(orderWeight)
        
        #open file and write order mass
        
        file = open("binID.txt", "a") 
        with file as f:
            for line in f:
                if line.startswith(binNumber):
                    line.append()
                    line[1] = orderWeight
                    #print("the item mass is:"mass)
    
    return

def pack(binNum):
    count = 0
    barcodeRead = 0
    binMass = 0 #will need to change this to the actual bin mass
    barcodeRead = input("scan your first item: ")
    
    while count is 0:
        #print ("The item id is: "barcodeRead)
        massItem = 0 # item weight
        fileItems = open("itemID.txt", "r") #find item mass in lookup table 
        with file as f:
            for line in f:
                if line.startswith(barcodeRead):
                    line = line.split()
                    lineId = line[0]
                    massItem = line[1]
                    #print("the item mass is:"mass)
        binMass = binMass + massItem
        
        barcodeRead = input("scan your next item: ")
        if barcodeRead is binNum
            count = 1

    return binMass

