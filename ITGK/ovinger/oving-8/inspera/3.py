songs = [("You hear the door slam. And realize there's nowhere left to", "run"),
         ("Oh, I wanna dance with somebody. I wanna feel the",  "heat"),
         ("There's a fire starting in my heart. Reaching a fever", "pitch"),
         ("Hey, I just met you and this is crazy. But here's my", "number"),
         ("'Cause baby, you're a firework. Come on, show 'em what you're", "worth")]
import random
def pop_random_songs(songs):
    random_number = random.randint(0,len(songs)-1)

    popped_song = songs[random_number]
    songs.pop(random_number)
    return popped_song

#print(pop_random_songs(songs))

def song_contest(songs):
    while len(songs):
        random_song = pop_random_songs(songs)
        print('The lyrics are:')
        print(random_song[0])
        while True:
            svar = input('What is the next word? ').lower()
            if svar == random_song[1].lower():
                print('Correct!')
                break
            print('Wrong guess. Try again')
        if not len(songs):
            print('Congrats, music lover! you have guessed everything correct')
            break
        try_again = input('Do you want to go again? (y/n) ').lower()
        if try_again == 'n':
            break

song_contest(songs)