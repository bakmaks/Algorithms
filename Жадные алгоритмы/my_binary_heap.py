# Задача на программирование: очередь с приоритетами.
#
# Первая строка входа содержит число операций 1 <= n <= 10^5.
# Каждая из последующих nn строк задают операцию одного из следующих двух типов:
# Insert x, где 0 <= x <= 10^9  — целое число;
# ExtractMax.
# Первая операция добавляет число x в очередь с приоритетами,
# вторая — извлекает максимальное число и выводит его.


class MyMaxBinaryHeap:
    """
    # Куча с максимумом в корне.
    """
    max_heap = []
    heap_size = 0

    def get_max_heap(self):
        """Возвращает список содержащий кучу"""
        return self.max_heap

    def insert(self, x):
        """Вставляет элемент в кучу"""
        self.max_heap.append(x)
        self.heap_size = len(self.max_heap)
        # Исправление кучи вверх
        self.sift_up(self.heap_size - 1)

    def extract_max(self):
        """Метод извлекает корневой элемент(самый большой)"""
        if self.heap_size > 1:
            root = self.max_heap[0]
            # Извлечение последнего элемента т. к. он явно меньше корневого
            # и замена им корневого элемента
            self.max_heap[0] = self.max_heap.pop()
            self.heap_size = len(self.max_heap)
            # Исправление кучи вниз
            self.sift_down()
        elif self.heap_size == 1:
            root = self.max_heap.pop()
            self.heap_size = len(self.max_heap)
        else:
            root = 0
        return root

    def sift_up(self, i: int):
        """
        Метод исправляет кучу вверх, т. е. если родитель элемента меньше самого элемента,
        они меняются местами. Элемент поднимается вверх на место родителя.
        :param i: Позиция с которой начинается исправление
        """
        while 0 < i < self.heap_size:
            parent = (i - 1) // 2
            if self.max_heap[i] > self.max_heap[parent]:
                self.max_heap[i], self.max_heap[parent] = self.max_heap[parent], self.max_heap[i]
                i = parent
            else:
                break

    def sift_down(self, i: int = 0):
        """
        Метод исправляет кучу вниз. Если дети элемента больше, то выбирается наибольший из них
        и элемент опускается на место ребёнка, а ребёнок соответсвенно поднимается на верх
        :param i: Позиция с которой начинается исправление
        :return:
        """
        while 0 <= i < self.heap_size:
            # позиция левого ребёнка
            left_child = 2 * i + 1
            # позиция правого ребёнка
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
    a = MyMaxBinaryHeap()
    print('Тест кучи.')
    in_range = int(input('Введите длину списка: '))
    step = int(input('Введите шаг проверки работы кучи: '))
    x = [i for i in range(in_range)]
    rnd.shuffle(x)
    print(x)
    print('Длина списка')
    print(len(x))
    i = 0
    old_i = 0
    for el in x:
        a.insert(el)
        i += 1
        if i == old_i + step:
            print('КУЧА:')
            print(a.get_max_heap())
            print('Максимальный эл. max(эл.):')
            max_el = max(a.get_max_heap())
            print(max_el)
            print('Макасимальный эл. extract_max(эл.): ')
            max_ex_el = a.extract_max()
            print(max_ex_el)
            if max_el != max_ex_el:
                print('ОШИБКА! На i-том шаге.')
                print('i = ', i)
                print('Эл. полученный с помощью ф. max() не равен эл. из ф. extract_max()')
                print(f'max_el = %s, max_ex_el %s ' % (max_el, max_ex_el))
                break
            else:
                print('Ok')
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
    # a.get_max_heap()
    # a.extract_max()
    # a.get_max_heap()
    # a.extract_max()
    # a.get_max_heap()
    # a.insert(250)
    # a.get_max_heap()

