import sys
import urllib3 
import random
import time  
import Adafruit_DHT as dht

# Enter Your API key here
#myAPI= 'YTO65N2C4JEDKXMI'
myAPI= 'PU9CNPOBWV7HHNZ4'
# URL where we will send the data, Don't change it
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI 
def DHT22_data():
	# Dummey data of temperature and humidity
	humi, temp = dht.read_retry(dht.DHT22,23)
	return humi, temp

print("Exit data logging with control+c")
while True:
	try:
		humi,temp = DHT22_data()
		print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temp,humi))
		#Sending the data to thingspeak
		con = urllib3.PoolManager()
		response = con.request('GET', baseURL + '&field1=%s&field2=%s' % (temp, humi))
		print(response.status)
		print("Sample transfer OK")
		# DHT22 requires 5 seconds to give a reading
		time.sleep(5)
			
	except  KeyboardInterrupt:
        		exit()
