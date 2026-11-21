class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None] * self.capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() >= self.capacity:
            self.resize()

        end_index = self.size
        self.arr[end_index] = n
        self.size += 1

    def popback(self) -> int:
        last_index = self.size - 1
        value = self.arr[last_index]
        self.size -= 1
        self.arr[last_index] = None
        return value

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_arr = [None] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]
        
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
