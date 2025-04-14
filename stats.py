def get_book_text(file_path):
    with open(file_path) as f:
         return f.read()
 

def count_chars(words):
    count = {}
    for i in words:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    return count

def print_stats(book,count,words):
    print("============ BOOKBOT ============\n"
         f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")

    for i in words:
        if i.isalpha():
            print(f"{i}: {words[i]}")
    print("============= END ===============")
        
