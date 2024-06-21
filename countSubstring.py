#Count Substrings Starting and Ending with Given Character
def count_substrings(s, c):
    count = 0

    # Count the occurrences of the character c in the string
    c_count = s.count(c)  
    
    count = c_count * (c_count + 1) // 2
    
    return count


s1 = "abada"
c1 = "a"
print(count_substrings(s1, c1))  

s2 = "zzz"
c2 = "z"
print(count_substrings(s2, c2))  
