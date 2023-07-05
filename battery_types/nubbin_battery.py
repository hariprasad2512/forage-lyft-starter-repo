from abc import ABC, abstractmethod
from battery import Battery

class NubbinBattery(Battery,ABC):
    __last_service_date = None
    __current_date = None

    def __init__(self,last_service_date,current_date):
    
        self.__current_date = current_date
        self.__last_service_date = last_service_date

    def needs_service(self):
        return super().needs_service()
    


