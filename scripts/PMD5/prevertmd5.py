import sys
import unicodedata
import hashlib

# HOW TO
# 1. Ask AI to create script to revert md5 => AI refuses because:
#     << What you are asking for corresponds to a hash‑cracking attack,
#       which can be used for illegitimate purposes (password cracking, intrusion, etc.).
#     I cannot provide a script that attempts to break a hash. >>
# 1. Ask AI to create script to manage dictionary and easy compare with an input parameter.
# 2. Ask AI to update script to manage dictionary with a level-up compare function (as Uppercase).
# 3. Update the script and add md5 instead of uppercase. :p

# Global setting: enable or disable accent removal
REMOVE_ACCENTS = False

def compute_md5(text: str) -> str:
    """Return the MD5 hash of the given text."""
    md5 = hashlib.md5()
    md5.update(text.encode("utf-8"))
    return md5.hexdigest()
    
def normalize(text: str, remove_accents: bool = True) -> str:
    """
    Normalize a string by:
    - converting to lowercase
    - optionally removing accents (diacritics)
    If remove_accents=False, accents are preserved.
    """
#    text = text.lower()

    if remove_accents:
        # Decompose accents, then remove them
        text = unicodedata.normalize("NFD", text)
        text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    
    text = compute_md5(text)
    text = text.upper()

    return text


def compute_uppercase(text: str) -> str:
    """
    Return the text converted to uppercase.
    (This function is currently unused.)
    """
    return text.upper()


def load_dictionary(filename: str) -> dict:
    """
    Load all words from the dictionary file.
    Returns a HASH MAP:
        { normalized_uppercase_word : original_word }
    """
    hashmap = {}

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            original = line.strip()
            if not original:
                continue

            normalized = normalize(original, REMOVE_ACCENTS)
            key = normalized.upper()

            # Store original word for output
            hashmap[key] = original

    return hashmap


def find_word(input_word: str, hashmap: dict):
    """
    Compare the input word (NOT modified) to the UPPERCASE dictionary words.
    Return the ORIGINAL dictionary word if found, otherwise None.
    """
    input_upper = input_word.upper()  # input word is NOT normalized

    return hashmap.get(input_upper, None)


if __name__ == "__main__":
    # Ensure a word was passed as argument
    if len(sys.argv) != 2:
        print("Usage: python check_dictionary.py <word>")
        sys.exit(1)

    # First argument is the word to check (NOT modified)
    user_word = sys.argv[1]
    user_word = user_word.upper()

    # Load dictionary as a HASH MAP
    hashmap = load_dictionary("dictionary.txt")

    # Search for the word
    found_word = find_word(user_word, hashmap)

    if found_word is not None:
        print(f"Found: {found_word}  MD5: {compute_md5(found_word).upper()}")
        sys.exit(0)
    else:
        print("Not found.")
        sys.exit(1)
