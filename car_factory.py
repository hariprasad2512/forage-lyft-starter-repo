from abc import ABC
from car import Car
from engine_types.capulet_engine import CapuletEngine
from engine_types.willoughby_engine import WilloughbyEngine
from engine_types.sternman_engine import SternmanEngine

from battery_types.spindler_battery import SpindlerBattery
from battery_types.nubbin_battery import NubbinBattery

class CarFactory(ABC):

    def create_calliope(self,current_date,last_service_date,current_mileage,last_service_mileage):
        car = Car(last_service_date)
        myengine = CapuletEngine(last_service_mileage,current_mileage)
        car.__engine = myengine
        mybattery = SpindlerBattery(last_service_date,current_date)
        car.__battery = mybattery

        return car


    def create_glissade(self,current_date,last_service_date,current_mileage,last_service_mileage):
        car = Car(last_service_date)
        myengine = WilloughbyEngine(last_service_mileage,current_mileage)
        car.__engine = myengine
        mybattery = SpindlerBattery(last_service_date,current_date)
        car.__battery = mybattery

        return car    
    
    def create_palindrome(self,current_date,last_service_date,warning_light_on):
        car = Car(last_service_date)
        myengine = SternmanEngine(warning_light_on)
        car.__engine = myengine
        mybattery = SpindlerBattery(last_service_date,current_date)
        car.__battery = mybattery
        return car
    

    def create_rorschach(self,current_date,last_service_date,current_mileage,last_service_mileage):
        car = Car(last_service_date)
        myengine = WilloughbyEngine(last_service_mileage,current_mileage)
        car.__engine = myengine
        mybattery = NubbinBattery(last_service_date,current_date)
        car.__battery = mybattery

        return car    
    

    def create_thovax(self,current_date,last_service_date,current_mileage,last_service_mileage):
        car = Car(last_service_date)
        myengine = CapuletEngine(last_service_mileage,current_mileage)
        car.__engine = myengine
        mybattery = NubbinBattery(last_service_date,current_date)
        car.__battery = mybattery
        return car