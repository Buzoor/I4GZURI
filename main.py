# Check if a word is an anagrams
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(str1, str2):
    str1 = input("string1:")
    str2 = input("string2:")
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False
find_anagrams('str1', 'str2')
