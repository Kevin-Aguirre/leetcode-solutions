# Largest Prime Factor

* Problem #3
* Difficulty rating: 5%
* https://projecteuler.net/problem=3

## Solution

Just by looking at the size of 600851475143, it was obvious that a naive approach to checking for factors, such as 

```python3
primes = []
n = 600851475143
for i in range(2, n):
    if (n // i == 0 and isPrime(i)):
        primes.append(i)
return max(primes)
```

would not work based on Project Euler's rule that solution can typically be found within a minute. 
This made it clear I would be using the square root of the number.

```python3
for i in range(2, sq_n):
    if n % i == 0: 
        prime_factors.append(i)
        prime_factors.append(n // i)
        break 
```

I knew that as soon as I found a prime number, in this case i, I would want to start the for loop again. 
The question is how many times do I run this for loop? I decided to keep track by dividing n by the prime 
factors I came across. I also realized that I would have to check if n // i is prime. (Consider prime factors of 8; 8 / 2 = 4 but 4 is not prime).

```python3
while (n > sq_n):
        for i in range(2, sq_n):
            if n % i == 0: 
                prime_factors.append(i)
                if isPrime(n // i):
                    prime_factors.append(n // i)
                n //= i 
                break 
```

After implementing a simple isPrime function, all I had to do was return max(prime_factors) at the end 