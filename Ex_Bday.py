
months=('Jan','Feb','March','April','May','June','July','Augest','September','October','November','December')
b_date=input('Enter your birthday in format DD-MM-YYYY:')

index=int(b_date[3:5])-1
b_month=months[index]
print('your birthday is on',b_month)
