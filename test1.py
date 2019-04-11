## test1.py

import time
import busio
import adafruit_ina219
from ina219 import INA219
i2c = busio.I2C(board.SCL, board.SDA)

    ina219 = adafruit_ina219.INA219(i2c_bus)
     
    print("ina219 test")

  if (i2c.try_lock())
	print("EXIT_FAILURE1");

  while not i2c.try_lock():
	pass
     
    while True:
        print("Bus Voltage:   {} V".format(ina219.bus_voltage))  ##b/w GND and V-    use 2 and 9
        print("Shunt Voltage: {} mV".format(ina219.shunt_voltage / 1000))  ##b/w V- and V+
        print("Load Voltage:  {} V".format(ina219.bus_voltage + ina219.shunt_voltage))  
        print("Current:       {} mA".format(ina219.current))
        print("")

	if(ina219.current >= 430)
	  print("Warning: current exceeds limit!")

	except KeyboardInterrupt:
		print(EXIT_FAILURE2)

        time.sleep(1)

	busio.I2C.unlock()


