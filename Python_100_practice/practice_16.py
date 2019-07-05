import datetime

print (datetime.date.today().strftime('%d/%m/%Y'))

miyazakiBirthDate = datetime.date(1941, 1, 5)
print (miyazakiBirthDate.strftime('%d/%m/%Y'))

miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)
print (miyazakiBirthNextDay.strftime('%d/%m/%Y'))

miyazakiBirthNextDay = miyazakiBirthDate.replace(year = miyazakiBirthDate.year + 1)
print (miyazakiBirthNextDay.strftime('%d/%m/%Y'))
