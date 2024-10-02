def validAnagram(str1, str2):
    str1_dict = {}
    str2_dict = {}

    for char in str1:
        if char not in str1_dict:
            str1_dict[char] = 1
        else:
            str1_dict[char] += 1
    # print(str1_dict)

    for char in str2:
        if char not in str2_dict:
            str2_dict[char] = 1
        else:
            str2_dict[char] += 1
    # print(str2_dict)

    for k in str1_dict.keys():
        if k not in str2_dict:
            return False
        elif str1_dict[k] != str2_dict[k]:
            return False

    return True

print(validAnagram('aaz', 'zza')) # false
print(validAnagram('anagram', 'nagaram')) # true
print(validAnagram('rat', 'car')) # false
print(validAnagram('qwerty', 'qeywrt')) # true