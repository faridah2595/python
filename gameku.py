"""introduction"""

print("\nWelcome to Gameku"
      "\nHope you can enjoy"
      "\n=_<")

"""How to play"""
print("\nChoose two number between 1 to 50, "
     "the numbers will equal to 50")


"""proses"""

"""setkan nilai pemboleh ubah"""
max_trials = 10
score = 0
trial = 1

"""ulangan untuk markah"""
for score in range (max_trials):

    """ulangan untuk cubaan"""
    for trial in range (max_trials):

        """input the two numbers"""
        nombor1 = int(input("\nPick a number: "))
        nombor2 = int(input("\nPick another number: "))

        """proses penambahan"""
        x = nombor1 + nombor2

        """jika jawab betul"""
        if x == 50:
            print("\nYou genius!")
            score = score + 1
            trial = max_trials - trial

        else: #jika jawab salah#
            print("\nTry again.")
            score = score - 1
            trial = max_trials - trial

        print ("You have ", trial, "time trials")
        print ("Your score is", score)
    
