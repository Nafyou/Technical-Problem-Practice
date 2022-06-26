class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Insight: Two parts
        # 1)How do we find a valid substring containing same letters after replacement ? 
        # - Helper Questions
        # What does a substring consist of ? 
        
        # repeating letters, replacements, left and right index
        # Can I make an equation with these ?
        # right - left + 1 = length
        # length - most_repeating_letter = number of replacements
        # invalid: length-most_frequent > k
        
        # 2)How do we find the length of the longest substring ?
        # length = right - left + 1
        # max_length = max(length,max_length)
        
        # 3) How do we keep track of the most frequent letter ?
        # Use a hashmap and iterate through the string, update as we travel through 
        
        # Insight: Manage "state" of the window, try to extend until we hit an invalid state
        # And then after, we are in valid state calculate length. 
        
        #Summary:
        # Extend window until invalid state.(keeping track of most_frequent,length)
        # calculate length and keep track of max
        left = 0
        most_frequent = 0 
        max_length = -float('inf')
        freq = {}
        for right in range(len(s)):
            letter = s[right]
            freq[letter] = freq.get(letter,0) + 1
            most_frequent = max(freq[letter],most_frequent)
            # more replacements then possible
            while right-left+1-most_frequent > k:
                left_letter = s[left]
                freq[left_letter] -= 1
                left += 1
                
            length = right - left + 1
            max_length = max(length,max_length)
            
        return max_length
                