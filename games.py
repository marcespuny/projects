import random

#You walk in a casino with 100 dollars and you bet it on different games.
#After the game results, your bet will be added or discounted depending if you won or lose.

money = 100

#First you bet on guessing heads or tails for a coin toss.

def coin(guess, bet):

    #Will randomly get 1 or 2. Will associate 1 to heads and 2 to tails.

    flip = random.randint(1, 2)

    if flip == 1:
        print('The coin toss result was heads')

    if flip == 2:
        print('The coin toss result was tails')

    if (flip == 1 and guess.lower() == 'heads'):
        print('You guessed heads and you got it right! You won '+ str(bet) +'$!!')
        return +bet

    elif (flip == 2 and guess.lower() == 'tails'):
        print('You guessed tails and you got it right! You won '+ str(bet) +'$!!')
        return +bet

    else:
        print('Your guess was wrong, you lost '+str(bet)+'$!!')
        return -bet

#Now you play cho han, in which 2 dices are rolled and you guess the total ir even or odd.

def chohan(guess, bet):

    #We calculate a random number between 1 and 6 twice and sum the result.

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    result = dice1+dice2

    if (result%2 == 0 and guess.lower() == 'even'):
        print('You guessed even and you got it right! You won '+ str(bet) +'$!!')
        return +bet

    elif (result%2 != 0 and guess.lower() == 'odd'):
        print('You guessed odd and you got it right! You won '+ str(bet) +'$!!')
        return +bet
    else:
        print('Your guess was wrong, you lost '+str(bet)+'$!!')
        return -bet

#Next you and another person pick a card from a deck where higher number wins the bet.

def card(bet):

   #First I build a deck with a comprehension list

   deck = [[i]*4 for i in range(1, 13)]

   #I convert the nested list into a flat list

   cards = [j for i in deck for j in i]

   #I randomly pick a card and take it out of the list so the chances to get the same card again are 0.
   #Lets say that you pick card1.

   card1 = random.choice(cards)
   cards.remove(card1)
   card2 = random.choice(cards)
   cards.remove(card2)

   if card1 > card2:
       print('You got a '+str(card1)+' and the other player got a '+str(card2)+'. You won ' + str(bet) + '$!!')
       return +bet

   elif card1 < card2:
       print('You got a '+str(card1)+' and the other player got a '+str(card2)+'. You lost ' + str(bet) + '$!!')
       return -bet

   else:
       print('It is a tie!')

#Finally you play at the roulette. 36 numbers with different betting options and rewards.
#I am not very familiar with it and I am aware I am forgetting few betting strategies.

def roulette(guess, bet):

    #We want a random number between 0 and 36 and also I will create a list for the numbers in the red zone.

    number = random.randint(0, 36)
    print('The number was '+str(number)+'!!')
    red= [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 29, 32, 34, 36]

    if (guess.lower() == 'even' and number%2 == 0):
        print('You guessed even and you got it right! You won ' + str(bet) + '$!!')
        return +bet

    elif (guess.lower() == 'odd' and number%2 != 0):
        print('You guessed odd and you got it right! You won ' + str(bet) + '$!!')
        return +bet

    elif guess == number:
        print('YOU GOT THE NUMBER RIGHT!! YOU WON '+str(bet)*35+' $$$!!!')
        return +(bet*35)

    elif guess.lower() == 'red' and number in red:
        print('You guessed red and you got it right! You won ' + str(bet) + '$!!')
        return +bet

    elif guess.lower() == 'black' and number not in red:
        print('You guessed black and you got it right! You won ' + str(bet) + '$!!')
        return +bet

    else:
        print('Your guess was wrong, you lost ' + str(bet) + '$!!')
        return -bet

#It is time to place your bets on the different games, keep in mind that if you run out of money you cannot continue.
#The total money will be printed at the end of the last best.

if money > 0:
    money += coin("heads", 10)
    print('You have '+str(money)+' $ left')
else:
    print('You are broke, go home!')

if money > 0:
    money += chohan("ODD", 10)
    print('You have '+str(money)+' $ left')
else:
    print('You are broke, go home!')

if money > 0:
    money += card(10)
    print('You have '+str(money)+' $ left')
else:
    print('You are broke, go home!')

if money > 0:
   money += roulette("black", 10)
else:
    print('You are broke, go home!')

print('You finished your gambling session with '+str(money)+' $ left')