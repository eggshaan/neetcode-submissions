class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        for i in s:
            s_map[i] = s_map.get(i,0)+1

        t_map = {}
        for i in t:
            t_map[i] = t_map.get(i,0)+1
        
        return s_map == t_map


        
        

        
        