import logic

while True:
    command = input("command>")
    if command == "show_movies":
        logic.show_movies()
    elif command == "show_movies": # to be fixed
        logic.show_movies(movie_id, date=None)
    elif command == "make_reservation":
        logic.make_reservation()
    elif command == "cancel_reservation":
        logic.cancel_reservation()
    elif command == "delete_employee":
        logic.delete_employee()
    elif command == "help":
        logic.helpp()
    elif command == "exit":
        break
