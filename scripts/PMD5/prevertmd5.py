import os
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
#
# (OR) Search on the Web:
#Another source, Another way for the same goal.
#https://www.youtube.com/watch?v=9J7X0l6r2Gs

# Global setting: enable or disable accent removal
REMOVE_ACCENTS = False

def detect_encoding(filename):
    """
    Detect encoding by trying UTF-8, ISO-8859-1, CP1252.
    Returns the first encoding that works.
    """
    # Try UTF-8
    try:
        with open(filename, "r", encoding="utf-8") as f:
            f.read()
        return "utf-8"
    except:
        pass

    # Try ISO-8859-1
    try:
        with open(filename, "r", encoding="iso-8859-1") as f:
            f.read()
        return "iso-8859-1"
    except:
        pass

    # Try CP1252 (Windows)
    try:
        with open(filename, "r", encoding="cp1252") as f:
            f.read()
        return "cp1252"
    except:
        pass

    # Fallback
    return "utf-8"

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
    Load dictionary with automatic encoding detection.
    Log file name = <filename>.log
    """
    hashmap = {}

    # Detect encoding
    encoding = detect_encoding(filename)
    print(f"Detected encoding for {filename}: {encoding}")

    # Build log filename
    base, _ = os.path.splitext(filename)
    log_filename = base + ".log"

    log = open(log_filename, "w", encoding="utf-8")

    with open(filename, "r", encoding=encoding, errors="replace") as file:
        for line_number, line in enumerate(file, start=1):

            # Log line number
            log.write(f"Processing line {line_number}\n")

            original = line.strip()
            if not original:
                continue

            normalized = normalize(original, REMOVE_ACCENTS)
            key = normalized.upper()

            hashmap[key] = original

    log.close()
    return hashmap


def find_word(input_word: str, hashmap: dict):
    """
    Compare the input word (not modified) to the UPPERCASE dictionary words.
    Return the ORIGINAL dictionary word if found, otherwise None.
    """
    input_upper = input_word.upper()  # input word is NOT normalized

    return hashmap.get(input_upper, None)


if __name__ == "__main__":
    # Expect: python check_dictionary.py <dictionary_file> <word>
    if len(sys.argv) != 3:
        print("Usage: python check_dictionary.py <dictionary_file> <word>")
        sys.exit(1)

    # First argument is the word to check (as is)
    dictionary_file = sys.argv[1]
    user_word = sys.argv[2]
    user_word = user_word.upper()

    # Load dictionary as a HASH MAP: you may use the classical hacker passwords dictionnary ;-)
    hashmap = load_dictionary(dictionary_file)

    # Search for the word
    found_word = find_word(user_word, hashmap)

    if found_word is not None:
        print(f"Found: {found_word}  MD5: {compute_md5(found_word).upper()}")
        sys.exit(0)
    else:
        print("Not found.")
        sys.exit(1)
