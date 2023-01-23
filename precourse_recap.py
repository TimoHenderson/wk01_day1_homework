def full_name(first_name, last_name):
    return first_name + " " + last_name

def num_bananas_left(bought, eaten):
    return bought - eaten

def have_bananas(bought, eaten):
    if num_bananas_left(bought, eaten) > 0:
        return True
    else:
        return False

def enough_bananas(num_bananas, friends):
    bananas_each = num_bananas / friends
    if bananas_each == 1:
        return "You have the perfect number of bananas for you and your friends!"
    elif bananas_each > 1:
        whole_bananas_each = num_bananas // friends
        bananas_left = num_bananas % friends
        return f"You can have {whole_bananas_each} bananas each and have {bananas_left} left over!"
    else:
        return f"You can only have {bananas_each} bananas each. Better get more bananas or you'll lose friends!"

my_first_name = input("What's your first name?: ")
my_last_name = input("What's your last name?: ")
friends = int(input("How many friends do you have?: "))
bananas_bought = int(input("How many bananas have you bought? "))
bananas_eaten = int(input("How many bananas have you eaten?" ))

bananas_left = num_bananas_left(bananas_bought,bananas_eaten)


print("Your name is " + full_name(my_first_name, my_last_name))
print(f"You have {friends} friends")
print(enough_bananas(bananas_left,friends))
