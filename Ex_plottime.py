import matplotlib.pyplot as plt
import time as t

times=[]
mistakes=0

print("This program will help you to type fast, type 'programming' as fast as you can for five time")
input('press enter to begin')

while len(times)<5:
    start=t.time()
    word=input('type the word: ')
    end=t.time()
    time_elapsed=end-start

    times.append(time_elapsed)

    if (word.lower()!= 'programming'):
        mistakes += 1

print('you made'+ str(mistakes)+'mistakes')
print('now lets see your evalution')
t.sleep(3)

x=[1,2,3,4,5]
y=times
plt.plot(x,y)
plt.show()

    
