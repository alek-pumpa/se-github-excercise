while True:
    try:
        age = int(input("How old are you? "))
        calc = 100 / age
        print(calc)
    except:
        print("Please enter a number!")
    else:
        print('Your input has been varified! Thank you!')
        break