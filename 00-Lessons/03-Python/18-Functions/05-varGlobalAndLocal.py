payment = 20000

def payment_extra(extra):
    global payment #global variable
    payment += extra
    return payment

print(payment_extra(5000))  # Output: 25000