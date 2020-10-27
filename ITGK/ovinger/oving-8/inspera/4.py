def smallify_words(objects):
    for i in range(len(objects)):
        objects[i] = objects[i].lower()
    return objects

#print(smallify_words(['INDØK','ER','HOMO']))

def get_five_objects():
    while True:
        str1 = input("Enter five objects separated by ';': ")
        obj = str1.split(';')
        if len(obj) == 5:
            return obj
        print('You where supposed to enter FIVE objects, not '+str(len(obj))+'. Try again.')

#print(get_five_objects())

def play_game():
    words = smallify_words(get_five_objects())
    while len(words):
        guess = input('Guess a word ')
        if guess.lower() == 'quit': break

        if guess.lower() in words:
            print(guess,'was a correct word!')
            words.remove(guess)
            if not len(words):
                print('You did it! you remembered all the objects')
        else:
            print(guess, 'was a wrong guess')


play_game()