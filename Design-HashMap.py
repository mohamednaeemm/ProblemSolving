class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.hashMap = [None] * self.size
    
    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        if self.hashMap[index] is None:
            self.hashMap[index] = []

        for i, (k, v) in enumerate(self.hashMap[index]):
            if k == key:
                self.hashMap[index][i] = [key, value]
                return

        self.hashMap[index].append([key, value]) 

    def get(self, key: int) -> int:
        index = self._hash(key)
        if self.hashMap[index] is None:
            return -1
        for k, v in self.hashMap[index]: 
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        if self.hashMap[index] is None:
            return
        for i, (k, v) in enumerate(self.hashMap[index]):
            if k == key:
                self.hashMap[index].pop(i)
                return
