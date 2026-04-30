class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # counting sort each string which takes O(m) then check in hash table
        hash_table = dict()
        for string in strs:
            sorted_string = str(sorted(string)) # counting sort
            key = hash_table.get(sorted_string)
            if key:
                key.append(string)
            else:
                hash_table[sorted_string] = [string]
        
        return list(hash_table.values())