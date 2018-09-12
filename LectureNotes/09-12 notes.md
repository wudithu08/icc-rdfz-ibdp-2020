
## Guess and Check
Questions:
how to count a cube root & a square root?
   1.exhaustive(thorough) enumeration
   2.bisection
   3.Newton-Raphson(polynomial)
binary and denary for all real numbers

## exhaustive enumeration to acquire a cube root
x = int(input())
ans = 0
while ans**3 < abs(x):
    ans = ans+1
if ans**3!= abs(x):
    print (x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
        print( 'Cube root of', x,'is', ans)

## square root 
x = 25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans*ans <= x:
    ans += step
    numGuesses += 1
print ('numGuesses =', numGuesses)
if abs(ans**2 - x) >= epsilon:
    print ('Failed on square root of', x)
else:
    print( ans, 'is close to square root of',x)

## import timeit to time the programme
import timeit
start = timeit.timeit()
end = timeit.timeit()
print(end-start)

## disads of exhaustive enumeration
not really applicable to large integers due to its massive time consumption

## logic behind the method
For what values of  x will this program terminate?
The answer is, “all integers.” This can be argued quite simply.
•  The value of the expression  ans**3 starts at  0, and gets larger each time
through the loop.
•  When it reaches or exceeds  abs(x) , the loop terminates.
•  Since  abs(x) is always positive there are only a finite number of
iterations before the loop must terminate.
Whenever you write a loop, you should think about an appropriate
decrementing function. This is a function that has the following properties:
1.It maps a set of program variables into an integer.
2.When the loop is entered, its value is nonnegative.
3.When its value is <=0, the loop terminates.
4.Its value is decreased every time through the loop

## what about strings?
total = 0
for c in '123456789':
    total = total + int(c)
print (total)

## approximate solutions and bisection solutions
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print( 'low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print ('numGuesses =', numGuesses)
print (ans, 'is close to square root of', x)

## homework:
## mit exercise lecture 3
## bisection on cube root
## preview denary and binary
