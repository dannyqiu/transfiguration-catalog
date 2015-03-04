import logging
from catalog import *

class TestPage(BaseHandler):

    def get(self):
        books = bookLists.get_books_values()
        books = [[books[r][c] for c in [0,1,2,3,4,6]] for r in range(0,len(books))]
        big_books = bookLists.get_big_books_values()
        big_books = [[big_books[r][c] for c in [0,1,2,3,4,6]] for r in range(0,len(big_books))]
        audio_books = bookLists.get_audio_books_values()
        audio_books = [[audio_books[r][c] for c in [0,1,2,3,4,6]] for r in range(0,len(audio_books))]

        template_values = {
            'books': books,
            'big_books': big_books,
            'audio_books': audio_books
        }
        self.render_template('test.html', template_values)

        books = bookLists.get_books()
        logging.info(books.updated)
