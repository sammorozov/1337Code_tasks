from typing import *
'''
Given two positive integers left and right, find the two integers num1 and num2 such that:

    left <= nums1 < nums2 <= right .
    nums1 and nums2 are both prime numbers.
    nums2 - nums1 is the minimum amongst all other pairs satisfying the above conditions.

Return the positive integer array ans = [nums1, nums2]. If there are multiple pairs satisfying these conditions, return the one with the minimum nums1 value or [-1, -1] if such numbers do not exist.

A number greater than 1 is called prime if it is only divisible by 1 and itself.

Example 1:

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.

Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.

 

Constraints:

    1 <= left <= right <= 106



class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
'''


'''
first of all we will write a default alhorithm about eratosphene siete.
there will be one number N and we need to write out all prime numbers before the N inclusively
'''

'''
какая ваще логика бля типа есть число, мы можем в тупую проверять делится ли оно на все предыдущие,

скорее всего даже до корня из этого числа, потому что епта больше чем на корень оно делится не может

но мы также можем исключать из рассмотрения уже все кратные нахуй тому числу на которое оно точно не делится

типа 17 не делится на 3 значит автоматом оно уже не делится на 6 нахуй

но если 18 делится на 2 это еще не значит что оно делится на 8 например вот блять

ну и типа удаляем по индексу элементы вспомогательного массива

нашли, что оно не делится на 2 удаляем нахуй все четные

нашли, что оно не делится на 3 удаляем все кратные трём, вплоть до корня из n 

то есть бежим по вспомогательному массиву если число делится на k то удаляем k, 2k, 3k, ...

потом берем следующий делитель, и обновляем вспомогательный массив, если мы дошли до корня из н и нихуя не удалили, значит число
точно простое

так... а нам надо было от нуля до н вывести все простые

короче наверное как-то так


'''

def prime_numbers(N):

    primes = []
    nums = [i for i in range(N+1)]

    for i in range(2, int((len(nums))**(1/2)) + 1):

        for j in range(len(nums)):

            if nums[j] % i == 0:
                nums[j] = 0

            else:
                continue

    for num in nums:
        if num != 0:
            primes.append(num)

    primes.remove(1)
    primes = [2] + primes
 

    return primes

# print(prime_numbers(34))


def is_prime(N):

    if N in prime_numbers(N):
        return True
    else:
        return False
    
# print(is_prime(11))


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:


        primes = []
        nums = [i for i in range(right + 1)]


        for i in range(2, int((len(nums))**(1/2)) + 1):

            for j in range(len(nums)):

                if nums[j] % i == 0:
                    nums[j] = 0

                else:
                    continue

        for num in nums:
            if num != 0:
                primes.append(num)

        if 1 in primes:
            primes.remove(1)
        if 2 not in primes:
            primes = [2] + primes

        for i in range(len(primes)):
            if primes[i] >= left:
                primes = primes[i::]
                break

        find_min = float('inf')

        if len(primes) == 1:
            return [-1, -1]
        
        for i in range(len(primes)-1):

            if primes[i+1] - primes[i] < find_min:
                find_min = primes[i+1] - primes[i]
                first_out = primes[i]
                last_out = primes[i+1]


        return [first_out, last_out]


print(Solution().closestPrimes(4, 6))

            
'''
смысл кода такой же. просто есть ускорение на while, я считаю это дроч полный
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(n):
            if n < 2: return False
            for x in range(2, int(n**0.5) + 1):
                if n % x == 0:
                    return False
            return True
        q = []
        diff = float('inf')
        pair = [-1,-1]
        for i in range(left,right+1):
            if isPrime(i): 
                q.append(i)
            while len(q)>=2:
                if abs(q[0]-q[1])<diff:
                    pair=[q[0],q[1]]
                    diff=abs(q[0]-q[1])  
                    if diff<=2: return pair
                q.pop(0)
        return pair
'''
                
