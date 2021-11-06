import time

nth_term=1000

start = time.time()
n1,n2=0,1
f=nth_term
for x in range(f-1):
    nth = n1 + n2
    n1=n2
    n2=nth
#print(nth)

example1 = time.time()

series=[0]
new_n1,new_n2 = 0,1
for x in range(100001):
    new_nth = new_n1 + new_n2
    series.append(new_nth)
    new_n1=new_n2
    new_n2=new_nth

def Fibonacci(n,list_fib):
    if n==0:
        Fib=0
    elif n==1 or n==2:
        Fib=1 
    else:
        if n%2==0:
            Fib=list_fib[int(n)]-list_fib[int(n-2)]
        else:
            Fib=list_fib[int(n)]-list_fib[int(n-2)]
    return Fib

#print(Fibonacci(nth_term,series))

example2=time.time()

Final=(1/5**0.5)*(((1+5**0.5)/2)**nth_term-((1-5**0.5)/2)**nth_term)
#print(round(Final))

example3=time.time()

method1=(example1-start)*1000000
method2=(example2-example1)*1000000
method3=(example3-example2)*1000000

times={}
times["Simple Recursion"]=method1
times["If-else Recursion"]=method2
times["Equation/Raw Computation"]=method3

print(min(times,key=times.get))