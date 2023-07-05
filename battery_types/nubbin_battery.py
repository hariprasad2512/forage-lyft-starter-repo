from abc import ABC, abstractmethod
from battery import Battery
from utils import add_years_to_date
class NubbinBattery(Battery,ABC):
    __last_service_date = None
    __current_date = None

    def __init__(self,last_service_date,current_date):
    
        self.__current_date = current_date
        self.__last_service_date = last_service_date

    def needs_service(self):
        date_which_battery_should_be_serviced_by = add_years_to_date(self.last_service_date, 4)
        if date_which_battery_should_be_serviced_by < self.current_date:
            return True
        else:
            return False
    


