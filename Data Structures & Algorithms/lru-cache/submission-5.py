class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = None
        self.dic = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dic:
            val = self.dic[key]
            linked_list = self.cache

            if linked_list.key==key:
                right = linked_list.next
                if right:
                    self.cache = right
                    right.prev = None
                    node_left = right
                else:
                    return val
            else:
                while linked_list.key!=key:
                    linked_list = linked_list.next
                left = linked_list.prev
                right = linked_list.next

                left.next = right
                if right:
                    right.prev = left
                node_left = left

            while node_left.next:
                node_left = node_left.next
        
            node_left.next = Node(key,val)
            node_left.next.prev = node_left

            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key] = value
            linked_list = self.cache
            if linked_list.key==key:
                right = linked_list.next
                if right:
                    self.cache = right
                    right.prev = None
                    node_left = right
                else:
                    node_left = None 
            else:
                while linked_list.key!=key:
                    linked_list = linked_list.next
                left = linked_list.prev
                right = linked_list.next

                left.next = right
                if right:
                    right.prev = left
                node_left = left
            if node_left:
                while node_left.next:
                    node_left = node_left.next
                node_left.next = Node(key,value)
                node_left.next.prev = node_left
        else:
            self.dic[key] = value
            node_left = self.cache
            if node_left:
                while node_left.next:
                    node_left = node_left.next
                node_left.next = Node(key,value)
                node_left.next.prev = node_left
            else:
                self.cache = Node(key,value)
        if self.capacity<len(self.dic):
            k = self.cache.key
            self.cache = self.cache.next
            self.cache.prev = None
            del self.dic[k]
