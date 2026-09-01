class MyHashMap:

    def __init__(self):
        self.key_list = []
        self.val_list = []

    def put(self, key: int, value: int) -> None:
        if not key in self.key_list:
            self.key_list.append(key)
            self.val_list.append(value)
        else:
            i = 0
            while self.key_list[i] != key:
                i+=1
            self.val_list[i] = value

    def get(self, key: int) -> int:
        
        if not key in self.key_list:
            return -1
        else:
            i = 0
            while self.key_list[i] != key:
                i+=1
            return self.val_list[i]

    def remove(self, key: int) -> None:
        if key in self.key_list:
            i = 0
            while self.key_list[i] != key:
                i+=1
            del self.key_list[i]
            del self.val_list[i]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)