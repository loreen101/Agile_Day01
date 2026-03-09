import re

def extract_individual_digits(text: str) -> list[int]:
    """
    Uses Regex to find every single digit character.

    """
    pattern = r"\d"
    digit_strings = re.findall(pattern, text)
    
    return [int(d) for d in digit_strings]

def calculate_sum_of_digits(text: str) -> int:
    """
    Takes text, extracts the digits, and returns their sum.
    
    """
    digits = extract_individual_digits(text)
    
    print(f"Extracted digits: {digits}")
    
    return sum(digits)

if __name__ == "__main__":
    user_input = input("Enter text: ")
    
    total = calculate_sum_of_digits(user_input)
    
    print(f"Total Sum of Digits: {total}")