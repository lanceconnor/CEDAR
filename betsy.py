import usb
import usb.core
import usb.util
import RPi.GPIO

def mainJudging():
    
    #GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(11,GPIO.OUT)
    NUMBINS = 2
    NUMITEMS = 7
    TUBMASS = 0 #grams
    TOLERANCE = 1 #grams
    massOrder = 0
    massRead = 0
    loopy = 0

    while (loopy is 0):        
        massOrder = int(extract())
        print ("according to the system, the order should weigh:")
        print (massOrder) #What the order mass should be
        massRead = computeMass()
        print ("the read weight of the order is:")
        print (massRead) #see what was actually read
        lowerBound = massOrder-TOLERANCE
        upperBound = massOrder+TOLERANCE
        if (massRead >= lowerBound and massRead <= upperBound):
            accept()
            massRead = 0
            massOrder = 0
        else:
            reject()
            massRead = 0
            massOrder = 0
    return

    
 
def extract():
    barcodeRead = 0
    barcodeRead = input("please scan for ol' betsy: ")
    #print (barcodeRead)
    id = 0 # bin number
    mass = 0 # bin weight
    file = open("itemID.txt", "r") #will be binID as this is Judging 
    with file as f:
        for line in f:
            if line.startswith(barcodeRead):
                line = line.split()
                id = line[0]
                mass = line[1]
                #print("the mass is:")
                #print(mass)
    return mass


#interpret data array and convert to mass
def computeMass():
    #print ("START COMPUTE MASS")
    mass = 0
    massArr = weigh()
    
    scalingFactor = 0
    
    if massArr[2] is 2:
        mass = massArr[4] + (256 * massArr[5])
    else:
        scalingFactor =10**(massArr[3] - 256)
        mass = scalingFactor * (massArr[4] + (256 * massArr[5]))
    
    #print ("FINISH COMPUTE mass")
    return mass

#retrieve data array from scale

def weigh():
    #print ("START WEIGH")
    VENDOR_ID = 0x0922
    PRODUCT_ID = 0x8003

# find the USB device
    
    dev = usb.core.find(idVendor=0x0922, idProduct=0x8003)
    #dev = usb.core.find(idProduct=PRODUCT_ID, idVendor=VENDOR_ID)
    if dev is None:
        raise ValueError("device not found")
    
    '''else:
        #print(dev.idProduct)
        print("scale read successful")
'''
    #print ("set endpoint")
# unload driver from scale and set first endpoint
    if dev.is_kernel_driver_active(interface=0):
        dev.detach_kernel_driver(0)
        endpoint = dev[0][(0,0)][0]
        #print ("driver active")
    else:
        endpoint = dev[0][(0,0)][0]
        #print ("driver inactive")
    
# read a data packet
    attempts = 10 #we might want it to run for more than 10 attempts depending on the delay between when the barcode is read and when the bin winds up sitting on the scale - Lance
    data = [0,0,0,0,0,0]
    while (data[4] is 0 and attempts > 0):
        #print("pulling scale data")
        try:
            #print("trying")
            data = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
        except usb.core.USBError as e:
            print(e)
            attempts = attempts - 1
            if e.args == ('Operation timed out',):
                continue
    #print ("FINISH WEIGH")
    dev.reset()
    
    return data


def servoCalibration():
    pwm=GPIO.PWM(11,50)
    frequency=50 #Hz
    pulseWidth=0.001
    dutyCycle=pulseWidth*frequency
    
    return


def servoControl(angle,pinNum):
    pwm=GPIO(pinNum,50)
    slope=(1/18)#need to adjust slope based on calibration of our motor
    constant=2#constant will also need to be calibrated
    dutyCycle=slope*angle-constant
    pwm.ChangeDutyCycle(dutyCycle)


def accept():
    #servoControl(180) #final accept angle
    #servoControl(0) #return to home position
    print ('accept package')
    return


def reject():
    #servoControl(-180) #final reject angle
    #servoControl(0) #return to home position
    print ("reject package, betsy ain't having this shit")
    return



mainJudging()