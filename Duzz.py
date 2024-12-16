def translate_to_uzz(word):
    if len(word) <= 3:
        return word[:1] + "uzz"  # For short words, just keep the first letter and add "uzz"
    else:
        return word[:len(word) // 2] + "uzz"  # Keep the first half and replace the rest with "uzz"

# Loop to allow multiple translations
while True:
    word = input("Enter a word (or type 'quit' to exit): ")
    
    if word.lower() == 'quit':  # Check if the user wants to quit
        print("Goodbye!")
        break  # Exit the loop
    
    translated_word = translate_to_uzz(word)
    print(f"The translated word is: {translated_word}")

