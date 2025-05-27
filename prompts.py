ANKI_FROM_COMMENTS_CLAUDE = """
Here is a list of comments I made when I read the text:

{comments}

Use your tools to create multiple Anki flashcards based on this text. Focus specifically on the comments made during the reading of the text. Both the questions and answers should be able to stand alone, but ensure they're based on the full content of the PDF and the text associated with each comment. Keep the answers concise and memorable.

Use numbered lists if the answer includes multiple items.

If a label start with "front:" use it as the front.

Make each card stand alone.

Make sure you get the essence of the comment/highlight. To do this it is important to understand the full text, especially the parts surrounding the highlighted text. Make sure that the answers are correct.

Eventually, save it to the Anki deck named: "{anki_deck_name}", but before you create the flashcards, print them out so I can review them. Only when I say "go" should you use your tools to create the flashcards and save them to the Anki deck.
"""

ANKI_FROM_COMMENTS_OTHER = """
Here is a list of comments I made when I read the text:

{comments}

Create a list of Anki-style flashcards. Focus specifically on the comments and highlights made during the reading of the text. Both the questions and answers should be able to stand alone, but ensure they're based on the full content of the PDF and the text associated with each comment. Keep the answers concise and memorable.

Use numbered lists if the answer includes multiple items.

If a label start with "front:" use it as the front.

Make each card stand alone.

Make sure you get the essence of the comment/highlight. To do this it is important to understand the full text, especially the parts surrounding the highlighted text. Make sure that the answers are correct.
"""
