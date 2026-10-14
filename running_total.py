def running_total():
       total = 0
       while True:
                Number = input("Enter a number:")
                if Number == "0":
                        break 
                else:
                        total += int(Number)
                        print (total)
running_total() 