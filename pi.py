from math import pi
if __name__ == "__main__":
    while True:
        n = int(input("Please enter numeric value below 48 \n"))
        try:
            if n > 48:
                raise Exception("Please enter below 48 \n")
            if n < 0:
                raise Exception("Please enter positive value \n")
            break
        except ValueError as error:
            print ("Please enter numeric value \n")
        except Exception as e:
            print (e)
print ('{:.{prec}f}'.format(pi, prec=n))