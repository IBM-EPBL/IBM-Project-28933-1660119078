#importing Random function to generate the value and required IoT and System Libraries
import random as rand
import time
import ibmiotf.application
import ibmiotf.device
import sys


#defining credentials of device
organization = "sfq80i"
deviceType = "IoTDevice"
deviceId = "PNT2022TMID30308"
authMethod = "token"
authToken = "dAdKBdtr*Er(mud*0x"

# Initialize GPIO
# code to activate the motor comes here in Sprint 4
def myCommandCallback(cmd):
    # Command Call back
    print("Command received: %s" % cmd.data['command'])


try:
    deviceOptions = {"org" : organization, "type": deviceType, "id" : deviceId, "auth-method" : authMethod, "auth-token" : authToken}
    deviceCli = ibmiotf.device.Client(deviceOptions)

except Exception as e:
    print("Caught exception connecting device: %s" %str(e))
    sys.exit()


deviceCli.connect()

while True:
    print("Welcome to Real-Time River Water Quality Monitoring and Control System")
    temperature = int(rand.randint(0,125))
    pH = int(rand.randint(0,14))
    DO = int(rand.randint(0,150))
    TSS = int(rand.randint(0,3700))
    Manganese = int(rand.randint(0,1000))
    Copper = int(rand.randint(0,2000))
    ammoniaNitrate = int(rand.randint(0,100))
    Hardness = int(rand.randint(0,1000))
    Zinc =  int(rand.randint(0,100))        
    Conductivity =  f"{float(rand.uniform(0.001,2000)):.2f}"
    Chloride = int(rand.randint(0,200))
    Sulphate = int(rand.randint(0,1000))

    data = {"Temperature": temperature,
            "pH": pH,
            "DO": DO,
            "TSS": TSS,
            "Manganese": Manganese,
            "Copper": Copper,
            "AmmoniaNitrate":ammoniaNitrate,
            "Hardness":Hardness,
            "Zinc": Zinc,
            "Conductivity": Conductivity,
            "Chloride": Chloride,
            "Sulphate": Sulphate
        }
        #These variables store value of ramdom data to be shared to the cloud

        #printing the values
    def myOnPublishCallback():
        print("Published all data to IBM Watson")

    success = deviceCli.publishEvent("IotSensor","json",data,qos=0,on_publish=myOnPublishCallback)
    if not success:
        print("Not connected to IoT Device")
    time.sleep(1)

    deviceCli.commandCallback = myCommandCallback

    
#Disconnect the device and application from the cloud
deviceCli.disconnect()


