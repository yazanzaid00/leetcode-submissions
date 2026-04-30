class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u, v, t in times:
            adj_list[u].append((t, v))
        min_heap = [(0, k)]
        distances = [float("inf")] * (n + 1)
        distances[k] = 0
        while min_heap:
            cur_time, cur_node = heapq.heappop(min_heap)
            if cur_time > distances[cur_node]:
                continue
            for time, nei in adj_list[cur_node]:
                if cur_time + time < distances[nei]:
                    distances[nei] = cur_time + time
                    heapq.heappush(min_heap, (distances[nei], nei))
                
        distances = distances[1:]
        return -1 if max(distances) == float("inf") else max(distances)