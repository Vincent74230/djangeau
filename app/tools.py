"""Contains GPIO control tools and other functions"""
import time
import datetime
from gpiozero import DistanceSensor, LED


def distance_sensor():
    """returns water level"""
    sensor = DistanceSensor(echo=24, trigger=23)
    water_level = sensor.distance * 100
    sensor.close()
    return water_level


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

def print_in_the_file(water_level):
    """It only writes in a file, date, watering and if no water"""
    if water_level < 31:
        date = datetime.datetime.now()
        date = str(date)
        with open("fichier.txt", "a") as mon_fichier:
            mon_fichier.write("Arrosage effectué le: "+date +'\n')
    else:
        with open("fichier.txt", "a") as mon_fichier:
            mon_fichier.write("PLus d'eau "+date+'\n')
