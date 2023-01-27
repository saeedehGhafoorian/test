import random
sysGam = ['rock', 'paper', 'scssiors']
userGam = {'rock':'r', 'paper':'p', 'scssiors':' s', 'quit' : 'q' }
checkwhile = 0
userRate = 0
sysRate = 0
#inp = input('chand bar mikhai bazi konid?')

    #==================================
while True:
    inp = input('chand bar mikhai bazi konid?')
    if inp.isdigit():
        check = int(inp)
        break
    elif inp == 'q'.lower() or inp == 'quit'.lower():
        print('by')
    elif  not inp.isdigit() and not inp == 'q':
        print('number')
    #inp = input('chand bar mikhai bazi konid?')
#====================================
while True:
    userChoice = input('rock, paper, scssiors or q (quite)')
    userChoice = userChoice.lower()
    sysChoice = random.choice(sysGam)

    #====================================

    if userChoice == 'rock' and sysChoice == 'paper':
        print('sys')
        sysRate += 1
        checkwhile += 1
        print(f"{userRate}-{sysRate}")
    elif userChoice == 'rock' and sysChoice == 'scssiors':
        print('user')
        userRate += 1
        checkwhile += 1
        print(f"{userRate}-{sysRate}")
    elif userChoice == sysChoice :
        print('mosavi')
        checkwhile += 1
        print(f"{userRate}-{sysRate}")
    # ====================================

    elif userChoice == 'paper' and sysChoice == 'rock':
        print('user')
        userRate += 1
        checkwhile += 1
        print(f"{userRate}-{sysRate}")
    elif userChoice == 'paper' and sysChoice == 'scssiors':
        print('sys')
        sysRate += 1
        checkwhile += 1
        print(f"{userRate}-{sysRate}")

    #====================================

    elif userChoice == 'scssiors' and sysChoice == 'rock':
        print('sys')
        sysRate += 1
        checkwhile += 1
        print(f"{userRate}-{sysRate}")
    elif userChoice == 'scssiors' and sysChoice == 'paper':
        print('user')
        userRate += 1
        checkwhile += 1
        print(f"{userRate}-{sysRate}")

    #====================================

    elif userChoice == 'q' or 'quite':
        print('bye')
        break
    # ====================================
    else:
        print('dorost vared konid')
    userChoice = input('rock, paper, scssiors or q (quite)')
    # ====================================
while True:
    if checkwhile == int(inp):
        break

    if sysRate < userRate:
            print('won user, los sys')
    elif userRate > sysRate:
            print('user')
        # else:
        # print('equal')

    #====================================
for check in checkwhile:
    if checkwhile == int(inp):
        continue
    if sysRate < userRate:
        print('won user, los sys')
    elif userRate > sysRate:
        print('user')
    else:
        print('equal')


    #========================================
print(f"youRate:{userRate}\nsyatemRate:{sysRate}")






