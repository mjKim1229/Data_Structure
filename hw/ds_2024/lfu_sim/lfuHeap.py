class LfuHeap:

    def __init__(self, list, cache_slots):
        if list == None:
            self.__A = []
        else:
            self.__A = []
        self.buildHeap()
        self.length = cache_slots

    # heap이 다 찼는지 여부를 반환
    def isFull(self):
        return self.size() == self.length

    # heap의 lpn에 해당하는 freq값 1증가
    def hit(self, index):
        self.__A[index][1] += 1

    # 힙의 원소는 [lpn,freq] 형태로 삽입
    def insert(self, lpn, freq):
        self.__A.append([lpn, freq])
        self.percolateUp(len(self.__A)-1)

    # freq가 가장 낮은 값을 삭제
    def deleteMin(self):
        if (not self.isEmpty()):
            min = self.__A[0]
            self.__A[0] = self.__A.pop()
            self.percolateDown(0)
            return min
        else:
            return None

    # 스며오르기, 스며내리기 : 각 원소의 freq 기준 힙 수선 작업
    def percolateUp(self, i:int):
        parent = (i-1) // 2
        if i > 0 and self.__A[i][1] < self.__A[parent][1]:
            self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
            self.percolateUp(parent)

    def percolateDown(self, i:int):
        left = 2 * i + 1  # left child
        right = 2 * i + 2  # right child
        if (left <= len(self.__A)-1):
            if (right <= len(self.__A)-1 and self.__A[left][1] > self.__A[right][1]):
                left = right
            if self.__A[i][1] > self.__A[left][1]:
                self.__A[i], self.__A[left] = self.__A[left], self.__A[i]
                self.percolateDown(left)

    # lpn에 해당하는 index 값 반환
    def search(self, x):
        for i in range(len(self.__A)):
            if self.__A[i][0] == x:
                return i
        return False

    def buildHeap(self):
        for i in range((len(self.__A)-2)//2, -1, -1): # 마지막 노드의 부모 노드에서부터 0번째 노드까지 스며내리기를 진행하기
            self.percolateDown(i) # 재귀적 호출

    def isEmpty(self):
        return len(self.__A) == 0

    def size(self):
        return len(self.__A)
