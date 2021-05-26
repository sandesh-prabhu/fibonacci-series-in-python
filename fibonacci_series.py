while 1:
    def fib(n):
        if n==0 or n==1:
            return n
        else:
            return fib(n-1)+fib(n-2)
    num=input("Enter a positve number(number of terms)(enter nothing to quit):")
    if num=="":
        print("Have a good day!")
        break
    elif not num.isnumeric() or int(num)<0:
        print("enter a positive integer")
    else:
        print("Fibonacci series:")
        [print(fib(i)) for i in range(int(num))]
