# Задача на программирование: очередь с приоритетами.
#
# Первая строка входа содержит число операций 1 <= n <= 10^5.
# Каждая из последующих nn строк задают операцию одного из следующих двух типов:
# Insert x, где 0 <= x <= 10^9  — целое число;
# ExtractMax.
# Первая операция добавляет число x в очередь с приоритетами,
# вторая — извлекает максимальное число и выводит его.


class MyBinaryHeap:
    max_heap = []   # Куча с максимумом в корне.
    heap_size = 0
    index = 0

    def insert(self, x):
        self.max_heap.append(x)
        self.heap_size = len(self.max_heap)
        self.index = self.heap_size - 1
        self.siftup(self.index)

    def extract_max(self):
        return self.max_heap[self.index]

    def siftup(self, i: int):
        while 0 < i < self.heap_size:
            parent = (i - 1) // 2
            if self.max_heap[i] > self.max_heap[parent]:
                self.max_heap[i], self.max_heap[parent] = self.max_heap[parent], self.max_heap[i]
                i = parent
            else:
                break



if __name__ == '__main__':
    a = MyBinaryHeap()
    a.insert(20)
    a.insert(100)
    a.insert(200)
    a.insert(50)
    a.insert(101)
    a.insert(65)
    a.insert(201)
    a.insert(180)
    print(a.max_heap)