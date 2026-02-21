class IntegerToRoman:
    """
    A class to convert an integer value to a Roman numeral using OOP principles.
    """
    # Define the Roman numeral mappings as a class attribute (static data)
    roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
        (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'),
        (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    def __init__(self, number):
        """
        Initialize the class with the integer value to convert.
        Valid input range is 1 to 3999.
        """
        if not isinstance(number, int) or not (1 <= number <= 3999):
            raise ValueError("Input must be an integer between 1 and 3999.")
        self.number = number

    def convert(self):
        """
        Convert the stored integer to its Roman numeral representation.
        Implements a greedy algorithm using the predefined map.
        """
        num_to_convert = self.number
        roman_numeral = []

        for value, symbol in IntegerToRoman.roman_map:
            # Use integer division (//) to find out how many times the current
            # value fits into the remaining number, and modulo (%) to get the remainder
            count = num_to_convert // value
            if count > 0:
                roman_numeral.append(symbol * count)
                num_to_convert %= value
            
            # Stop if the number is fully converted
            if num_to_convert == 0:
                break
                
        # Join the list of symbols into a single string for better performance
        return "".join(roman_numeral)

# --- Example Usage ---
# Create an instance of the class
numeral_converter = IntegerToRoman(1994)

# Call the conversion method
result = numeral_converter.convert()
print(f"The Roman numeral for 1994 is: {result}") # Output: The Roman numeral for 1994 is: MCMXCIV

# Another example
numeral_converter_58 = IntegerToRoman(58)
result_58 = numeral_converter_58.convert()
print(f"The Roman numeral for 58 is: {result_58}") # Output: The Roman numeral for 58 is: LVIII
