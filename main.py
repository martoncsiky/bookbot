from stats import get_num_words
from stats import count_characters
from stats import report
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    
    report(sys.argv[1])  # Use the second argument (book path)

if __name__ == "__main__":
    main()
        
