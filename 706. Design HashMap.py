class MyHashMap:

    def __init__(self):
        self.dict = dict()

    def put(self, key: int, value: int) -> None:
        self.dict[key] = value

    def get(self, key: int) -> int:
        try:
            if self.dict[key]:
                return self.dict[key]
        except:
            return -1 
        

    def remove(self, key: int) -> None:
        try:
            del self.dict[key]
        except:
            pass

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)