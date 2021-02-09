idk = {
    'a': 1,
    'b': 2
}

updated_dict = {key:value**2 for key, value in idk.items()}
number_dict = {num:num*2 for num in [1,2,3]}
print(updated_dict)
print(number_dict)