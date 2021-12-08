# we are dividing until correct data is given
executed = False
while not executed:
    try:
        a = float(input('first number --> '))
        b = float(input('second number --> '))
        z = a / b
        print(z)
        executed = True
    except ZeroDivisionError as ZeroDivisionError:
        print(ZeroDivisionError)
    except ValueError as valueError:
        print(valueError)
    except Exception as exception:
        print(exception)