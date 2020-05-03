data_valid= False
while data_valid==False:
    grade1=float(input('Enter the first grade:'))
    if grade1<0 or grade1>10:
        print('The grade should be between 0 and 10')
        continue
    else:
        data_valid=True

data_valid= False        
while data_valid==False:
    grade2=float(input('Enter the second grade:'))
    if grade2<0 or grade2>10:
        print('The grade should be between 0 and 10')
        continue
    else:
        data_valid=True

data_valid= False
while data_valid==False:
    Total_class=int(input('The total number of class?'))
    if Total_class <= 0:
        print('the total number of class cant be 0 or less')
        continue
    else:
        data_valid=True
        

data_valid= False
while data_valid==False:
    ab_num=int(input('How many abcences does he?'))
    if ab_num<0 or ab_num>Total_class:
        print('the absence number should be in range of total class')
        continue
    else:
        data_valid=True
        
 


avg=(grade1+grade2)/2
attendence=(Total_class-ab_num)/Total_class

print('average is:',avg)
print('rate of attendency is:',attendence*100,'%')

if(avg >= 6):
    if(attendence >= 0.8):
        print('student has been approved')
    else:
        print('student has faild due to attendance rate')
elif(attendence >= 0.8):
    print('student has faild due to the average is lower than 6')
else:
    print('student has failed due to average and attendancy rate')
            
