# nested loop is which inside in exiting for loop is know as for loop
# nested loops = The "inner loop" will finish all of it;s iteration before finishing one iteration
# of the " outer loop"

rows = int(input('How many row: '))
column = int(input('how many column: '))
symbol = input("Enter a symbo to use: ")

for i in range(rows):
    for j in range(column):
         print(symbol, end = "")# this decide the ending point the symbol to stop
    print() #soo this use to print the Column

#today we stop at 1:17:19
#relearning this 
