def even(x):
    if x % 2 == 0:
        return True
    else:
        return False
def num_even():
    user = input("Do you want a odd ticket or even ticket?")
    for number in range(0,21):
        if user == "even":
            if even(number):
                print(number)
        if user == "odd":
           if not even(number):
                print(number)



num_even()
