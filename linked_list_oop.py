class StackObj:

    def __init__(self, data) -> None:
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        if isinstance(next, StackObj) or next is None:
            self.__next = next


class Stack:

    def __init__(self) -> None:
        self.top = None

    def push(self, obj):
        if not self.top:
            self.top = obj
        else:
            n = self.top
            while n is not None:
                if n.next is None:
                    n.next = obj
                    break
                n = n.next

    def pop(self):
        n = self.top
        prev_obj = None
        while n is not None:
            if self.top.next is None:
                self.top = None
            elif n.next is None and n != self.top:
                prev_obj.next = None
                break
            else:
                prev_obj = n
            n = n.next

    def get_data(self):
        obj_list = []
        n = self.top
        while n is not None:
            if n.next is None and n != self.top:
                obj_list.append(n.data)
                break
            obj_list.append(n.data)
            n = n.next
        return obj_list


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
# st.pop()
# st.pop()
res = st.get_data()    # ['obj1', 'obj2']
print(res)
