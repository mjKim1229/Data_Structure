

class CacheSimulator:
    def __init__(self, cache_slots):
        self.cache_slots = cache_slots
        self.cache_hit = 0
        self.tot_cnt = 1
        self.array = []
    
    def do_sim(self, page):
        #1번마다 tot_cnt 증가 
        self.tot_cnt += 1 
        
        #[1] : 페이지에 있는 지 확인 후 삽입 
        if page in self.array: #1. cache hit
            self.array.remove(page)
            self.array.insert(0,page)
            self.cache_hit += 1 
        else: #2. cache miss
            self.array.insert(0,page)

        
        #[2] : cache_slot의 크기보다 크면 마지막 원소 삭제 
        if len(self.array) > self.cache_slots:
            self.array.pop()
 
        
    def print_stats(self):
        print("cache_slot = ", self.cache_slots, "cache_hit = ", self.cache_hit, "hit ratio = ", self.cache_hit / self.tot_cnt)


if __name__ == "__main__":

    data_file = open("./linkbench.trc")
    lines = data_file.readlines()
    for cache_slots in range(100, 1001, 100):
        cache_sim = CacheSimulator(cache_slots)
        for line in lines:
            page = line.split()[0]
            cache_sim.do_sim(page)
        
        cache_sim.print_stats()

