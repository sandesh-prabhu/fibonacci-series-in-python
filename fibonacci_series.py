while 1:
    def fib(n):
        if n==0 or n==1:
            return n
        else:
            return fib(n-1)+fib(n-2)
    num=input("Enter positive number(number of terms)(enter nothing to quit):")
    if num=="":
        break
    elif not num.isnumeric() or int(num)<0:
        print("enter a positive integer")
    elif num=="":
        break
    else:
        print("Fibonacci series:")
        for i in range(int(num)):
            print(fib(i));
