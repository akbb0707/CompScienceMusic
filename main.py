# Authentication
enteredPlayerName = input("Enter your name: ")
checkPlayersArray = []
with open("players.txt", "r") as checkPlayersFile:
  for line in checkPlayersFile:
    checkPlayersArray.append(line.strip(", 0\n"))

if enteredPlayerName in checkPlayersArray:
  print("Authenticated!\n")
else:
  print("Not Authenticated")
  exit(0)

import random
# Function to add a user to the players file
def addingUser(toAppendName):
    with open("players.txt", "a+") as file_object:
      # Move read cursor to the start of file.
      file_object.seek(0)
      # If file is not empty then append '\n'
      data = file_object.read(100)
      if len(data) > 0 :
          file_object.write("\n")
      # Append text at the end of file
      file_object.write(f"{toAppendName} 0")
      file_object.close()
# Function to add music to the music.txt file
def addingMusic(songName, songArtist):
    with open("music.txt", "a+") as file_object1:
      # Move read cursor to the start of file.
      file_object1.seek(0)
      # If file is not empty then append '\n'
      data = file_object1.read(100)
      if len(data) > 0 :
          file_object1.write("\n")
      # Append text at the end of file
      file_object1.write(f"{songName}, {songArtist}")
      file_object1.close()

# Main options loop
while True:
    choice = input("Enter an option to begin:\n1 - Adding Music\n2 - Adding User\n3 - Continue with existing files\ndone - Finished with this stage\nexit - Exit the program\n>>> ")
    if choice == "1":
        while True:
            songTitle = input("Enter the name of the song to add (type \033[1m/done\033[0m to finish): ")
            if songTitle == "/done":
                break
            songPerson = input("Enter the name of the artist for that song (type \033[1m/done\033[0m to finish): ")
            if songPerson == "/done":
                break
            addingMusic(songTitle, songPerson)
    elif choice == "2":
        while True:
            toAppendName = input("Enter the \033[1mname\033[0m of the new user (Enter \033[1m/done\033[0m to finish): ")
            if toAppendName == "/done":
                break
            addingUser(toAppendName)
    elif choice == "3":
        break
    elif choice == "done":
        break
    elif choice == "exit":
        print("Quitting...")
        exit(0)
    else:
        print("Invalid choice")
        break

try:
    tempSongs = open("music.txt", encoding="utf-8").readlines()
except FileNotFoundError:
    print("Music file not found! Please run the 1st choice on the main menu.")
try:
    tempPlayers = open("players.txt", encoding="utf-8").readlines()
except FileNotFoundError:
    print("No users file found! Please run the 2nd option on the main menu.")
    exit(0)
songs = []
artists = []
players = []
scores = []

for element in tempSongs:
    songs.append(element.strip())
for element1 in tempPlayers:
    players.append(element1.strip())


for iteration, titleAndSong in enumerate(songs):
    try:
        title, artist = titleAndSong.split(", ")
        artists.append(artist)
        songs[iteration] = title
    except ValueError:
        print(f"\033[1mERROR:\033[0m Invalid song file syntax detected at line: \033[1m{int(iteration) + 1}\033[0m of music.txt file")

for iteration1, playerItem in enumerate(players):
    try:
        player, score = playerItem.split(" ")
        players[iteration1] = player
        scores.append(score)
    except ValueError:
        print(f"\033[1mERROR:\033[0m Invalid player file syntax detected at line: \033[1m{int(iteration1) + 1}\033[0m of players.txt file")


# Actual game

for users in range(len(scores)):
  print(f"\nPlayer {players[users]} is playing now\n")
  for z in range(2):
    random_choice = random.randrange(len(songs))
    random_artist = artists[random_choice]
    random_song = songs[random_choice]
    print(f"{random_artist} - {random_song[0]}")
    guess1 = input("Enter the first guess for the song: ")
    if guess1 == str(random_song):
        tempScore = int(scores[users])
        tempScore += 3
        scores[users] = str(tempScore)       
    elif guess1 != str(random_song):
        guess2 = input("One more chance: ")
        if guess2 == random_song:
            tempScore = int(scores[users])
            tempScore += 1
            scores[users] = str(tempScore)

openFile1 = open("players.txt", "a", encoding="utf-8")
openFile1.truncate(0)

for g in range(len(scores)):
    print(f"{players[g]} got a score of {scores[g]}")

for u in range(len(scores)):
    with open("players.txt", "a+") as file_object2:
      # Move read cursor to the start of file.
      file_object2.seek(0)
      # If file is not empty then append '\n'
      data = file_object2.read(100)
      if len(data) > 0 :
          file_object2.write("\n")
      # Append text at the end of file
      file_object2.write(f"{players[u]} {scores[u]}")
      file_object2.close()