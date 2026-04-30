class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        Build the longest 'happy' string using a, b, c copies of 'a','b','c', where:
          - no "aaa", "bbb", or "ccc" is allowed as a substring.
        Greedy idea:
          - At each step, pick the character with the highest remaining count
            that does NOT create three identical chars in a row.
          - If no such character exists, we stop; the string is maximal.
        """

        # Represent remaining counts as a small list of [char, count] pairs.
        # Using a list instead of a heap is fine because we only have 3 characters.
        chars = [
            ['a', a],
            ['b', b],
            ['c', c],
        ]

        # We'll build the answer as a list of characters (more efficient than string concat).
        result = []

        while True:
            # Sort characters by current remaining count (ascending).
            # After this, chars[-1] will be the character with the largest remaining count.
            # Sorting a list of size 3 is effectively O(1) time.
            chars.sort(key=lambda pair: pair[1])

            placed = False  # Track if we successfully place a character in this iteration.

            # Try characters from largest remaining count to smallest: indices 2, 1, 0.
            for i in range(2, -1, -1):
                ch, count = chars[i]

                if count == 0:
                    # No copies of this character left; skip it.
                    continue

                # Check if using this character would create three in a row.
                # We only need to look at the last two characters of the current result.
                if len(result) >= 2 and result[-1] == ch and result[-2] == ch:
                    # Using 'ch' would make "xxx" at the end, so it's not allowed now.
                    # We *don't* give up; we just try the next-most-frequent character.
                    continue

                # If we reach here, we CAN safely use this character.
                result.append(ch)
                chars[i][1] -= 1  # Decrease remaining count for this character.
                placed = True
                break  # We made our greedy choice for this step; move to the next step.

            if not placed:
                # We tried all characters from most frequent to least frequent, and:
                #   - either all counts were zero, OR
                #   - every remaining character would create "xxx" if appended.
                # In either case, we cannot extend the happy string anymore.
                # So the current result is a longest possible happy string.
                break

        # Convert the list of characters into the final string.
        return ''.join(result)
