# Main program
from Book import Book
from AudioBook import AudioBook 

if __name__ == "__main__":
    
    # Create book instances
    book = Book("1", "1984", "George Orwell", 1949, "Dystopian")
    audio_book = AudioBook("2", "The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", "Andy Serkis", 720, "MP3")
    # Actualizar autor pelor setter
    book.author = "Orwell"
 
    print(book.display_info())  # Output: Book information
    print(book.borrow_book())  # Output: True
    print(audio_book.display_info())  # Output: AudioBook information
    print(audio_book.play())  # Output: True


