def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    return sum(1 for char in sentence if char in vowels)

def main():
    sentence = input("Enter a sentence: ")

    while True:
        print("\nChoose an operation:")
        print("1. Reverse the sentence")
        print("2. Count vowels")
        print("3. Check if palindrome")
        print("4. Find and replace a word")
        print("5. Format (title case)")
        print("6. Split into words")
        print("7. Word frequency counter")
        print("8. Swap case")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Reversed:", sentence[::-1])

        elif choice == "2":
            print("Vowel count:", count_vowels(sentence))

        elif choice == "3":
            cleaned = "".join(c.lower() for c in sentence if c.isalnum())
            if cleaned == cleaned[::-1]:
                print("Yes, it's a palindrome.")
            else:
                print("No, it's not a palindrome.")

        elif choice == "4":
            word_to_find = input("Enter the word to find: ")
            word_to_replace = input("Enter the word to replace it with: ")

            words = sentence.split()
            new_words = []
            replaced = False

            for word in words:
                if word.lower() == word_to_find.lower():
                    new_words.append(word_to_replace)
                    replaced = True
                else:
                    new_words.append(word)

            if replaced:
                sentence = " ".join(new_words)
                print("Updated sentence:", sentence)
            else:
                print(f"The word '{word_to_find}' was not found in the sentence.")

        elif choice == "5":
            sentence = sentence.title()
            print("Title case:", sentence)

        elif choice == "6":
            print("Words:", sentence.split())

        elif choice == "7":
            words = sentence.split()
            freq = {}
            for word in words:
                freq[word.lower()] = freq.get(word.lower(), 0) + 1
            print("Word frequency:", freq)

        elif choice == "8":
            sentence = sentence.swapcase()
            print("Swapped case:", sentence)

        elif choice == "9":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
