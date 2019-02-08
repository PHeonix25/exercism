import re

class Phone():
    def __init__(self, phone_number):
        self.number = self.__clean(phone_number)
        if not self.__validate():
            raise ValueError("Phone number was not valid")

        # Build all the properties we'd ever need!        
        self.country_code = "+1"
        self.area_code = self.number[0:3]
        self.exchange_code = self.number[3:6]
        self.subscriber_number = self.number[6:10]
        self.local_number = self.exchange_code + self.subscriber_number

    @staticmethod
    def __clean(number):
        clean = re.sub("[^0-9]", "", number)

        if clean and len(clean) == 10:
            return clean

        if (len(clean) == 11 and clean[0] == '1'):
            return str(clean[1:])

        raise ValueError("Phone number could not be understood")

    def __validate(self):
        return re.search("[2-9]([0-9]{2})[2-9]([0-9]{6})", self.number)

    def pretty(self):
        return f"({self.area_code}) {self.exchange_code}-{self.subscriber_number}"
