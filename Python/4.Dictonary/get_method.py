while True:
    x=input("please enter your choice of pizza")
    #dict={"key1":'value1',"key2":'value2'}
    menu_pizza={'panpizza':129,'tomato capicum':150,"cheese corn":220}
    #y=d[x] # it will throw error if key is not present
    y=menu_pizza.get(x,"Sry item not available")
    #print(f"price of pizza {x} is Rs {y}")
    print('price is',y)
