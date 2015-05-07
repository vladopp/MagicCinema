import logic
import sys
import time

def helpp():
    print("""
You can use the following magic commands for our magic cinema:
show_movies
show_movie_projection
make_reservation
cancel_reservation
delete_employee
help
exit
abracadabra
""")

def abracadabra():
    print("YOUR COMPUTER IS GOING TO EXPLODE IN 3 SECONDS !!! RUN FOR YOUR LIFE !!!")
    time.sleep(3)
    print("BOOOOOOOM")
    sys.exit()

while True:
    command = input("command>")
    if command == "show_movies":
        logic.show_movies()
    elif command == "show_movie_projection": # to be fixed
        logic.show_movie_projection(movie_id, date=None)
    elif command == "make_reservation":
        logic.make_reservation()
    elif command == "cancel_reservation":
        logic.cancel_reservation()
    elif command == "delete_employee":
        logic.delete_employee()
    elif command == "help":
        helpp()
    elif command == "abracadabra":
        abracadabra()
    elif command == "exit":
        break
