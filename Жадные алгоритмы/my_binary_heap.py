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

    def insert(self, x):
        self.max_heap.append(x)
        self.heap_size = len(self.max_heap)
        self.sift_up(self.heap_size - 1)

    def extract_max(self):
        root = self.max_heap[0]
        self.max_heap[0] = self.max_heap.pop()
        self.heap_size = len(self.max_heap)
        self.sift_down(0)
        return root

    def sift_up(self, i: int):
        while 0 < i < self.heap_size:
            parent = (i - 1) // 2
            if self.max_heap[i] > self.max_heap[parent]:
                self.max_heap[i], self.max_heap[parent] = self.max_heap[parent], self.max_heap[i]
                i = parent
            else:
                break

    def sift_down(self, i: int):
        while 0 <= i < self.heap_size:
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            if left_child < self.heap_size and self.max_heap[i] < self.max_heap[left_child]:
                self.max_heap[i], self.max_heap[left_child] = self.max_heap[left_child], self.max_heap[i]
                i = left_child
            elif right_child < self.heap_size and self.max_heap[i] < self.max_heap[right_child]:
                self.max_heap[i], self.max_heap[right_child] = self.max_heap[right_child], self.max_heap[i]
                i = right_child
            else:
                break


if __name__ == '__main__':
    a = MyBinaryHeap()
    a.insert(3)
    a.insert(6)
    a.insert(4)
    a.insert(9)
    a.insert(8)
    a.insert(12)
    a.insert(7)
    a.insert(11)
    a.insert(9)
    print(a.max_heap)
    print(a.extract_max())
    print(a.max_heap)