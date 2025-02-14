
age_list = [19, 50, 8, 34, 5, 41]
def get_age_list(x):
    if x>18:
        return True
    else:
        return False
age = filter(get_age_list, age_list)
print(list(age))
print(age)
print(type(age))

