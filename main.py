from wordings import *

class Data:
    pass

class Commands:
    def execute(self, text):
        pass

def main() -> None:
    commands = Commands()
    print(w_start)
    print(w_commands)
    while True:
        try:
            user_cmd = input("Введите номер операции >> ")
            commands.execute(user_cmd)
        except KeyboardInterrupt:
            print(w_goodbye)
            exit(0)


if __name__ == "__main__":
    main()
