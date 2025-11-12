def check_vowel_consonant(ch):
    vowels="aeiouAEIOU"
    if ch in vowels:
        print(ch, "is a vowel")
    else:
        print(ch, "is consonant")
char=input("Enter a single character:")
check_vowel_consonant(char)
