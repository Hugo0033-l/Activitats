def is_anagram(string1:str, string2:str) -> bool:
    if string1.lower() == string2.lower():
        return False
    return sorted(string1.lower()) == sorted(string2.lower())

w1 = input().strip()
w2 = input().strip()
print(is_anagram(w1,w2))