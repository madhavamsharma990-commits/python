list1 = [10 , 20 , 30 , 40]
list2 = [100 , 200 , 300 , 400]
for x , y in zip(list1 , list2):
    print(x , y)
stocks = ['reliance' , 'infosys' , 'tes' ]
prices = [2275 , 3327 , 3750 ]
new_dict = {stock:price for stock, price in zip(stocks , prices)}
print('\n{}' .format(new_dict))