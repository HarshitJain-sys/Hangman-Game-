#Hangman Game Python
import random
print("Test Change")
print("Sample Change")
words=("apple","orange","banana","coconut","pineapple","grape","strawberry","watermelon","peach","kiwi")
#dictionary of key():-
hangman_art={0: ("  ",
                 "  ",
                 "  "),
             1: (" o ",
                 "   ",
                 "   "),
             2: (" o ",
                 " | ",
                 "   "),
             3: (" o ",
                 "/| ",
                 "   "),
             4: (" o ",
                 "/|\\",
                 "   "),
             5: (" o ",
                 "/|\\",
                 "/   "),
             6: (" o ",
                 "/|\\",
                 "/ \\")}
def dis_man(wrong_guess):
    print("*********************")
    for line in hangman_art[wrong_guess]:
        print(line)
    print("*********************")
def display_hint(hint):
    print(" ".join(hint))
def display_ans(ans):
  print(" ".join(ans))
def main():
    ans=random.choice(words)
    hint=["_"]*len(ans)
    wrong_guess=0
    guessed_letter=set()
    is_Running=True
    while is_Running:
        dis_man(wrong_guess)
        display_hint(hint)
        guess=input("Enter A Letter : ").lower()
        if len(guess)!=1 or not guess.isalpha():
            print("Invalid Input")
            continue
        if guess in guessed_letter:
            print(f"{guess} is already guessed")
            continue
        guessed_letter.add(guess)
        if guess  in ans :
            for i in range(len(ans)):
                if ans[i]==guess:
                    hint[i]=guess
        else:
            wrong_guess+=1
        if "_" not in hint:
            dis_man(wrong_guess)
            display_ans(ans)
            print("You Win!!!")
        elif wrong_guess>=len(hangman_art)-1:
            dis_man(wrong_guess)
            display_ans(ans)
            print("Hangman!!!!")
            is_Running=False
if __name__=="__main__":
    main()