class DoubleElement:
    def __init__(self, *lst):
        if len(lst) % 2 != 0:
            self.elemens = list(lst)
            self.elemens.append(None)
            self.elemens = tuple(self.elemens)
        else:
            self.elemens = lst

    def __next__(self):
        x = self.iter_element

        if self.i == len(self.elemens) // 2:
            raise StopIteration
        self.i += 1
        self.iter_element = self.elemens[2 * self.i:2 * (self.i + 1)]

        return x

    def __iter__(self):
        self.i = 0
        self.iter_element = self.elemens[:2]
        return self


dL = DoubleElement(1, 2, 3, 4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1, 2, 3, 4, 5)
for pair in dL:
    print(pair)
