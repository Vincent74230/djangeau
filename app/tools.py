"""Contains GPIO control tools and other functions"""
from gpiozero import DistanceSensor, LED
import time


def distance_sensor():
    """returns water level"""
    sensor = DistanceSensor(echo=24, trigger=23)
    return sensor.distance * 100


def water_plants(water):
    """Takes in arguments the quantity of water per plant(solenoid) and waters the plants"""
    pump = LED(20, initial_value=True)
    solenoid_1 = LED(21, initial_value=True)
    solenoid_2 = LED(26, initial_value=True)
    solenoid_list=[solenoid_1, solenoid_2]

    try:
        solenoid_counter = 0
        for water_per_plant in water:
            #for 1 second, the pump will deliver 80ml approximatively
            seconds_of_watering = (water_per_plant*1000)/80

            #setting up the current solenoid
            current_solenoid = solenoid_list[solenoid_counter]

            #start watering using current solenoid
            current_solenoid.off()
            time.sleep(1)
            pump.off()
            time.sleep(seconds_of_watering)
            pump.on()
            time.sleep(1)
            current_solenoid.on()
            time.sleep(1)

            solenoid_counter += 1
    finally:
        pump.close()
        solenoid_1.close()
        solenoid_2.close()
