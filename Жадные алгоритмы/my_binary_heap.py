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

    def get(self):
        # print(self.max_heap)
        return self.max_heap

    def insert(self, x):
        self.max_heap.append(x)
        self.heap_size = len(self.max_heap)
        self.sift_up(self.heap_size - 1)

    def extract_max(self):
        if self.heap_size > 1:
            root = self.max_heap[0]
            self.max_heap[0] = self.max_heap.pop()
            self.heap_size = len(self.max_heap)
            self.sift_down()
        elif self.heap_size == 1:
            root = self.max_heap.pop()
            self.heap_size = len(self.max_heap)
        else:
            root = 0
        # print(root)
        return root

    def sift_up(self, i: int):
        while 0 < i < self.heap_size:
            parent = (i - 1) // 2
            if self.max_heap[i] > self.max_heap[parent]:
                self.max_heap[i], self.max_heap[parent] = self.max_heap[parent], self.max_heap[i]
                i = parent
            else:
                break

    def sift_down(self, i: int = 0):
        while 0 <= i < self.heap_size:
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            if right_child < self.heap_size:
                if self.max_heap[left_child] > self.max_heap[right_child]:
                    if self.max_heap[i] < self.max_heap[left_child]:
                        self.max_heap[i], self.max_heap[left_child] = self.max_heap[left_child], self.max_heap[i]
                        i = left_child
                    else:
                        break
                else:
                    if self.max_heap[i] < self.max_heap[right_child]:
                        self.max_heap[i], self.max_heap[right_child] = self.max_heap[right_child], self.max_heap[i]
                        i = right_child
                    else:
                        break
            elif left_child < self.heap_size:
                if self.max_heap[i] < self.max_heap[left_child]:
                    self.max_heap[i], self.max_heap[left_child] = self.max_heap[left_child], self.max_heap[i]
                    i = left_child
                else:
                    break
            else:
                break



if __name__ == '__main__':
    import random as rnd
    a = MyBinaryHeap()
    in_range = int(input('Введите диапазон: '))
    step = int(input('Введите шаг: '))
    x = [i for i in range(in_range)]
    rnd.shuffle(x)
    print(x)
    print(len(x))
    i = 0
    old_i = 0
    flag = True
    for el in x:
        a.insert(el)
        i += 1
        if i == old_i + step:
            max_el = max(a.get())
            max_ex_el = a.extract_max()
            if max_el != max_ex_el:
                flag = False
                print('i = ', i)
                print(f'max_el = %s, max_ex_el %s ' % (max_el, max_ex_el))
                break
            old_i = i


    # a.insert(50)
    # a.insert(6)
    # a.insert(100)
    # a.insert(9)
    # a.insert(20)
    # a.insert(200)
    # a.insert(201)
    # a.insert(150)
    # a.insert(45)
    # a.get()
    # a.extract_max()
    # a.get()
    # a.extract_max()
    # a.get()
    # a.insert(250)
    # a.get()

