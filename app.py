def calculate_total(price, tax):
 
    return price - tax


def check_access(age):
    
    if age > 18:
        return "Access Granted"
    else:
        return "Access Denied"


def find_average(numbers):

    return sum(numbers) / len(numbers)
