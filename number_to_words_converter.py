# Function to convert numbers to words
def num_to_words(n, suffix):
    single_digits = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    two_digits = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens_multiple = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    if n == 0:
        return ""
    if n < 10:
        return single_digits[n] + suffix
    elif n < 20:
        return two_digits[n - 10] + suffix
    elif n < 100:
        return tens_multiple[n // 10] + (" " + single_digits[n % 10] if n % 10 != 0 else "") + suffix
    elif n < 1000:
        return single_digits[n // 100] + " Hundred " + (num_to_words(n % 100, "") if n % 100 != 0 else "") + suffix

# Main function to convert a number into words
def number_to_words(num):
    if num == 0:
        return "Zero"

    # Define larger units
    billion = num // 1000000000
    million = (num // 1000000) % 1000
    thousand = (num // 1000) % 1000
    remainder = num % 1000

    result = ""
    
    # Process each part (billion, million, thousand, and remainder)
    if billion > 0:
        result += num_to_words(billion, " Billion ")
    if million > 0:
        result += num_to_words(million, " Million ")
    if thousand > 0:
        result += num_to_words(thousand, " Thousand ")
    if remainder > 0:
        result += num_to_words(remainder, "")

    return result.strip()

# Input from the user
num = int(input("Enter an integer: "))

# Output the number in words
print("Number in words:", number_to_words(num))
