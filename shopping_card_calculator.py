print('        SHOPPING CART CALCULATOR')
print('-'*40)
def calculate_item_total(quantity, unit_price):
    return quantity * unit_price

def apply_bulk_discount(total, quantity):
    if quantity >= 10:
        return total * 0.10  # 10% discount
    elif quantity >= 5:
        return total * 0.05  # 5% discount
    else:
        return 0

def calculate_tax(subtotal, tax_rate):
    return subtotal * tax_rate / 100

def is_eligible_for_free_shipping(subtotal):
    return subtotal >= 50

def process_order(item_name, quantity, unit_price, tax_rate):
    item_total = calculate_item_total(quantity, unit_price)
    discount = apply_bulk_discount(item_total, quantity)
    subtotal = item_total - discount
    tax = calculate_tax(subtotal, tax_rate)
    final_total = subtotal + tax
    print(f'Order receipt for: {item_name}')
    print(f' Quantity: {quantity}@  ${unit_price:.2f} each')
    print(f' Item total: ${item_total:.2f}')
    if discount > 0 :
        print(f' Bulk dicount: -${discount:.2f}')  
    print(f' Subtotal: ${subtotal} ')
    print(f' Tax({tax_rate}%): {tax:.2f}')
    print(f' Final total: {final_total:.2f}')
    if is_eligible_for_free_shipping(subtotal):
          print(f" Eligible for free shipping")
    else:
        need_more = 50-subtotal
        print(f' Need ${need_more:.2f} more for free shipping')
    print('-'*40)

process_order("Notebooks", 12, 3.50 , 8)
process_order("Pens", 6 , 1.25 , 8)
process_order("Paper", 3 , 4.99 , 8)



        


    

