# Control Flow and Logical Operators

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You`re at a crossroad, where do you want to go? Left or Right? ").lower()

if choice1 == 'left':
    print("You're at a lake. There is an island in the middle of the lake.")
    choice2 = input("Type 'Wait' to wait for a boat. Type 'Swim' to swim and cross the lake: ").lower()
    if choice2 == "wait":
        print("Nice, you made it to the next level, you're pretty good at this!")

        print("Welcome to bear land")
        print('''
                  _                     
                  | |                    
                  | |__   ___  __ _ _ __ 
                  | '_ \ / _ \/ _` | '__|
                  | |_) |  __/ (_| | |   
                  |_.__/ \___|\__,_|_|   
                              ''')

        choice3 = input("Now that you've made it to Treasure Island, you can dig or search the cave. \n Type Dig/Cave: ").lower()
        if choice3 == "dig":
          print("You've found the treasure, you win!")
        elif choice3 == "cave":
            print('''
                                     .
                                 _.:/ )
               _              .-Q      `._
            '\(o7/'         o(.__         '-.
            `.( ).'           `_/    )
               H       ._      '-._.'         
               w       ( \         /
                        \ '.     .'   )
    
                  ''')
            print("You were eaten by a bear, game over.")
    else:
        print('''
                        (`.
                        \ `.
                          )  `._..---._
        \`.       __...---`         o  )
        \ `._,--'           ,    ___,'
          ) ,-._          \  )   _,-'
        /,'    ``--.._____\/--''
            ''')
        print("Unfortunately, you were eaten by a Great White Shark, try again.")

else:
    print('''
'o <_
` /\
   |
  //
''')
    print("You fall into a trap. You died.")
