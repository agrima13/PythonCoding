import string
my_string = "####Hey This is, my string !!!!!"

new_string = my_string.translate(str.maketrans('','',string.punctuation))
print(new_string)