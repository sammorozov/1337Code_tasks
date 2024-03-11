'''
ЭТОТ КОД НАГЛО СПИЗЖЕН Я НЕ ПОНИМАЮ ЗАЧЕМ ТАКИЕ ЗАДАЧИ
'''


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # want O(1) access to best-rated item for each cuisine, lex smallest tie-break: max heap
        #   (or min heap by (-rating, name))
        
        # want to be able to change ratings, despite using a heap: tombstone dictionary?
        #    > have a heap for each cuisine
        #    > also have a new rating for each cuisine not yet applied to the queue
        #       > while the top item in the heap has a pending change, clear that change from the dictionary
        #         and requeue it.
        
        self.f2c = {} # food -> cuisine
        self.heaps = defaultdict(list) # cuisine -> min heap of (-rating, food)
        self.ratings = {} # food -> current rating; used to evict stale values from heaps

        for f, c, r in zip(foods, cuisines, ratings):
            self.f2c[f] = c
            self.heaps[c].append((-r, f))
            self.ratings[f] = r

        for h in self.heaps.values():
            heapify(h)

    def __applyChanges(self, cuisine) -> None:
        heap = self.heaps[cuisine]

        while (food := heap[0][1]) in self.ratings and self.ratings[food] != -heap[0][0]:
            heapreplace(heap, (-self.ratings[food], food)) # replace (-oldRating, food) with (newRating, food)


    def changeRating(self, food: str, newRating: int) -> None:
        if self.ratings[food] == newRating: return

        self.ratings[food] = newRating
        cuisine = self.f2c[food]
        heappush(self.heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        self.__applyChanges(cuisine)
        return self.heaps[cuisine][0][1] # heap[0] is top (-rating, food)
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)