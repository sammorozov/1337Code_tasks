'''
firstly i want to understand what is lru cache with built in function in python

hmm i think that i need to train to print some text in english

but i will do it later
'''

# from functools import lru_cache


def test():

    # @lru_cache(maxsize=5)
    def test(num):
        res = 0
        for i in range(num):
            res += i
        print('была вызвана')
        return res

    a = test(1000000)
    a = test(1000000)
    a = test(2000000)
    a = test(4000000)
    a = test(3000000)
    a = test(6000000)
    a = test(7000000)
    a = test(9000000)
    # print(test.cache_clear())
    # print(test.cache_info())




class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}
        self.stack = []

    def get(self, key: int) -> int:
        if key in self.data:

            self.stack.remove(key)
            self.stack.append(key)
            return self.data[key]
        else:
            return -1 



    def put(self, key: int, value: int) -> None:
        if len(self.data) >= self.capacity:
            if key in self.data:
                self.stack.remove(key)
                self.data[key] = value
                self.stack.append(key)
            else:
                if self.stack and self.stack[0] in self.data:
                    del self.data[self.stack[0]]
                    self.stack.remove(self.stack[0])
                self.data[key] = value
                self.stack.append(key)
        else:
            self.data[key] = value
            self.stack.append(key)



cache = LRUCache(3)
print(cache.sost())

cache.put(0, 2)
print(cache.sost())


cache.put(1, 3)
print(cache.sost())



cache.put(4, 4)
print(cache.sost())



cache.put(5, 5)
print(cache.sost())



cache.put(5, 6)
print(cache.sost())


'''
class LRUCache:

    def __init__(self, capacity: int):
        self.used = []
        self.cache = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.used.remove(key)
        else:
            return -1
        self.used.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if len(self.cache) >= self.cap and key not in self.cache:
            val = self.used.pop(0)
            if val in self.cache:
                del self.cache[val]
        if key in self.cache:
            self.cache[key] = value
            self.used.remove(key)

        else:
            # self.stack.append(key)
            self.cache[key] = value
        self.used.append(key)


'''

