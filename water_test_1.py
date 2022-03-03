from gpiozero import LED
import time

pump = LED(20, initial_value=True)
solenoid_1 = LED(21, initial_value=True)
solenoid_2 = LED(26, initial_value=True)



try:
    solenoid_1.off()
    time.sleep(1)
    pump.off()
    time.sleep(3)
    pump.on()
    time.sleep(1)
    solenoid_1.on()
    time.sleep(1)
    solenoid_2.off()
    time.sleep(1)
    pump.off()
    time.sleep(3)
    pump.on()
    time.sleep(1)
    solenoid_2.on()

finally:
    pump.close()
    solenoid_1.close()
    solenoid_2.close()
