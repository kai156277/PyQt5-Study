from PyQt5.QtCore import QDate, Qt

p1 = QDate(1996, 4, 2)
p2 = QDate(1994, 6, 13)

dayspassed = p1.daysTo(p2)

print("{0} days have passed since {1} to {2}".format(dayspassed, p1.toString(Qt.ISODate), p2.toString(Qt.ISODate)))