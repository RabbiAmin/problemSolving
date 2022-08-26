def are_anagrams(s1,s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2) # for sorting algm Time "O(nlogn)" here working two sorting algm, for equality check Time "n"  #for space sorting space "n"
#T(n) = O(nlogn) + O(nlogn) + n == O(nlogn)
#S(n) = 2n == O(n)
print(are_anagrams("aminrabbi","rabbiamin"))
print(are_anagrams("nameless","salesmen"))
print(are_anagrams("danger","garden"))