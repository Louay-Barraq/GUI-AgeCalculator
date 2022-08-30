from cgitb import reset
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QLineEdit
from functions import AgeCalc, Day, Month, Year


def reset():
    windows.DayBox.setValue(Day)
    windows.MonthBox.setValue(Month)
    windows.YearBox.setValue(Year)

    windows.YearsLCD.display(0)
    windows.MonthsLCD.display(0)
    windows.DaysLCD.display(0)
   
def calc():
    yearDate = windows.YearBox.value()
    monthDate =  windows.MonthBox.value()
    dayDate =  windows.DayBox.value()

    (yearRes, monthRes, dayRes) = AgeCalc(yearDate, monthDate, dayDate)

    windows.YearsLCD.display(yearRes)
    windows.MonthsLCD.display(monthRes)
    windows.DaysLCD.display(dayRes)


app = QApplication([])
windows = loadUi('calculator.ui')
windows.show()
windows.btn_1.clicked.connect(calc)
windows.btn_2.clicked.connect(reset)
app.exec_()