# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
sum_names = len(names)
random_choice = random.randint(0, sum_names - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy a meal today.")


# print(sum_names)






