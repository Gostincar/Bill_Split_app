from bill_app.room import Bill, Roommate
from bill_app.reports import PdfReport, FileSharer


amount  = float(input("Hey, how much do you pay your apartment(with all your bills): "))
car = float(input("How much are you playing mountly your car?: "))
name1 =input("What is your name?: ")
DaysInHouse1 = int(input(f"How many days did {name1} stay in the house: "))
car_usage1 = int(input(f"How many times in a month do you use your car {name1}?: "))
name2 =input("What is the name of other roommate?: ")
DaysInHouse2 = int(input(f"How many days did {name2} stay in the house: "))
car_usage2 = int(input(f"How many times in a month do you use your car {name2}?: "))
'''
amount  = float(200)
car = float(155)

name1 ="D"
DaysInHouse1 = int(30)
car_usage1 = int(20)
name2 ="S"
DaysInHouse2 = int(20)
car_usage2 = int(5)
'''
the_bill = Bill(amount,car)

roommate1 = Roommate(name1, DaysInHouse1,car_usage1)
roommate2 = Roommate(name2, DaysInHouse2,car_usage2)

print(f"{roommate1.name} pays: ", roommate1.pays(the_bill, roommate2))
print(f"{roommate2.name} pays: ", roommate2.pays(the_bill, roommate1))

pdf_report = PdfReport(filename=f"{the_bill.car}.pdf")
pdf_report.generate(roommate1, roommate2, the_bill)

file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())