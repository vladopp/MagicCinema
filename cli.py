import logic

while True:
    command = input("command>")
    command = command.split(sep=" ")

    if command[0] == "show_movies":
        logic.show_movies()

    elif command[0] == "show_movie_projections":
        if len(command) == 2:
            logic.show_movie_projections(int(command[1]))
        elif len(command) == 3:
            logic.show_movie_projections(int(command[1]), date=int(command[2]))

    elif command[0] == "make_reservation":
        logic.make_reservation()

    elif command[0] == "cancel_reservation":
        logic.cancel_reservation(command[1])

    elif command[0] == "help":
        logic.helpp()

    elif command[0] == "abracadabra":
        logic.abracadabra()

    elif command[0] == "exit":
        break
