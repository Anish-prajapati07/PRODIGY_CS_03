import re
def assess_password_strength(password):
    length_score = 0
    uppercase_score = 0
    lowercase_score = 0
    number_score = 0
    special_char_score = 0
    if len(password) >= 8:
        length_score = 1
    if len(password) >= 12:
        length_score = 2
    if len(password) >= 16:
        length_score = 1
    if re.search(r'[A-Z]', password):
        uppercase_score = 1
    if re.search(r'[A-Z]{2,}', password):
        uppercase_score = 2
    if re.search(r'[a-z]', password):
        lowercase_score = 1
    if re.search(r'[a-z]{2,}', password):
        lowercase_score = 2
    if re.search(r'\d', password):
        number_score = 1
    if re.search(r'\d{2,}', password):
        number_score = 2
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        special_char_score = 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]{2,}', password):
        special_char_score = 2
    total_score = length_score + uppercase_score + lowercase_score + number_score + special_char_score
    if total_score >= 8:
        strength = "Very Strong"
    elif total_score >= 6:
        strength = "Strong"
    elif total_score >= 4:
        strength = "Moderate"
    else:
        strength = "Weak"
    result = {
        'length': length_score,
        'uppercase': uppercase_score,
        'lowercase': lowercase_score,
        'numbers': number_score,
        'special_characters': special_char_score,
        'strength': strength
    }
    return result
password = input("Enter a password to assess: ")
result = assess_password_strength(password)
print("\nPassword Assessment:")
print(f"Length Score: {result['length']}")
print(f"Uppercase Score: {result['uppercase']}")
print(f"Lowercase Score: {result['lowercase']}")
print(f"Numbers Score: {result['numbers']}")
print(f"Special Characters Score: {result['special_characters']}")
print(f"Overall Strength: {result['strength']}")
