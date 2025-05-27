from utils import extract_pdf_comments
from prompts import ANKI_FROM_COMMENTS_CLAUDE, ANKI_FROM_COMMENTS_OTHER
import pyperclip
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <PDF path> <anki deck name>")
        sys.exit(1)
    
    pdf_file = sys.argv[1]
    anki_deck_name = sys.argv[2]

    comments = extract_pdf_comments(pdf_file)

    comments_text = "* " + "\n* ".join(comments)

    prompt = ANKI_FROM_COMMENTS_CLAUDE.format(comments=comments_text, anki_deck_name=anki_deck_name)
    #prompt = ANKI_FROM_COMMENTS_OTHER.format(comments=comments_text)
    pyperclip.copy(prompt)
    print("Prompt copied to clipboard. Don't forget to also give Claude the PDF.")

