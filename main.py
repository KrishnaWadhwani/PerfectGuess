import random
def perfectguess():
    count = 0
    num = random.randint(1,100)
    print('Hey, Welcome To PerfectGuess')
    print('Here You Have The Number If Number Is Right Then This Game Will End')
    print('The Guesses Are From 1 To 100')
    print('Write "999" For More Info And How To Play')

    while True:
        a = int(input('Guess The Number: '))
        if a == 999:
            print('Just Guess The Number From 1 To 100, In The Game Where It Says "Guess The Number: "')
            print('If The Number Is Right The Game Will End Else Continue')
            print('Write "return" To Continue The Game')
            print('Write "hiscore" To Know The High Score')
            hc = str(input('>>> '))
            q = 'return'
            if hc == q:
                perfectguess()
            if hc == 'hiscore':
                with open('worldrecord.txt', 'r') as f:
                    hiscore2 = int(f.read())
                print(f'This Is The High Score {hiscore2}')
                hs = str(input('>>>'))
                if hs == q:
                    perfectguess()
                else:
                    perfectguess()
        if a == num:
            count +=1
            print(f'Wallah You Guessed It Congratulation The Number Was: {num}')
            print(f"You Did It In {count} Tries")
            with open('worldrecord.txt', 'r') as f:
                hiscore = int(f.read())
            if count<hiscore:
                with open('worldrecord.txt', "w") as f:
                    print(f'Yea, You Have Broken The High Score Of {hiscore} Tries, And Set A New High Score Of {count} Tries')
                    f.write(str(count))
            print('Print "restart" To Restart The Game Or "quit" To Quit The Game')
            ase = input('>>> ')
            if ase == 'restart':
                perfectguess()
            else:
                break
        elif a < num:
            count += 1
            print(f'Hmmmm, {a} Is Not The Right Number Please Increase It')

        elif a > num:
            count += 1
            print(f'Ohh, You Messed Up, {a} Is Not That Hidden Number Please Decrease It')
perfectguess()
