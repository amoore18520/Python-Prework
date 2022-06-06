# The While Loop
# while boolean or boolean expression:
    # code block
    # to run while
    # condition is true

# You must be over 5 feet to ride my ride
# I have a magic potion that will let you grow one inch every time you use it!

#height = int(input("What is your height? "))
#while height < 60:
    #height += 1
    #if height < 58:
        #continue
    #print(f"You are {height} inches tall \n and too short to ride!")
    #print("Drink my magic potion")

#print("Thanks for coming!")

while True:
    response = input("What do you want to do? Say hi [h], Say goodbye [g], or Quit? [q]")
    if response.lower() == 'h':
        print("hello")
    elif response.lower() == 'g':
        print("goodbye")
    elif response.lower() == 'q':
        break
    else:
        print("invalid option")