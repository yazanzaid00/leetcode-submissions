class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Keep your boundary logic
        l, r, t, b = -1, len(matrix[0]), -1, len(matrix)
        curr_i, curr_j = 0, 0
        curr_dir = (0, 1)
        res = []
        
        # Use total elements to ensure we don't loop infinitely if bounds cross awkwardly
        total_elements = len(matrix) * len(matrix[0])
        
        while l < r and  t < b:
            # --- SURGICAL FIX START ---
            
            # Logic: If out of bounds, Shrink Wall -> New Dir -> Fix Coordinates
            
            # Hit Right Wall (Overshot to the right)
            if curr_j == r:
                t += 1              # Top row is done
                curr_dir = (1, 0)   # Corrected: Down is (1, 0)
                curr_j -= 1         # Step back into bounds
                curr_i += 1         # Step down into new path
                
            # Hit Bottom Wall (Overshot the bottom)
            elif curr_i == b:
                r -= 1              # Right col is done
                curr_dir = (0, -1)  # Left
                curr_i -= 1         # Step back up
                curr_j -= 1         # Step left
                
            # Hit Left Wall (Overshot the left)
            elif curr_j == l:
                b -= 1              # Bottom row is done
                curr_dir = (-1, 0)  # Corrected: Up is (-1, 0)
                curr_j += 1         # Step back right
                curr_i -= 1         # Step up
                
            # Hit Top Wall (Overshot the top)
            elif curr_i == t:
                l += 1              # Left col is done
                curr_dir = (0, 1)   # Right
                curr_i += 1         # Step back down
                curr_j += 1         # Step right
            
            # --- SURGICAL FIX END ---

            # while valid coordinates (Your original inner loop)
            # Added len check to prevent adding duplicates during the turn logic
            while t < curr_i < b and l < curr_j < r:
                res.append(matrix[curr_i][curr_j])
                curr_i += curr_dir[0]
                curr_j += curr_dir[1]
                
        return res