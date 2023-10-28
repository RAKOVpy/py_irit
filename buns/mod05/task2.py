class Queue:
    class _Node:
        def __init__(self, element, prev_link=None, next_link=None):
            self.element = element
            self.next_link = next_link
            self.prev_link = prev_link

    __head = None
    __tail = None
    __lenght = 0

    def pop(self):
        self.__lenght -= 1
        node = self.__head
        if not node:
            raise Exception('No Elements')
        if not self.__tail:
            del self.__head
            return node.element
        if self.__lenght == 2 - 1:
            self.__head = self.__tail
            self.__head.prev_link = None
            del self.__tail
            return node.element

        self.__head = self.__head.next_link
        self.__head.prev_link = None
        return node.element

    def push(self, element):
        self.__lenght += 1
        if not self.__head:
            self.__head = self._Node(element)
            return element
        if not self.__tail:
            self.__tail = self._Node(element, self.__head)
            self.__head.next_link = self.__tail
            return element
        self.__tail = self._Node(element, self.__tail)
        self.__tail.prev_link.next_link = self.__tail
        return element

    def insert(self, index, element):
        node = self.__head
        i = 0
        if index < 0:
            raise Exception('Queue Index Out Of Range')
        while i < index:
            if not node.next_link:
                raise Exception('Queue Index Out Of Range')
            node = node.next_link
            i += 1

        node.element = element
        return element

    def print(self):
        node = self.__head
        if not node:
            raise Exception('No Elements')
        while node.next_link:
            print(node.element)
            node = node.next_link
        print(node.element)
