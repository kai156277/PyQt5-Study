from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

now = QDate.currentDate()

print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))

datetime = QDateTime.currentDateTime()

print(datetime.toString("yyyy-MM-dd hh:mm:ss"))
print(datetime.toString(Qt.DefaultLocaleLongDate))

time = QTime.currentTime()

print(time.toString(Qt.DefaultLocaleLongDate))