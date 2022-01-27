import webbrowser
import os

from filestack import Client
from fpdf import FPDF

'''
PDF file that contains the information about Roommates 
'''
class PdfReport:
    def __init__(self,filename):
        self.filename = filename
    def generate(self, roommate1, roommate2, bill):

        roommate1_pay = str(round(roommate1.pays(bill, roommate2),2 ))
        roommate2_pay = str(round(roommate2.pays(bill, roommate1),2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # add incon
        pdf.image("pic/maja.jpg", w=60, h=60)
        # title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="It's time to pay your bills Majo", border=0, align="C", ln=1)
        # Insert Period label and value
        pdf.set_font(family="Times", size=14, style='B')


        # Insert name and due amount of the first Rommate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h= 25, txt= roommate1.name, border= 0)
        pdf.cell(w=100, h=25, txt=roommate1_pay, border=0, ln=1)
        # Insert name and due amount of the second Roomate
        pdf.cell(w=100, h=25, txt=roommate2.name, border=0)
        pdf.cell(w=100, h=25, txt=roommate2_pay, border=0, ln=1)

        # Change directory to pic, generate and open the PDF
        os.chdir("pic")
        pdf.output(self.filename)
        webbrowser.open(self.filename)

class FileSharer:

    def __init__(self, filepath, api_key="AViVqp7suSQWWEdrl6hf9z"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url