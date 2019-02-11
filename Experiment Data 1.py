#Připojujeme SenseHat a Čas#
import time
from sense_hat import SenseHat
#Při psaní textu budeme používat SenseHat jako sense#
sense = SenseHat()
#Vytváříme styl času že 1sekunda=1000%
msleep = lambda x: time.sleep(x / 1000.0)
#Vytváříme soubor kde se budou ukládat data z experimentu#
DerdioLog = open("DerdioLog.csv", "w")
#Program vytváří Tabulky#
DerdioLog.write("time;humidity;pressure;temp;")
#Nekonečná smyčka#
while True:
# Nastavujeme časové pásmo UTC#
#Nastavujeme a zapínáme měření času,teploty......a u každého necháme vytisknou data do shell zóny#
    cTime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    print("Time: %s UTC" % cTime)
    humidity = sense.get_humidity()
    print("Humidity: %s %%rH" % humidity)
    pressure = sense.get_pressure()
    print("Pressure: %s Millibars" % pressure)
    temp = sense.get_temperature()
    print("Temperature: %s C" % temp)
    #Ukladáme do dokumentu#
    DerdioLog.write("{0};{1};{2};{3};\n".format(cTime, temp, humidity,pressure));
    DerdioLog.flush();
#Zadávám interval na 2minuty#
    msleep(120000)

#Toto se nikdy nestane, protože je nekonečný#
DerdioLog.close();    

#Program vypnete pomocí shellu a data budou uložené v složce DerdioLog vedle experimentu#

#Toto nemůže jít na ISS, protože není plně automatický konec!!!!!#
#Ukládá to až druhý záznam.#
