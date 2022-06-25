class ObjList:
    def __init__(self, data) -> None:
        self.__data = data
        self.__prev = None
        self.__next = None

    def __repr__(self) -> str:
        return self.__data

    @property
    def data(self):
        return self.__data

    @property
    def prev(self):
        return self.__prev
    
    @prev.setter
    def prev(self, obj):
        self.__prev = obj

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, obj):
        self.__next = obj

class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __len__(self):
        obj = self.head

        counter = 1
        while obj.next:
            counter += 1
            obj = obj.next
        return counter

    def __call__(self, indx, *args, **kwargs):
        obj = self.head
        for _ in range(indx):
            obj = obj.next
        return obj.data

    def add_obj(self, obj):
        if not self.head:
            self.head = obj
            self.tail = obj
        else:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj

    def remove_obj(self, indx):
        obj = self.head

        for _ in range(indx):
            obj = obj.next
        if obj.next:
            obj.next.prev = obj.prev
        obj.prev.next = obj.next
        self.tail = obj.prev
        del obj


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Hello"))
linked_lst.add_obj(ObjList("World"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python OOP"))
n = len(linked_lst)  # n = 3
print(n)
s = linked_lst(1) # s = World
print(s)