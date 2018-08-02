from PyQt5.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

print("Locak datetime: ", now.toString(Qt.ISODate))
print("Universal datetime: ", now.toUTC().toString(Qt.ISODate))

print("The offset from UTC is: {0} seconds".format(now.offsetFromUtc()))
print("The offset from UTC is: {0} minutes".format(now.offsetFromUtc() / 60))
print("The offset from UTC is: {0} hours".format(now.offsetFromUtc() / 3600))