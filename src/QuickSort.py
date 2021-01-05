class SortableArray:
    def __init__(self, array):
        self.array = array

    def partition(self, left_pointer, right_pointer):

        #항상 가장 오른쪽에 있는 값을 피벗으로 선택
        pivot_position = right_pointer
        pivot = self.array[pivot_position]

        #피벗 바로 왼쪽에서 오른쪽 포인터를 시작시킨다.
        right_pointer -= 1
        while True:
            while self.array[left_pointer] < pivot:
                left_pointer += 1
            while self.array[right_pointer] > pivot:
                right_pointer -= 1
            if left_pointer >= right_pointer:
                break
            else:
                left_pointer, right_pointer = right_pointer, left_pointer

            left_pointer, pivot_position = pivot_position, left_pointer #이걸 왜 스왑하는건지??

        return left_pointer



    def quicksort(self,left_index, right_index):
        if right_index - left_index <= 0:
            return

        pivot_position = self.partition(left_index, right_index) #객체함수 사용부분

        self.quicksort(left_index, pivot_position - 1)

        self.quicksort(pivot_position + 1, right_index) # 재귀함수가 두개??


if __name__ == '__main__':

    obj = SortableArray([0, 5, 2, 1, 6, 3])
    obj.quicksort(0, 5)
    print(obj.array)