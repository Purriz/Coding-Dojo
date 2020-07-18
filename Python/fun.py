## Data Types

num = 10

# Number
# +, -, *, /, %

# String
name = "Matt"

print(num)
print(name)

# Boolean
result = True

#  Lists
students = ["Amy", "Thomas", "Natalie", "Saneeta"]

print(len(students))

students.append("Matt")

students.pop()

print(students)

# Prints "Thomas"
print(students[1])

# Dictionaries
bad_guy = {
    'health': 500,
    'name': "Ka' Thar",
    'attack': 'Mace Smash'
}

# name = 'attack'

print(bad_guy['attack'])

bad_guy['attack'] = 'Mace Super Smash'

print(bad_guy['attack'])

# Loops/Conditionals

students = ["Amy", "Thomas", "Natalie", "Saneeta"]

post = {
    'post': "Odion",
    'content': "omg this python class won't end!",
    'post_date': '07/07/20'
}

for thing in post:
    count+=1
    print(f"Object attr: {banana}, Object value: {post[banana]}")
    print(count)


# for(let i =0; i<250; i++){
# }

for banana in range(len(students)):
    print(f"This is the index: {i}, This is the value: {students[i]}")

def print_name_return_ten(name):
    print(name)
    if name == "Ka'Thar":
        return "You have run into the boss"
    elif name == "Michael":
        return "Oh no.. run"
    else:
        return 10

print(print_name_return_ten("Kyle"))

# pay attention to directory