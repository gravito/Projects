def fib(f1,f2):
    return (f1 + f2)

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Please enter positive value \n"))
            if n <= 0:
                raise Exception("Please enter positive value \n")
            break
        except ValueError:
            print ("Please enter numeric value \n")
        except Exception as e:
            print (e)

f = [1,1,0]

if n <= 2:
    print (1)
else:
    for i in range(2,n):
        f[2] = fib(f[0],f[1])
        f[0] = f[1]
        f[1] = f[2]
    print(f[2])
