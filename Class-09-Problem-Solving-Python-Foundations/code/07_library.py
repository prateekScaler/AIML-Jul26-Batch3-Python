# Q6. Mini library management system (Classes 1 to 8)
library = {
    "B101": {"title": "Python Basics", "author": "R. Rao", "copies": 3, "tags": {"python", "beginner"}},
    "B102": {"title": "Data Science 101", "author": "S. Iyer", "copies": 1, "tags": {"data", "python"}}
}

def add_book():
    book_id = input("Id: ").strip().upper()
    if book_id in library:
        print("That id already exists.")
        return
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    copies = int(input("Copies: "))
    tags = set(input("Tags (comma separated): ").lower().replace(" ", "").split(","))
    library[book_id] = {"title": title, "author": author, "copies": copies, "tags": tags}
    print(f"Added {title}.")

def issue_book():
    book_id = input("Id: ").strip().upper()
    if book_id not in library:
        print("No such book.")
        return
    book = library[book_id]
    if book["copies"] == 0:
        print("Not available")
        return
    book["copies"] -= 1
    print(f"Issued {book['title']}. {book['copies']} left.")

def return_book():
    book_id = input("Id: ").strip().upper()
    if book_id not in library:
        print("No such book.")
        return
    library[book_id]["copies"] += 1
    print(f"Returned {library[book_id]['title']}.")

def search_by_tag():
    tag = input("Tag: ").strip().lower()
    found = False
    for book in library.values():
        if tag in book["tags"]:
            print(book["title"])
            found = True
    if not found:
        print("No book has that tag.")

def show_all():
    for book_id, book in library.items():
        print(f"{book_id}  {book['title']} by {book['author']}  copies: {book['copies']}  tags: {sorted(book['tags'])}")

while True:
    print()
    print("1 Add  2 Issue  3 Return  4 Search tag  5 Show all  6 Exit")
    choice = input("Choose: ").strip()
    if choice == "1":
        add_book()
    elif choice == "2":
        issue_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        search_by_tag()
    elif choice == "5":
        show_all()
    elif choice == "6":
        break
    else:
        print("Unknown choice.")
        continue

print("Bye.")
