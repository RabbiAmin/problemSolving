#second solotion of anagrams problem by using counter
from collections import Counter

def are_anagrams(s1,s2):
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)

print(are_anagrams("aminrabbi","rabbiamin"))
print(are_anagrams("nameless","salesmen"))
print(are_anagrams("danger","garden"))