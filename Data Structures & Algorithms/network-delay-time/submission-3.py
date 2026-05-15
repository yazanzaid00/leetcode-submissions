class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # we solve it dijkastra
        adj_list = defaultdict(list)
        for src, dest, time in times:
            adj_list[src - 1].append((time, dest - 1))
        

        distances = [float("inf")] * n
        min_heap = [(0, k - 1)]
        distances[k - 1] = 0

        while min_heap:
            cur_wei, cur_node = heapq.heappop(min_heap)

            if cur_wei > distances[cur_node]:
                continue

            for wei, nei in adj_list[cur_node]:
                if cur_wei + wei < distances[nei]:
                    distances[nei] = cur_wei + wei
                    heapq.heappush(min_heap, (distances[nei], nei))
        
        return -1 if float("inf") in distances else max(distances)