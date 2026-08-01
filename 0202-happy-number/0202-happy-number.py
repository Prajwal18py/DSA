class Solution:
    def isHappy(self, n: int) -> bool:
        def func(n):
            s = 0
            while n > 0:
                d = n % 10
                s += d*d
                n //= 10
            return s
        
        slow,fast = n,n
        while True:
            slow = func(slow)
            fast = func(func(fast))

            if slow == fast:
                break
        return slow == 1
        