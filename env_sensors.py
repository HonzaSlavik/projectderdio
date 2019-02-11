import time
from sense_hat import SenseHat

#objekt pro praci se SenseHat
sense = SenseHat()

#lambda funkce pro sleep v ms
msleep = lambda x: time.sleep(x / 1000.0)

#vytvoreni souboru pro zapis logu a zapsani hlavicky
tempLog = open("tempLog.csv","w")
tempLog.write("time;temp humidity;temp pressure;temp CPU;humidity;pressure\n");

#nekonecna smycka (cyklus se stale opakuje)
while True:
        #precteme si hodnoty z cidel na SenseHatu
	humidity = sense.get_humidity()
	temp = sense.get_temperature()
	temp2 = sense.get_temperature_from_pressure()
	pressure = sense.get_pressure()
	#precteme si teplotu z CPU
	cpuTemp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp

	#konverze casu do vhodneho formatu (UTC time) - https://docs.python.org/2/library/time.html
	cTime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

	#vytiskneme a zformatujeme vypis do konzole
	print("humidity: {0} %%rH, temperature: {1} and {2}, {4}, pressure: {3}".format(humidity, temp, temp2, pressure, cpuTemp))
	#vypis do souboru - musime pridat konec radky (\n)
	tempLog.write("{0};{1};{2};{3};{4};{5}\n".format(cTime, temp, temp2, cpuTemp, humidity,pressure));
	#zapsani souboru, abysme neprisli o posledni radky pri ukonceni smycky
	tempLog.flush();

	#trosku si pospime
	msleep(5000)

#zavreme soubor - pozor, sem se pravdepodobne program nikdy nedostane
tempLog.close();
