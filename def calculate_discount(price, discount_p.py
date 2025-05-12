def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying the discount.
    Only apply the discount if it is 20% or higher.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

def apply_tax(price, tax_percent):
    """
    Apply tax to the price.
    """
    tax_amount = price * (tax_percent / 100)
    return price + tax_amount

def main():
    total_price = 0
    total_items = int(input("Enter the number of items: "))
    
    for i in range(total_items):
        print(f"\nItem {i+1}:")
        try:
            price = float(input("Enter the original price of the item: "))
