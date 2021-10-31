started = False
command = ""
while True:
    input_command = input("> ")
    command = input_command.upper()
    if command == "HELP":
        print( "start - to start the car\n"
               "stop - to stop the car\n"
               "quit - to exit")
    elif command == "START":
        if started:
            print("Car already start")
        else:
            started = True
            print("Car start.....Ready to go!")
    elif command == "STOP":
        if not started:
            print("Car already stopped")
        else:
            started = False
            print("Car stopped")
    elif command == "QUIT":
        break
    else:
        print("I don't understand that")