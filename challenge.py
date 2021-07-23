######################################################
# Part 1: Most Clocks are Normal, But Some are Cuckoo

time = 22
# Complete the prompt here
if (time < 9):
    print('Morning is wonderful. Its only drawback is that it comes at such an inconvenient time of day.')
elif(time <= 16):
    print('Working hard or hardly working?')
elif(time < 20):
    print('How did it get so late so soon?')
elif(time < 22):
    print('A day without sunshine is like, you know, night.')
else:
    print('Burning the midnight oil!')
######################################################
# Part 2: I Came, I 'Saur, I Conquered

angry = True
bored = True
hungry = False
tired = False

# Complete the prompt here
# Example `if` statement:
if (bored and angry and hungry):
    print('T-Rex eats the Triceratops')
elif(tired and hungry):
    print('Trex eats the iguanadon')
elif(hungry and bored):
    print('trex eats the stegasaurus')
elif(tired):
    print('trex goes to sleep')
elif(angry and bored):
    print('trex fights the velociraptor')
elif(angry or bored):
    print('trex roars')
else:
    print('trex has a toothy smile')

######################################################
# Part 3: IOU

disney_characters = ['simba', 'ariel', 'pumba',
                     'flounder', 'nala', 'ursula', 'scar', 'flotsam', 'timon']

# Complete the prompt here

for character in disney_characters:
    if('i' in character):
        print(f'{character} i bet youre impressively intelligent')
    elif('u' in character):
        print(f'{character} u are so uniquely u')
    elif('u' in character):
        print(f'{character} O my how original')
    else:
        print(f"{character} ehh, a's and e's are so oridinary")


######################################################
# Part 4: If You're Cold, Sit in a Corner. It's 90 Degrees!

temperature = 90

while(temperature > 75):
    print(f'the tempature is {temperature}, crank the AC!')
    temperature -= 3
print('75 ahh, thats better')

# Complete the prompt here
