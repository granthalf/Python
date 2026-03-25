#Use this website in order to test the strength of your hash:
#https://www.dcode.fr/hash-function
#
#be careful /!\ gromweb is displaying hashes on the bottom of the page => better to avoid this site
#mechanism of unhash md5: by dictionary.
#
import sys
import hashlib

def compute_md5(text: str) -> str:
    """Return the MD5 hash of the given text."""
    md5 = hashlib.md5()
    md5.update(text.encode("utf-8"))
    return md5.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python md5_hash.py <text>")
        sys.exit(1)

    input_text = sys.argv[1]
    result = compute_md5(input_text)
    print(f"MD5: {result}")
