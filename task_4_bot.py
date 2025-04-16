# decorator
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter username and phone number."
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    return inner

# parse command and arguments
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# add name phone
@input_error
def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    else:
        raise ValueError

# change username phone
@input_error
def change_contact(args, contacts):
    if len(args) == 2:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return "Contact updated."
        else:
            raise KeyError
    else:
        raise ValueError

# phone username
@input_error
def show_phone(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            raise KeyError
    else:
        raise ValueError

# all
@input_error
def show_all(contacts):
    if contacts:
        result = "All contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()
    else:
        return "No contacts saved yet."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

''' INPUT -> OUTPUT:
Welcome to the assistant bot!
Enter a command: add
Give me name and phone please.
Enter a command: add Bob
Give me name and phone please.
Enter a command: add Bob +489997777
Contact added.
Enter a command: phone
Give me name and phone please.
Enter a command: Bob +480001111
Invalid command.
Enter a command: add Mike +7777777777
Contact added.
Enter a command: hello
How can I help you?
Enter a command: change
Give me name and phone please.
Enter a command: change Gleb +9999999999
Contact not found.
Enter a command: change Mike +3800000001
Contact updated.
Enter a command: all
All contacts:
Bob: +489997777
Mike: +3800000001
Enter a command: stramge_command
Invalid command.
Enter a command: exit
Good bye!
'''