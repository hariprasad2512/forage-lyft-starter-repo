from abc import ABC
from car import Car
from engine_types.capulet_engine import CapuletEngine
from engine_types.willoughby_engine import WilloughbyEngine
from engine_types.sternman_engine import SternmanEngine

from battery_types.spindler_battery import SpindlerBattery
from battery_types.nubbin_battery import NubbinBattery
from tires import carrigan_tire_service
from tires import octoprime_tire_service
class CarFactory(ABC):

    def create_calliope(self,tire_sensors,current_date,last_service_date,current_mileage,last_service_mileage):
        car = Car(last_service_date)
        myengine = CapuletEngine(last_service_mileage,current_mileage)
        car.__engine = myengine
        mybattery = SpindlerBattery(last_service_date,current_date)
        car.__battery = mybattery
        count = 0
        sum = 0
        for tire in tire_sensors:
            if(tire >= 0.9):
                count+=1
            
            sum += tire
        
        if(count >= 1):
            carrigan_tire_service()
        
        if(sum >= 3):
            octoprime_tire_service()

        return car


    def create_glissade(self,tire_sensors,current_date,last_service_date,current_mileage,last_service_mileage):
        car = Car(last_service_date)
        myengine = WilloughbyEngine(last_service_mileage,current_mileage)
        car.__engine = myengine
        mybattery = SpindlerBattery(last_service_date,current_date)
        car.__battery = mybattery
        count = 0
        sum = 0
        for tire in tire_sensors:
            if(tire >= 0.9):
                count+=1
            
            sum += tire
        
        if(count >= 1):
            carrigan_tire_service()
        
        if(sum >= 3):
            octoprime_tire_service()


        return car    
    
    def create_palindrome(self,tire_sensors,current_date,last_service_date,warning_light_on):
        car = Car(last_service_date)
        myengine = SternmanEngine(warning_light_on)
        car.__engine = myengine
        mybattery = SpindlerBattery(last_service_date,current_date)
        car.__battery = mybattery
        count = 0
        sum = 0
        for tire in tire_sensors:
            if(tire >= 0.9):
                count+=1
            
            sum += tire
        
        if(count >= 1):
            carrigan_tire_service()
        
        if(sum >= 3):
            octoprime_tire_service()

        return car
    

    def create_rorschach(self,tire_sensors,current_date,last_service_date,current_mileage,last_service_mileage):
        car = Car(last_service_date)
        myengine = WilloughbyEngine(last_service_mileage,current_mileage)
        car.__engine = myengine
        mybattery = NubbinBattery(last_service_date,current_date)
        car.__battery = mybattery
        count = 0
        sum = 0
        for tire in tire_sensors:
            if(tire >= 0.9):
                count+=1
            
            sum += tire
        
        if(count >= 1):
            carrigan_tire_service()
        
        if(sum >= 3):
            octoprime_tire_service()


        return car    
    

    def create_thovax(self,tire_sensors,current_date,last_service_date,current_mileage,last_service_mileage):
        car = Car(last_service_date)
        myengine = CapuletEngine(last_service_mileage,current_mileage)
        car.__engine = myengine
        mybattery = NubbinBattery(last_service_date,current_date)
        car.__battery = mybattery
        count = 0
        sum = 0
        for tire in tire_sensors:
            if(tire >= 0.9):
                count+=1
            
            sum += tire
        
        if(count >= 1):
            carrigan_tire_service()
        
        if(sum >= 3):
            octoprime_tire_service()

        return car