def translate_to_uzz(word):
    if len(word) <= 3:
        return word[:1] + "uzz"  # For short words, just keep the first letter and add "uzz"
    else:
        return word[:2] + "uzz"  # Keep the first 2 letters and replace the rest with "uzz"

# Loop to allow multiple translations
while True:
    word = input("Enuzz auzz wuzz (ouzz tyuzz 'quzz' tuzz euzz): ")
    
    if word.lower() == 'quzz':  # Check if the user wants to quit
        print("Guzz!")
        break  # Exit the loop
    
    translated_word = translate_to_uzz(word)
    print(f"Thuzz truzz wouzz iuzz: {translated_word}")

