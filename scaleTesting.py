import usb
import usb.core
import usb.util

#cycle = 0

def convert():
    massArr = weigh()
    
    scalingFactor = 0
    
    if massArr[2] is 2:
        mass = massArr[4] + (256 * massArr[5])
    else:
        scalingFactor =10**(massArr[3] - 256)
        mass = scalingFactor * (massArr[4] + (256 * massArr[5]))
    
    print ("the mass is:")
    print (mass)
    return


def weigh():
    VENDOR_ID = 0x0922
    PRODUCT_ID = 0x8003
    
    temp_cycle = 0 

# find the USB device
    
    dev = usb.core.find(idVendor=0x0922, idProduct=0x8003)
    #dev = usb.core.find(idProduct=PRODUCT_ID, idVendor=VENDOR_ID)
    if dev is None:
        raise ValueError("device not found")
    else:
        #print(dev.idProduct)
        print("scale read successful")

    #global cycle
    #temp_cycle = cycle


# unload driver from scale and set first endpoint
    if dev.is_kernel_driver_active(interface=0):
        dev.detach_kernel_driver(0)
        endpoint = dev[0][(0,0)][0]
    else:
        endpoint = dev[0][(0,0)][0]

# read a data packet
    attempts = 10 #we might want it to run for more than 10 attempts depending on the delay between when the barcode is read and when the bin winds up sitting on the scale - Lance
    data = None
    while data is None and attempts > 0:
        try:
            data = dev.read(endpoint.bEndpointAddress,
                           endpoint.wMaxPacketSize)
        except usb.core.USBError as e:
            data = None
            if e.args == ('Operation timed out',):
                attempts -= 1
            continue
    #print (data)
    
    return data

convert()


