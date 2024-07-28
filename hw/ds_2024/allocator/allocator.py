import time

class Block:
    def __init__(self, chunk_index, offset, length):
        """
        블록 클래스 초기화
        :param chunk_index: 청크 인덱스
        :param offset: 오프셋
        :param length: 길이
        """
        self.chunk_index = chunk_index  # 청크 인덱스
        self.offset = offset  # 오프셋
        self.length = length  # 길이
        self.next_block = None  # 다음 블록 포인터

class Arena:
    def __init__(self, chunk_size= 16 * 1024):
        """
        아레나 클래스 초기화
        :param chunk_size: 청크 크기
        """
        self.chunk_size = chunk_size  # 청크 크기
        self.chunks = []  # 청크 리스트
        self.free_blocks = None  # 빈 블록 리스트

    def add_chunk(self):
        """
        새로운 청크를 아레나에 추가
        """
        new_chunk = bytearray(self.chunk_size)  # 새로운 청크 생성
        self.chunks.append(new_chunk)  # 청크 리스트에 추가
        new_free_block = Block(len(self.chunks) - 1, 0, self.chunk_size)  # 새로운 빈 블록 생성
        new_free_block.next_block = self.free_blocks  # 새로운 빈 블록을 빈 블록 리스트의 맨 앞에 추가
        self.free_blocks = new_free_block
    

class Allocator:
    def __init__(self, arena: Arena):
        """
        할당기 클래스 초기화
        :param arena: 메모리 아레나
        """
        self.arena = arena  # 메모리 아레나
        self.allocations = {}  # 할당된 메모리 블록 딕셔너리
        self.total_alloc_time = 0  # 총 할당 시간
        self.total_free_time = 0  # 총 해제 시간
        self.alloc_ops = 0  # 할당 연산 횟수
        self.free_ops = 0  # 해제 연산 횟수

    def allocate_memory(self, identifier, size):
        """
        메모리를 할당하는 메서드
        :param identifier: 식별자
        :param size: 크기
        """
        start = time.time()
        block_info = self.find_block(size)  # 적합한 블록 찾기
        
        if not block_info:
            self.arena.add_chunk() # 새로운 청크 생성 
            block_info = self.find_block(size)  # 다시 블록 찾기

        (previous_block, current_block) = block_info
        self.commit_allocation(previous_block, current_block, identifier, size)  # 할당 수행
        self.total_alloc_time += time.time() - start  # 총 할당 시간 업데이트
        self.alloc_ops += 1  # 할당 연산 횟수 증가

    def find_block(self, size):
        """
        요청된 크기의 적합한 블록을 찾는 메서드
        :param size: 요청된 크기
        :return: (이전 블록, 현재 블록) 튜플
        """
        previous = None
        current = self.arena.free_blocks

        while current:
            if current.length >= size:
                return (previous, current)
            previous = current
            current = current.next_block
        return None

    def commit_allocation(self, previous_block: Block, current_block: Block, identifier, size):
        """
        메모리 할당을 커밋하는 메서드
        :param previous_block: 이전 블록
        :param current_block: 현재 블록
        :param identifier: 식별자
        :param size: 크기
        """
        # 할당 정보를 할당된 메모리 블록 딕셔너리에 추가
        self.allocations[identifier] = (current_block.chunk_index, current_block.offset, size)
        
        # 현재 블록이 요청한 크기보다 큰 경우 남은 부분을 새로운 블록으로 분할
        if current_block.length > size:
            current_block.offset += size
            current_block.length -= size
        else:
            # 현재 블록을 리스트에서 제거하고 해제된 블록 리스트에 추가
            if previous_block:
                previous_block.next_block = current_block.next_block
            else:
                self.arena.free_blocks = current_block.next_block

    def deallocate_memory(self, identifier):
        """
        메모리 할당을 해제하는 메서드
        :param identifier: 식별자
        """
        start = time.time()
        
        # 할당된 메모리 블록 딕셔너리에서 식별자에 해당하는 블록 정보 가져오기
        if identifier in self.allocations:
            chunk_index, offset, size = self.allocations.pop(identifier)
            self.insert_free_block(chunk_index, offset, size)  # 블록을 해제된 블록 리스트에 추가
        else:
            print(f"Invalid Identifier!: {identifier}")

        # 해제 시간 측정
        self.total_free_time += time.time() - start
        self.free_ops += 1

    def insert_free_block(self, chunk_index, offset, size):
        """
        해제된 블록을 빈 블록 리스트에 추가하는 메서드
        :param chunk_index: 청크 인덱스
        :param offset: 오프셋
        :param size: 크기
        """
        freed_block = Block(chunk_index, offset, size)
        freed_block.next_block = self.arena.free_blocks
        self.arena.free_blocks = freed_block

    def print_stats(self):
        """
        메모리 할당 통계 정보 출력
        """
        total_memory = len(self.arena.chunks) * self.arena.chunk_size  # 총 메모리
        allocated_memory = sum(size for index, offset, size in self.allocations.values())  # 할당된 메모리
        utilization_rate = allocated_memory / total_memory  # 활용률

        # 아레나 정보 출력
        print(f"Arena: {total_memory / (1024 * 1024):.2f} MB")

        # 사용 중인 메모리 정보 출력
        print(f"In-Use: {allocated_memory / (1024 * 1024):.2f} MB")

        # 활용률 정보 출력
        print(f"Utilization: {utilization_rate:.2f}")

        #총 사용 시간 
        print(f"Total Operation Time: {self.total_alloc_time + self.total_free_time:.6f} 초")

        # 총 할당 시간 정보 출력
        print(f"Total Allocation Time: {self.total_alloc_time:.6f} 초")

        # 총 해제 시간 정보 출력
        print(f"Total Free Time: {self.total_free_time:.6f} 초")


if __name__ == "__main__":
    arena = Arena()  # 메모리 아레나 생성
    allocator = Allocator(arena)  # 메모리 할당기 생성
    
    with open("./input.txt", "r") as file:
        for line in file:
            parts = line.split()
            command, identifier = parts[0], int(parts[1])
            
            if command == 'a':
                size = int(parts[2])
                allocator.allocate_memory(identifier, size)  # 메모리 할당
            elif command == 'f':
                allocator.deallocate_memory(identifier)  # 메모리 해제

    allocator.print_stats()  # 통계 정보 출력
