print('Welcome to KayCee grocery store!!')

def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount = ((100-discount_percentage)/100) * price;
    else:
        return f'Discount does not apply, price ${price} '
    return f'Discount applied of {discount_percentage} to the product price of ${price}- total price= ${discount}'


num1 = int(input('enter the price of the product \t'))
num2 = int(input('enter the discount given of the product \t'))

print(calculate_discount(num1,num2));

print('Thank you for shopping, please come back again')

