import string


class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = list(letters)

    def print(self):
        print(f"Літери алфавіту ({self.lang}): {' '.join(self.letters)}")

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    
    __letters_num = 26

    def __init__(self):
        super().__init__("En", string.ascii_uppercase)

    def is_en_letter(self, letter):
        return letter.upper() in self.letters

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example():
        
        return "This is text example."


if __name__ == "__main__":
    eng_alphabet = EngAlphabet()
    eng_alphabet.print()
    print(f"Кількість літер: {eng_alphabet.letters_num()}")

    letter_1 = "F"
    print(
        f"Чи належить '{letter_1}' до алфавіту? {eng_alphabet.is_en_letter(letter_1)}"
    )

    letter_2 = "Щ"
    print(
        f"Чи належить '{letter_2}' до алфавіту? {eng_alphabet.is_en_letter(letter_2)}"
    )

    print(f"Приклад тексту: {EngAlphabet.example()}")