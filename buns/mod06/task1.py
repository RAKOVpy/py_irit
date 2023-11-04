class LinkedList:
    class _Node:
        def __init__(self, val, link=None):
            self.val = val
            self.link = link

    __head = None
    __length = 0

    def push(self, val):
        self.__length += 1
        node = self.__head
        if not node:
            self.__head = self._Node(val)
            return val

        while node.link:
            node = node.link

        node.link = self._Node(val)
        return val

    def get(self, index):
        if index >= self.__length or index < 0:
            raise Exception('LinkedList Index Out Of Range')
        node = self.__head
        i = 0
        while i < index:
            node = node.link
            i += 1
        return node.val

    def remove(self, index):
        if index >= self.__length or index < 0:
            raise Exception('LinkedList Index Out Of Range')
        self.__length -= 1
        node = self.__head
        if index == 0:
            if not node.link:
                self.__head = None
                return node.val
            self.__head = self.__head.link
            return node.val

        prev_node = node
        i = 0
        while i < index:
            prev_node = node
            node = node.link
            i += 1
        next_node = node.link
        prev_node.link = next_node
        return node.val

    def insert(self, n, val):
        if n >= self.__length or n <= 0 or self.__length < 2:
            raise Exception('LinkedList Index Out Of Range')
        self.__length += 1
        node = self.__head
        prev_node = node
        i = 0
        while i < n:
            prev_node = node
            node = node.link
            i += 1

        new_node = self._Node(val, node)
        prev_node.link = new_node

        return val

    def __iter__(self):
        self.iter_element = self.__head
        return self

    def __next__(self):
        x = self.iter_element
        if not x:
            raise StopIteration
        self.iter_element = self.iter_element.link
        return x.val
