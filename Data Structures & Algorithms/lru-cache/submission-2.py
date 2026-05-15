class Node:
    def __init__(self, key = 0, val=0, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt
        
class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._in_list = dict()
        self._lru, self._mru = Node(), Node()
        self._lru.nxt = self._mru
        self._mru.prev = self._lru

    def get(self, key: int) -> int:
        if key in self._in_list:
            cur_node = self._in_list[key]
            self._remove(cur_node, key)
            self._append(cur_node, key)
            return self._in_list[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self._in_list:
            cur_node = self._in_list[key]
            self._remove(cur_node, key)
            self._append(cur_node, key)
            cur_node.val = value
        else:
            cur_node = Node(key, value)
            self._append(cur_node, key)
            if len(self._in_list) > self._capacity:
                self._remove(self._lru.nxt, self._lru.nxt.key)


    def _remove(self, node, key):
        prev_node = node.prev
        next_node = node.nxt
        prev_node.nxt = next_node
        next_node.prev = prev_node
        del self._in_list[key]

    def _append(self, node, key):
        prev_mru = self._mru.prev
        node.prev = prev_mru
        node.nxt = self._mru
        prev_mru.nxt = node
        self._mru.prev = node
        self._in_list[key] = node
