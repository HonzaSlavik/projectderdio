from sense_hat import SenseHat
import datetime
from time import sleep

#object for work with SenseHat
sense = SenseHat()

#Set ISS rotation 
sense.set_rotation(270)

#Infinite loop (the cycle repeats itself)
while True:
    datetime_object = datetime.datetime.now()
    print(datetime_object)
    humidity = sense.get_humidity()
    print ("Humidity: %s %%rH" % humidity)
    temp = sense.get_temperature()
    print("Temperature: %s C" % temp)
    pressure = sense.get_pressure()
    print("Pressure: %s Millibars" % pressure)
    sleep(120)
