
import time
from sense_hat import SenseHat
import ephem
sense = SenseHat()
i = 0
DerdioLog = open("DerdioLog.csv", "w")
DerdioLog.write("iss.Lat:;iss.Long;time;temp;humidity;pressure;")
while i < 16:
    iss = ephem.readtle("ISS (ZARYA)",
                    "1 25544U 98067A   19043.42555361  .00001350  00000-0  28477-4 0  9999",
                    "2 25544  51.6412 261.6420 0005384  21.1164  41.7177 15.53256867155878")
    msleep = lambda x: time.sleep(x / 1000.0)
    cTime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    iss.compute()
    print("ISS POSITION: Lat:\t%s\tLong:\t%s" % (iss.sublat, iss.sublong))
    print("Time: %s UTC" % cTime)
    humidity = sense.get_humidity()
    print("Humidity: %s %%rH" % humidity)
    pressure = sense.get_pressure()
    print("Pressure: %s Millibars" % pressure)
    temp = sense.get_temperature()
    print("Temperature: %s C" % temp)
    DerdioLog.write("{0};{1};{2};{3};{4};{5};\n".format(iss.sublat, iss.sublong, cTime, temp, humidity, pressure));
    msleep(600000)
    i += 1
    if i is 16:
        DerdioLog.close()




   

 


