import string


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, illegal_character, position):
        self.illegal_character = illegal_character
        self.position = position

    def __str__(self):
        return f"The username contains an illegal character '{self.illegal_character}' at position {self.position}"


class UsernameTooShort(Exception):
    def __str__(self):
        return "The username is too short"


class UsernameTooLong(Exception):
    def __str__(self):
        return "The username is too long"


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "The password is missing a character"


class MissingCapitalLetter(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"


class MissingSmallLetter(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"


class MissingNumber(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"


class MissingSpecialCharacter(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)"


class PasswordTooShort(Exception):
    def __str__(self):
        return "The password is too short"


class PasswordTooLong(Exception):
    def __str__(self):
        return "The password is too long"


def check_input(username, password):
    # Check username
    legal_characters = string.ascii_letters + string.digits + "_"
    for char in username:
        if char not in legal_characters:
            raise UsernameContainsIllegalCharacter(char, username.index(char))
    if len(username) < 3:
        raise UsernameTooShort()
    if len(username) > 16:
        raise UsernameTooLong()

    # Check password
    mandatory_characters = [string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation]
    for char_type in mandatory_characters:
        if not any(char in password for char in char_type):
            if char_type == string.ascii_uppercase:
                raise MissingCapitalLetter()
            elif char_type == string.ascii_lowercase:
                raise MissingSmallLetter()
            elif char_type == string.digits:
                raise MissingNumber()
            elif char_type == string.punctuation:
                raise MissingSpecialCharacter()
    if len(password) < 8:
        raise PasswordTooShort()
    if len(password) > 40:
        raise PasswordTooLong()

    print("OK")


def main():
    # # Testing
    # check_input("1", "2") -> The username is too short
    # check_input("0123456789ABCDEFG", "2") -> The username is too long
    # check_input("A_a1.", "12345678") -> The username contains an illegal character '.' at position 4
    # check_input("A_1", "2") -> The password is missing a character (Uppercase)
    # check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary") -> The password is missing a character (Digit)
    # check_input("A_1", "abcdefghijklmnop") -> The password is missing a character (Uppercase)
    # check_input("A_1", "ABCDEFGHIJLKMNOP") -> The password is missing a character (Lowercase)
    # check_input("A_1", "ABCDEFGhijklmnop") -> The password is missing a character (Digit)
    # check_input("A_1", "4BCD3F6h1jk1mn0p") -> The password is missing a character (Special)
    # check_input("A_1", "4BCD3F6.1jk1mn0p") -> OK
    # # End testing
    while True:
        try:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            check_input(username, password)
            break
        except UsernameContainsIllegalCharacter as e:
            print(e)
        except UsernameTooShort as e:
            print(e)
        except UsernameTooLong as e:
            print(e)
        except PasswordMissingCharacter as e:
            print(e)
        except PasswordTooShort as e:
            print(e)
        except PasswordTooLong as e:
            print(e)


if __name__ == "__main__":
    main()
