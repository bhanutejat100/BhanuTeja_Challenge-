import re

def check_credit_card(card_number):
   print(card_number)
   if not card_number:
       return "Invalid Card Number"
   
   pattern = r'\[4-6\]\[0-9\]{3}-?\[0-9\]{4}-?\[0-9\]{4}-?\[0-9\]{4}$'
   if not re.match(pattern, card_number):
       return 'Invalid Card Number'
   
   previous_digit = card_number[0]
   repeat_count = 1
   for current_digit in card_number[1:]:
       if current_digit == previous_digit:
           repeat_count += 1
       else:
           previous_digit = current_digit
           repeat_count = 1
       if repeat_count == 4:
           return "Invalid Card Number"
   
   return "Valid Card Number"

def validate_valid_cards():
   valid_cards = ["5555555555554444", "6011601160116011", "3782822463100005"]
   expected_result = "Valid Card Number"
   for card in valid_cards:
       assert expected_result == check_credit_card(card)

def validate_invalid_cards():
   invalid_cards = ["5555555555554444444", "6011601160116011601", "3782822463100000", "12345678901234"]
   expected_result = "Invalid Card Number"
   for card in invalid_cards:
       assert expected_result == check_credit_card(card)

validate_valid_cards()
validate_invalid_cards()
print("Test cases completed successfully")
