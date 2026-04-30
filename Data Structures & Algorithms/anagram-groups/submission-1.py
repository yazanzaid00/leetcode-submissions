class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = dict()
        for string in strs:
            num_of_letters = ord('z') - ord('a') + 1
            count = [0] * num_of_letters #how to intialize array python with zeros, is this good count[num_of_letters] = 0?
            # can i do list comprehension in here instead of explicit for loop?

            for char in string:
                count[ord(char)-ord('a')] += 1
            # make count immutable, how much time complexity does this take?
            immutable_count = tuple(count)
            key = hash_table.get(immutable_count)
            if key:
                key.append(string)
            else:
                hash_table[immutable_count] = [string]
        return list(hash_table.values())  # how mcuh time complexlity does list take in python? What about values()

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
#         hash_table = dict()
#         # O(m)
#         for string in strs:
#             sorted_string = str(sorted(string)) # counting sort  # counting sort each string which takes O(n) then check in hash table
#             key = hash_table.get(sorted_string) # O(1)
#             if key:
#                 key.append(string) # O(1)
#             else:
#                 hash_table[sorted_string] = [string] # O(1)
        
#         return list(hash_table.values())  # how mcuh time complexlity does list take in python? What about values()