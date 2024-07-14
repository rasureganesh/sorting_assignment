def reconstructSentence(s):
    # Step 1: Split the input string by spaces
    parts = s.split()
    
    # Step 2: Initialize a dictionary to map indices to words
    word_map = {}
    
    # Step 3: Process each part to extract words and indices
    for part in parts:
        word = part[:-1]  # Remove the last character (which is the index)
        index = int(part[-1])  # Get the last character as integer (1-indexed)
        word_map[index] = word
    
    # Step 4: Reconstruct the original sentence based on sorted indices
    original_sentence = []
    for i in range(1, len(parts) + 1):
        original_sentence.append(word_map[i])
    
    # Step 5: Join the words into a single string
    return ' '.join(original_sentence)

# Example usage:
s = "is2 sentence4 This1 a3" 
print("Input:", s)
print("Output:", reconstructSentence(s))  # Output: "This is a sentence"
