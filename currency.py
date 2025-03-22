#Currency

curr_p = int(input("Enter the price of hat in pesos: "))
curr_d = int(input("Enter the price of hat in dollars: "))

#0.02 $ = 1 pesos
#    x    $ =  y pesos
# therefore, y = x/0.02

curr_p2 = curr_d /0.02

if (curr_p  > curr_p2):
    print("Dollars.")
elif (curr_p == curr_p2):
    print("The prices are the same. Either can be used.")
else:
    print("Pesos")




