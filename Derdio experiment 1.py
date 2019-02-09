from sense_hat import SenseHat
import datetime
sense = SenseHat()
from time import sleep
sense.set_rotation(270)
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
    







