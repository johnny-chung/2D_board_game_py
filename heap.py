# Main Author: Wai Yin Chung
# Main Reviewer:

class Heap:

    # initial with min heap
    def __init__(self, arr=[]):
        self.arr = []
        for elem in arr:
            self.arr.append(elem)
        if len(self.arr) > 0:
            self.heapify_min()

    # append element without heapify
    def append_elem(self, elem):
        self.arr.append(elem)

    # insert as max heap
    def ins_max(self, elem):
        self.arr.append(elem)
        # move current to the newly add element at last
        cur = len(self.arr) - 1
        # compare the current with parent and swap if necessary
        while cur > 0 and self.arr[(cur - 1) // 2] < self.arr[cur]:
            self.arr[(cur - 1) //
                     2], self.arr[cur] = self.arr[cur], self.arr[(cur - 1) // 2]
            cur = (cur - 1) // 2

    # insert as min heap, similar to max heap
    def ins_min(self, elem):
        self.arr.append(elem)
        cur = len(self.arr) - 1
        while cur > 0 and self.arr[(cur - 1) // 2] > self.arr[cur]:
            self.arr[(cur - 1) //
                     2], self.arr[cur] = self.arr[cur], self.arr[(cur - 1) // 2]
            cur = (cur - 1) // 2

    # max heapify
    def heapify_max(self):
        size = len(self.arr)
        # skip the last leaf if it is single out
        first_parent = (size - 3 + size % 2) // 2
        first_right_kid = (first_parent + 1) * 2
        # outer loop, move from first none leaf till root
        while first_parent >= 0:
            parent = first_parent
            right_kid = first_right_kid

            # inner loop, if swap, contine down until end of array
            while right_kid < (size - 1 + size % 2):

                # get the larger child index
                larger_kid = right_kid - \
                    (self.arr[right_kid - 1] >= self.arr[right_kid])
                # swap if child > parent
                if self.arr[larger_kid] > self.arr[parent]:
                    self.arr[larger_kid], self.arr[parent] = self.arr[parent], self.arr[larger_kid]
                parent = larger_kid
                right_kid = (parent + 1) * 2

            first_right_kid -= 2
            first_parent -= 1

        # insert the single out child back if it exists
        if size % 2 == 0:
            elem = self.arr.pop()
            self.ins_max(elem)

    # min heapift, similar to max
    def heapify_min(self):
        size = len(self.arr)
        first_parent = (size - 3 + size % 2) // 2
        first_right_kid = (first_parent + 1) * 2
        while first_parent >= 0:
            parent = first_parent
            right_kid = first_right_kid
            while right_kid < size:
                smaller_kid = right_kid - \
                    (self.arr[right_kid - 1] <= self.arr[right_kid])
                if self.arr[smaller_kid] < self.arr[parent]:
                    self.arr[smaller_kid], self.arr[parent] = self.arr[parent], self.arr[smaller_kid]
                parent = smaller_kid
                right_kid = (right_kid + 1) * 2

            first_right_kid -= 2
            first_parent -= 1
        if size % 2 == 0:
            elem = self.arr.pop()
            self.ins_min(elem)

# ========================
# self testing

# a_heap = Heap([7, 6, 5, 4, 8, 3, 2, 1])
# print(a_heap.arr)
# a_heap.heapify_max()
# print(a_heap.arr)
# a_heap.heapify_min()
# print(a_heap.arr)
