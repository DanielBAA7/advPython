class IDIterator:
    def __init__(self, id):
        self._id = id

    def __iter__(self):
        return self

    def __next__(self):
        if self._id == 999999999:
            raise StopIteration
        self._id += 1
        while not check_id_valid(self._id):
            self._id += 1
        return self._id


def check_id_valid(id_number):
    digits = [int(digit) for digit in str(id_number)]
    multiplied_digits = [digit * (2 if (index+1) % 2 == 0 else 1) for index, digit in enumerate(digits)]
    summed_digits = [digit // 10 + digit % 10 if digit > 9 else digit for digit in multiplied_digits]
    return sum(summed_digits) % 10 == 0


def id_generator(id_number):
    while id_number < 999999999:
        id_number += 1
        while not check_id_valid(id_number):
            id_number += 1
        yield id_number


def main():
    id_number = int(input("Enter ID: "))
    method = input("Enter 'it' for iterator or 'gen' for generator: ")

    if method == "it":
        iterator = IDIterator(id_number)
        for i in range(10):
            print(next(iterator))
    elif method == "gen":
        generator = id_generator(id_number)
        for i in range(10):
            print(next(generator))
    else:
        print("Invalid input. Please enter 'it' or 'gen'.")

# TEST
    # Enter ID: 123456780
    # Enter
    # 'it'
    # for iterator or 'gen' for generator: gen
    # 123456782
    # 123456790
    # 123456808
    # 123456816
    # 123456824
    # 123456832
    # 123456840
    # 123456857
    # 123456865
    # 123456873
# END TEST

if __name__ == "__main__":
    main()
