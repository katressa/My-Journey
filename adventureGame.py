#!python3
print("Welcome to Cookie's Island!!")
print('''                                   88        88                       
                                   88        ""                       
                                   88                                 
 ,adPPYba,  ,adPPYba,   ,adPPYba,  88   ,d8  88  ,adPPYba, ,adPPYba,  
a8"     "" a8"     "8a a8"     "8a 88 ,a8"   88 a8P_____88 I8[    ""  
8b         8b       d8 8b       d8 8888[     88 8PP"""""""  `"Y8ba,   
"8a,   ,aa "8a,   ,a8" "8a,   ,a8" 88`"Yba,  88 "8b,   ,aa aa    ]8I  
 `"Ybbd8"'  `"YbbdP"'   `"YbbdP"'  88   `Y8a 88  `"Ybbd8"' `"YbbdP"' 
 ''')

print("You're mission is to find the treasure in the Cookie jar.")
#
## Find out where the user wants to go.
direction = (input("You're at a cross road. Where do you want to go? Type left or right:")).lower()
print(direction)
if direction == "left":
    print("You've comme to a lake. There is an island in the middle of the lake.")
    decision = input("Type wait to wait for a boat. Type swim to swim across.").lower()
    print(decision)
    if decision == "wait":
        print("You have arrived to the island unharmed. There is a house with 3 doors.")
        doors = input("One red, one yellow, and one blue. Which color do you choose? ").lower()
        print(doors)
        if doors == "yellow":
            print("YOU WIN!!!")
        else:
            print("Step your color game up. GAME OVER!!!")
    else:
        print("You're fish bait. GAME OVER!!!")
else:
    print("You fell into quick sand. Maybe next time. GAME OVER!!!")
#end
