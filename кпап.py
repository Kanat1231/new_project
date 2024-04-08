import string

def count_letters(name):
        vowels = 'аәеэёоөұүыіуи'
        consonants = 'бвгғджзкқлмнңпрстфхцчшщ'

        name = name.lower()
        vowel_count = sum(1 for letter in name if letter in vowels)
        consonant_count: int = sum(1 for letter in name if letter in consonants)

        return vowel_count, consonant_count

name = "Дәулетбай Қанат Қуанышұлы"
vowel_count, consonant_count = count_letters(name)
print(f"Дауысты: {vowel_count}")
print(f"Дауыссыз: {consonant_count}")

