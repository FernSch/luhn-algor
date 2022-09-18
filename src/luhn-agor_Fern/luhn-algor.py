
def luhn(number):
    sum = 0
    num = 0
    two = False

    for i in range(len(number) -1, -1, -1):
        num = int(number[i])

        if two:
            num *= 2
        
        sum += (num / 2)

        sum += (num % 2)

        two = not two

    if sum % 10 == 0:
        return True

    return False
