from flask.views import MethodView
from wtforms import Form , StringField, SubmitField
from flask import Flask
from flask import render_template,request
from bill_app import room


app = Flask(__name__)

class HomePage(MethodView):
    def get(self):
        return render_template('temp.html')  # flask knows that all the html files are in templates folder


class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm() # connecting billform.amount with htlm file
        return render_template('bill_form.html', billform= bill_form)


class ResultsPage(MethodView):
    def post(self):

        billform = BillForm(request.form)
        the_bill = room.Bill(float(billform.amount.data),float(billform.car.data))
        roommate1 = room.Roommate(billform.name1.data, float(billform.DaysInHouse1.data),
                                  float(billform.car_usage1.data))
        roommate2 = room.Roommate(billform.name2.data, float(billform.DaysInHouse2.data),
                                  float(billform.car_usage2.data))

        return render_template('results.html',
                               name1 = roommate1.name, amount1 = roommate1.pays(the_bill,roommate2),
                               name2 = roommate2.name, amount2 = roommate2.pays(the_bill,roommate1)
                               )


class BillForm(Form):

    amount = StringField("How much do you pay apartment per mounth?: ", default= "200")
    car = StringField("If you have a car, how much are you paying per mounth?: ", default= "1")

    name1 = StringField("Name:", default= "Man")
    DaysInHouse1 = StringField("How many days are you in the house? ", default="30")
    car_usage1 = StringField("How many times do you use car per mounth?: ", default= "1")
    name2 = StringField("Name:", default="Woman")
    DaysInHouse2 = StringField("How many days are you in the house? ", default= "30")
    car_usage2 = StringField("How many times do you use car per mounth?: ",default= "1")
    button = SubmitField("Calculate")

app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('result_page'))
app.run()

