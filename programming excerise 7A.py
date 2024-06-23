import re


def extract_sentences(text):
    # Define the regular expression pattern
    pattern = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'
    # Explanation of the pattern:
    # [A-Z0-9] matches an uppercase letter or a digit at the beginning of the sentence.
    # .*? matches any characters (non-greedy).
    # [.!?] matches one of the sentence-ending punctuation marks.
    # (?= [A-Z0-9]|$) lookahead assertion matches either a space followed by an uppercase letter or a digit,
    # or the end of the string ($).

    # Find all matches using re.findall with DOTALL and MULTILINE flags
    sentences = re.findall(pattern, text, flags=re.DOTALL | re.MULTILINE)

    # Return the list of sentences
    return sentences


def main():
    # Example text with sentences
    s = """
    1. This is a sentence. 
    2. This is another sentence! Isn't it great? 
    3. A sentence with numbers 123 and punctuation! And more text.
    """

    # Extract sentences
    extracted_sentences = extract_sentences(s)

    # Display extracted sentences
    print("Extracted Sentences:")
    for i, sentence in enumerate(extracted_sentences, 1):
        print(f"{i}. {sentence}")

    # Display count of sentences
    sentence_count = len(extracted_sentences)
    print(f"\nTotal number of sentences: {sentence_count}")

if __name__ == "__main__":
    main()
