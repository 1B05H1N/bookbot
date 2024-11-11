import os
from collections import Counter

def list_books(directory):
    # List all files in the given directory
    try:
        books = os.listdir(directory)
        if not books:
            print("No books found in the directory.")
            return []
        print("Available books:")
        for idx, book in enumerate(books):
            print(f"{idx + 1}. {book}")
        return books
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
        return []

def choose_book(books):
    # Prompt user to choose a book by index
    while True:
        try:
            choice = int(input("Enter the number of the book you want to read: ")) - 1
            if 0 <= choice < len(books):
                return books[choice]
            else:
                print("Invalid selection. Please choose a valid number.")
        except ValueError:
            print("Please enter a valid number.")

def read_book(file_path):
    # Read and return the content of the chosen book
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("\n--- Book Content Preview ---\n")
            print(content[:500] + "\n...")  # Print first 500 characters for preview
            print("\n--- End of Preview ---")
            return content
    except FileNotFoundError:
        print(f"The file '{file_path}' could not be found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return ""

def count_words(text):
    # Count and return the number of words in the text
    words = text.split()
    return len(words)

def count_characters(text):
    # Count occurrences of each character, ignoring case
    text = text.lower()  # Convert to lowercase to avoid duplicates
    char_counts = Counter(text)
    return char_counts

def main():
    directory = "books/"
    books = list_books(directory)
    if books:
        chosen_book = choose_book(books)
        content = read_book(os.path.join(directory, chosen_book))
        if content:
            word_count = count_words(content)
            print(f"\nThe book '{chosen_book}' contains {word_count} words.")
            
            char_counts = count_characters(content)
            print("\nCharacter frequency count (ignoring case):")
            for char, count in char_counts.items():
                print(f"'{char}': {count}")

if __name__ == "__main__":
    main()
