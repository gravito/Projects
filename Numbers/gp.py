def isPrime(x):
    if x == 1 or 2:
        return True
    elif x%2 == 0:
        return False
    else:
        for i in range(3,int(x/2)+1,2):
            if x%i == 0:
                return False
    return True

if __name__ == "__main__":
    choice = "y"
    while True:
        try:
            n = int(input("Please enter positive value from where to begin finding Prime number \n"))
            if n <= 0:
                raise Exception("Please enter positive value \n")
            break
        except ValueError:
            print ("Please enter numeric value \n")
        except Exception as e:
            print (e)
    n += 1
    while choice.lower() == "y":
        if isPrime(n):
            print ("Next prime number is: %d" % n)
            choice = input("Do you want to continue? y/n? \n")
        n += 1
    print ("Bye, have a beautiful day :)")
        
        