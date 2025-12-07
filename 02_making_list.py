import ctypes

class ThunderList:
    def __init__(self):
        self.size = 1
        self.n = 0

        self.A = self.__create_list(self.size)

    def __create_list(self, size):
        return (size*ctypes.py_object)()

    def __len__(self):
        return self.n

    def append(self, item):
        if self.size == self.n:
            self.__resize(self.size + 8)
        
        self.A[self.n] = item
        self.n += 1

    def __resize(self, size):
        B = self.__create_list(size)

        for i in range(self.n):
            B[i] = self.A[i]

        self.A = B

    def __str__(self):
        result = '[ '

        for i in range(self.n):
            result += (str(self.A[i]) + ", ")

        result = result[:-2] + ' ]'

        return result
    
# 5. indexing [D]
# 6. pop [D]
# 7. clear [D]
# 8. find [D]
# 9. insert [D]
# 10. delete [D]
# 11. remove [D]

# sort/min/max/sum
# extend
# negative indexing
# slicing
# Merge

# use
L = ThunderList()

print(len(L))

L.append(8)
L.append('Hello')
L.append('World')
L.append(True)
L.append(3.14)

print(len(L))

print(L)