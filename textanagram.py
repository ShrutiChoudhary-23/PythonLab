
# Function to clean text
def clean_text(text):
    return ''.join(
        ch.lower() for ch in text if ch.isalnum()
    )

# Function to generate an anagram key using sorting
def get_anagram_key(text):
    cleaned = clean_text(text)
    return tuple(sorted(cleaned))

# Function to check whether two texts are anagrams
def are_anagrams(text1, text2):
    return get_anagram_key(text1) == get_anagram_key(text2)

# Function to group anagrams using a dictionary
def group_anagrams(words):
    groups = {}

    for word in words:
        key = get_anagram_key(word)
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return groups

# Main program
text1 = input("Enter first word or phrase: ")
text2 = input("Enter second word or phrase: ")

if are_anagrams(text1, text2):
    print("The two texts are anagrams.")
else:
    print("The two texts are not anagrams.")

# Pattern matching across multiple words
words = input(
    "\nEnter multiple words separated by spaces: "
).split()

patterns = group_anagrams(words)

print("\nAnagram Groups:")

for key, group in patterns.items():
    print(group)