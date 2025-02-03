username = ['Bob', 'Mice', 'Rahul', 'Aditi']
email = ['bob@gmail.com', 'micgmail.com', 'rahul@hotmail.com', 'Aditi@hotmail.com']

dictionary = {username[i]: email[i] for i in range(len(username)) if '@' in email[i]}
print(dictionary)

