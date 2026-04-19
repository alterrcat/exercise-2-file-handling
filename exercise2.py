# Exercise 2 - File Handling

try:
    
    note1 = input("Enter a short note: ")

    
    with open("notes.txt", "w") as file:
        file.write(note1 + "\n")

    
    print("\n--- File Content ---")
    with open("notes.txt", "r") as file:
        print(file.read())

    
    note2 = input("\nEnter another note: ")

    
    with open("notes.txt", "a") as file:
        file.write(note2 + "\n")

    
    print("\n--- Updated File Content ---")
    with open("notes.txt", "r") as file:
        print(file.read())


except FileNotFoundError:
    print("Error: File not found.")
except IOError:
    print("Error: Cannot read/write file.")
except Exception as e:
    print("Unexpected error:", e)
