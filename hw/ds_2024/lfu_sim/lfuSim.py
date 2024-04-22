from lfuHeap import *

def lfu_sim(cache_slots):
    cache_hit = 0
    tot_cnt = 0

    data_file = open("linkbench.trc")

    cache_dict = dict()
    cache_heap = LfuHeap([], cache_slots)

    for line in data_file.readlines():
        lpn = line.split()[0]

        # 1. cache_dict에서의 처리
        # 새로 들어오면 값을 1로 함
        if lpn not in cache_dict.keys():
            cache_dict[lpn] = 1
        # 기존에 있다면 1증가
        else:
            cache_dict[lpn] += 1

        # 2. cache_heap에서의 처리
        if not cache_heap.search(lpn):
            # heap이 다 찼다면, 가장 적은 참조횟수 삭제(최소힙)
            if cache_heap.isFull():
                cache_heap.deleteMin()
            cache_heap.insert(lpn, cache_dict[lpn])
        else:
            # hit 횟수 업데이트 및 힙 수선
            index = cache_heap.search(lpn)
            cache_heap.hit(index)
            cache_dict[lpn] += 1
            cache_heap.percolateDown(index)
            cache_hit += 1
        tot_cnt += 1

    # Program here

    print("cache_slot =", cache_slots, "cache_hit =", cache_hit, "hit ratio =", cache_hit / tot_cnt)

if __name__ == "__main__":
    for cache_slots in range(100, 1000, 100):
        lfu_sim(cache_slots)
