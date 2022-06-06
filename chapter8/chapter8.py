# def NAME_OF_FUNCTION(PARAMETERS):
    # these line
    # belong
    # to the code block
    # for the function

#def say_hello(name, age):
    print(f"hello {name} you are {age} years old")

#def say_goodbye():
    print("Goodbye")

#def greet_back(feeling):
    if feeling == 'good':
        print("Awesome I feel good too")
    elif feeling == 'bad':
        print("I am so sorry")
    elif feeling == 'stressed':
        print("Coding can be hard to learn")
    else:
        print("Well, have a good day")

# Driver Code
#while True:
    response = input("What do you want to do? Say hello [h] Say Goodbye [g]"
    "talk to me [t], quit [q]")
    if response.lower() == 'q':
        say_goodbye()
        break
    elif response.lower() == 'h':
        n = input("What is your name? ")
        a = input("What is your age? ")
        say_hello(n, a)
    elif response.lower() == 'g':
        say_goodbye()
    elif response.lower() == 't':
        f = input("How are you today? ")
        greet_back(f)
    else:
        print("invalid input")



# Let's try another example...
def my_function(num):
    while num < 10:
        print(num)
        if num == 6:
            return
        num += 1

my_function(4)