import heapq

class LRUCache:

    def __init__(self, capacity: int):
        # key -> (value, last_used_time)
        self.hash_map = dict()
        self.capacity = capacity              # fixed maximum number of keys
        # (last_used_time, key) min-heap
        self.min_heap = []
        self.timer = 0

    def _touch(self, key: int) -> None:
        """Mark an existing key as most recently used."""
        self.timer += 1
        value, _ = self.hash_map[key]
        self.hash_map[key] = (value, self.timer)
        # push new (time, key); old heap entries become "stale"
        heapq.heappush(self.min_heap, (self.timer, key))

    def _evict(self) -> None:
        """Evict the true LRU key when over capacity (lazy-stale cleanup)."""
        while len(self.hash_map) > self.capacity and self.min_heap:
            last_used_time, key = heapq.heappop(self.min_heap)
            # Key already removed.
            if key not in self.hash_map:
                continue
            # Heap entry is stale (we have a newer timestamp in the map).
            if self.hash_map[key][1] != last_used_time:
                continue
            # This is the real LRU.
            del self.hash_map[key]
            break

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        self._touch(key)
        return self.hash_map[key][0]

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            # Update value and recency.
            self.hash_map[key] = (value, self.hash_map[key][1])
            self._touch(key)
        else:
            # Insert new key and evict if over capacity.
            self.timer += 1
            self.hash_map[key] = (value, self.timer)
            heapq.heappush(self.min_heap, (self.timer, key))
            self._evict()
