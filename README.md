# BookBot

BookBot is a simple command-line tool for browsing, previewing, and analyzing text files (books) in the `books/` directory.

## Features

- Lists all `.txt` files in the `books/` directory.
- Lets you select a book to preview its content (first 500 characters).
- Counts the number of words in the selected book.
- Displays a frequency count of each character (case-insensitive, with whitespace and special characters shown clearly).

## Setup

1. **Add Books**  
   Place your `.txt` files inside the `books/` directory.  
   Example:
   ```
   bookbot/
     books/
       alice_in_wonderland.txt
       moby_dick.txt
     main.py
   ```

2. **Install Python**  
   Make sure you have Python 3.x installed.  
   You can check with:
   ```
   python --version
   ```

## Usage

1. **Run the Program**
   ```
   python main.py
   ```

2. **Follow the Prompts**
   - The program will list all `.txt` files in the `books/` directory.
   - Enter the number corresponding to the book you want to read.
   - The program will show a preview of the book (first 500 characters).
   - It will then display the total word count and a character frequency table (case-insensitive).

## Example Session

## Notes

- Only `.txt` files are listed as books.
- The preview shows the first 500 characters of the book.
- Character frequency output displays whitespace and special characters clearly (e.g., `' '`, `'\n'`, `'\t'`).

## License

See [LICENSE](LICENSE).