#given two strings s1 and s2, check if they're anagrams. Two string are anagrams if they are made of the same characters with the same frequencies

def are_anagrams(s1,s2):
    if len(s1) != len(s2): #if s1 and s2 len is not same then return false
        return False
    frequency1 = {} #frequency of characters of s1 #space "O(n)"
    frequency2 = {} #frequency of characters of s2 #space "O(n)"
    for ch in s1: #frequency of s1 characters  #Time "O(n)"
        if ch in frequency1:
            frequency1[ch] += 1
        else:
            frequency1[ch] = 1
    for ch in s2: #frequency of s2 characters #Time "O(n)"
        if ch in frequency2 :
            frequency2 [ch] += 1
        else:
            frequency2 [ch] = 1
    for key in frequency1: #Time "O(n)"
        if key not in frequency2 or frequency1[key] != frequency2[key]:  #if frequency1 == frequency2 => s1 and s2 are anagrams
            return False
    return True
#T(n) = O(n) + O(n) + O(n) == O(n)
#S(n) = O(n) + O(n) == O(n)
print(are_anagrams("aminrabbi","rabbiamin"))
print(are_anagrams("nameless","salesmen"))
print(are_anagrams("danger","garden"))
