while True:
    a= input( "enter your name ")
    b=a.split()


    for i in b:
        c= (i[0].upper() + i[1:-1].lower()+i[-1].upper())
        print(c)
