import random
while True:
    words = ["apple", "star", "king", "check ", "code"]
    word = random.choice(words)
    
    guessed = []
    attempts = 6
    while attempts > 0:
        display = "  "
        
        for letter in word:  
            if letter in guessed:  
                display += letter + " "  
            else:  
                display += " _ "  
        
        print("\nWord:", display)  
        
        if " _ " not in display:
            print("YOU WIN THE GAME")
            break;
        
        guess=input("Enter a letter:").lower()
        if guess in word:
            guessed.append(guess)
            print("Correct")
        else:
            attempts-=1
            print("Worng!,You Loose the chancess remain you have ",attempts)
    if attempts==0:
        print("The game is over try next time")
        print("The scerate word is :",word)
        
    
    agine=input("play agine(yes/no) ?")
    if agine.lower()!="yes":
        print("good byee ,You exit the game")
        break
    