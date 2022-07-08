# Searches the text input for a match of the pattern input
def pattern_search(text, pattern):
    print("Input Text:", text, "Input Pattern:", pattern)

    for index in range(len(text)):
        print("Text Index:", index)
        match_count = 0

        for char in range(len(pattern)):
            print("Pattern Index:", char)

            if pattern[char] == text[index + char]:
                match_count += 1
            else:
                break

        if match_count == len(pattern):
            print(pattern, "found at index", index)

# Searches text for a matching pattern input with an option for case sensitivity
def pattern_search(text, pattern, case_sensitive=True):
    for index in range(len(text)):
        match_count = 0

        for char in range(len(pattern)): 
            if case_sensitive and pattern[char] == text[index + char]:
                match_count += 1
            elif not case_sensitive and pattern[char].lower() == text[index + char].lower():
                    match_count += 1
            else:
                break

        if match_count == len(pattern):
            print(pattern, "found at index", index)

# Takes adds the ability to swap the matched pattern with the replacement pattern
def pattern_search(text, pattern, replacement, case_sensitive=True):
    fixed_text = ''
    num_skips = 0

    for index in range(len(text)):

        match_count = 0

        if num_skips > 0:
            num_skips -= 1
            continue

        for char in range(len(pattern)): 
            if case_sensitive and pattern[char] == text[index + char]:
                match_count += 1
            elif not case_sensitive and pattern[char].lower() == text[index + char].lower():
                    match_count += 1
            else:
                break

        if match_count == len(pattern):
            print(pattern, "found at index", index)
            fixed_text += replacement
            num_skips = len(pattern) - 1
        else:
            fixed_text += text[index]
    
    return fixed_text
