class Node:
    def __init__(self, key = 0, value = 0, prev = None, nxt = None):
        self._key = key
        self._value = value
        self._prev = prev
        self._nxt = nxt

class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._in_list = {}
        self._lru = Node()
        self._mru = Node()
        self._lru._nxt = self._mru
        self._mru._prev = self._lru
        

    def get(self, key: int) -> int:
        if key in self._in_list:
            key_node = self._in_list[key]
            self._remove(key_node)
            self._append(key_node)
            return key_node._value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self._in_list:
            key_node = self._in_list[key]
            self._remove(key_node)
            self._append(key_node)
            key_node._value = value
        else:
            key_node = Node(key, value)
            self._append(key_node)
        
    def _remove(self, node:Node)->None:
        key = node._key
        prev_node, nxt_node = node._prev, node._nxt
        prev_node._nxt = nxt_node
        nxt_node._prev = prev_node
        del self._in_list[key]

    def _append(self, node:Node)->None:
        last_node = self._mru._prev
        last_node._nxt = node
        node._prev = last_node
        node._nxt = self._mru
        # what if i type last_node instead of self._mru._prev what happens? is it by reference in python or just pointer at the same reference?
        self._mru._prev = node
        self._in_list[node._key] = node
        if len(self._in_list) > self._capacity:
            self._remove(self._lru._nxt)
