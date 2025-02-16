import re
import sys

class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value  # Use the setter to validate input

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")  # Print the message instead of raising an error

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        sentences = re.split(r'[.!?]+', self.value.strip())
        return len([s for s in sentences if s.strip()])

# Example usage
string = MyString()
string.value = 123  # Should print: The value must be a string.

test_string = MyString("This is a string! It has three sentences. Right?")
print(test_string.count_sentences())  # Output: 3
print(test_string.is_sentence())  # Output: False
print(test_string.is_question())  # Output: True
print(test_string.is_exclamation())  # Output: False
