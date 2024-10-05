# Write a function that uses a regex expression to return a list with all the words that start with a vowel.
# Exmaple:
# Input: 'Errors should never pass silently. Unless explicitly silenced.'
# Output: ['Errors', 'Unless', 'explicitly']
import re

def regWord(characters):
    pattern = r'\b[aeiouAEIOU]\w*'
    return re.findall(pattern, characters)

print(regWord('Errors should never pass silently. Unless explicitly silenced.'))

# Write another function that uses a regex expression to return a list of emails that all have the domain of gmail.com.
# Exmaple:
# Input: 'aa@xyz.com bbb@abc.com cccc@cisco.com'
# Output: ['aa@gmail.com', 'bbb@gmail.com', 'cccc@gmail.com']
def add_gmail(text):
    pattern = r'@[a-zA-Z]+\.'
    return re.sub(pattern, '@gmail.', text)

text = 'aa@xyz.com bbb@abc.com cccc@cisco.com'
result = add_gmail(text)
print(result)

