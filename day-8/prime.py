number = int(input("Check if a number is prime: "))

prime_msg = " is a prime number"
not_prime_msg = " is not a prime number"

def prime_number(number):
    whole_number_counter = 0
    for current_number in range(1, 100):
        whole_number_counter += 1 if (number / current_number).is_integer() else 0
    
    print(f"{number}{not_prime_msg}") if whole_number_counter > 2 else print(f"{number}{prime_msg}")

prime_number(number)