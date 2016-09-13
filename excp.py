
while True:
    try:
        inp = int(input("Enter a number \n"))
        final = inp/2
        print(final)
        break
    except ValueError:
        print("Enter a  valid number \n")
    except:
        break