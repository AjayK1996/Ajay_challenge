import re

def is_valid_credit_card(card_number):
    # Check if the card starts with 4, 5, or 6 and has exactly 16 digits
    if not re.match(r"^[456]\d{3}(-?\d{4}){3}$", card_number):
        return False

    # Remove hyphens and check if the card contains only digits
    card_number = card_number.replace("-", "")
    if not card_number.isdigit():
        return False

    # Check if there are no 4 or more consecutive repeated digits
    if re.search(r"(\d)\1{3}", card_number):
        return False

    return True

# Input
N = int(input())
credit_cards = [input().strip() for _ in range(N)]

# Output
for card in credit_cards:
    if is_valid_credit_card(card):
        print("Valid")
    else:
        print("Invalid")
