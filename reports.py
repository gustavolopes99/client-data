from modules import *


class Reports():
    def printCustomer(self):
        webbrowser.open("report.pdf")

    def generate_report(self):
        self.c = canvas.Canvas("report.pdf")
        self.codRep = self.cod_entry.get()
        self.nameRep = self.name_entry.get()
        self.phoneRep = self.phone_entry.get()
        self.cityRep = self.city_entry.get()

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, 'Customer File')

        self.c.setFont("Helvetica-Bold", 12)
        self.c.drawString(50, 700, "Cod: " + self.codRep)
        self.c.drawString(50, 680, "Name: " + self.nameRep)
        self.c.drawString(50, 660, "Phone: " + self.phoneRep)
        self.c.drawString(50, 640, "City: " + self.cityRep)

        self.c.rect(20, 550, 550, 5, fill=True, stroke=False)

        self.c.showPage()
        self.c.save()
        self.printCustomer()
