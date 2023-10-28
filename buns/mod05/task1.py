class Stack:
    class _Node:
        def __init__(self, element, link=None):
            self.element = element
            self.link = link

    __head = None
    __length = 0

    def pop(self):
        self.__length -= 1
        node = self.__head
        prev_node = node
        if not node:
            raise Exception('No Elements')
        if node.link:
            while node.link:
                prev_node = node
                node = node.link
        else:
            del self.__head
        prev_node.link = None
        return node.element

    def push(self, element):
        self.__length += 1
        node = self.__head
        if not node:
            self.__head = self._Node(element)
            return element

        while node.link:
            node = node.link

        node.link = self._Node(element)
        return element

    def print(self):
        node = self.__head
        if not node:
            raise Exception('No Elements')
        while node.link:
            print(node.element)
            node = node.link
        print(node.element)
