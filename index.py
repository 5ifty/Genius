import json
import requests
import time


def welcome():


    print("Welcome to the Genius CMD app!")
    main()

def main():
    request = input("Please enter the song you would like to hear!")
    no_list = ["No", "no", "n"]
    conti = ["Contiune", "continue"]
    url = f"https://some-random-api.ml/lyrics?title={request}"
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)       # API stuff.
    title = parsed["title"]
    song = parsed["lyrics"]
    artist = parsed["author"]       # Making variables to make life easier later (F strings)

    print(f'\n \n Your search result best matched this title "{title}". \n This songs artist is {artist} \n \n \n \n \n \n \n ')
    print(song.replace('\\n', '\n'))    # basically in the API it returns `\n` for every new line. Using this it returns every \n in the api to an actuall newline.

    cont = input("\n\n\nIf you would like to search another songs lyrics, please type continue. If not please type No to exit the terminal.")
    if cont in no_list:     # I told you it would make sense. If the input is in the no_list it will exit. If not it will return to the start.
        print("Thank you for using the Genius terminal, made by 5ifty @  www.Github.com/5ifty/. ")
        print("Closing in 5 seconds")
        time.sleep(5)
        exit()
    if cont in conti:
        main()
    else:
        print("Unclear input , returning to start!")
        welcome()





welcome()
