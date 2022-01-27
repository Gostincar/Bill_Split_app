'''
Object that contains data about bills, what should you pay,
sush as Apartment bills, car and etc..
'''

class Bill:

    def __init__(self,amount,car):
        self.amount = amount
        self.car = car

'''
Class that creats method for caclucating expences
'''


class Roommate:


    def __init__(self,name,car_usage,DaysInHouse):
        self.name = name
        self.car_usage = car_usage
        self.DaysInHouse = DaysInHouse


    def pays(self,bill,roommate):
        money =( self.DaysInHouse / (self.DaysInHouse + roommate.DaysInHouse) +
                 (self.car_usage/ (self.car_usage + roommate.car_usage)) )/2
        paying = (bill.amount + bill.car )*money
        return float(paying)




