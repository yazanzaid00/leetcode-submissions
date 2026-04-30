class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heap.append((a, 'a'))
        if b > 0:
            heap.append((b, 'b'))
        if c > 0:
            heap.append((c, 'c'))
        heapq.heapify_max(heap)
        res = []
        while heap:
            max_val, max_char = heapq.heappop_max(heap)
            if len(res) >= 2 and res[-2] == res[-1] == max_char:
                if not heap:
                    break
                sec_max_val, sec_max_char = heapq.heappop_max(heap)
                res.append(sec_max_char)
                if sec_max_val > 1:
                    heapq.heappush_max(heap, (sec_max_val - 1, sec_max_char))
                heapq.heappush_max(heap, (max_val, max_char))
            else:
                res.append(max_char)
                if max_val > 1:
                    heapq.heappush_max(heap, (max_val - 1, max_char))
        return "".join(res)