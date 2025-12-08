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
        self.size = size

    def __str__(self):
        if self.n > 0:
            result = '[ '

            for i in range(self.n):
                result += (str(self.A[i]) + ", ")

            result = result[:-2] + ' ]'
        
        else:
            result = '[]'
        
        return result
    
    def __getitem__(self, index:int):
        if (-1*self.n) <= index < 0:
            return self.A[index + self.n]
        elif 0 <= index < self.n:
            return self.A[index]
        raise IndexError(f"Index out of range!")
    
    def pop(self):
        item = self.A[self.n-1]

        self.A[self.n - 1] = None
        self.n -= 1

        print(item)

    def clear(self):
        self.n = 0
        self.size = 1
    
    def index(self, item):
        for i in range(self.n):
            print(f'{self.A[i]} and {item}')
            if self.A[i] == item:
                return i
        raise ValueError(f"Item not found!")
    
    def insert(self, pos, item):
        if self.n == self.size:
            self.__reassign(pos, item, True)
        else:
            self.__reassign(pos, item)
        self.n += 1

    def __reassign(self, pos, item, new_list = False):
        if new_list:
            B = self.__create_list(self.size + 8)
            self.size += 8
            j = 0 # Index for B
            for i in range(self.n):
                if i == pos:
                    B[j] = item
                    B[j+1] = self.A[i]
                    j += 1    
                else:
                    B[j] = self.A[i]
                j += 1
            self.A = B
        
        else:
            for i in range(self.n, pos, -1):
                self.A[i] = self.A[i - 1]
            self.A[pos] = item

# 10. delete [D]
# 11. remove [D]

# sort/min/max/sum
# extend
# slicing
# Merge

# use
L = ThunderList()

L.append(8)
L.append('Hello')
L.append('World')
L.append(True)
L.append(3.14)
L.append('a')
L.append('b')
L.append('c')
L.append('d')

print(L)
L.insert(1, 200)
print(L)
L.insert(1, 100)
print(L)