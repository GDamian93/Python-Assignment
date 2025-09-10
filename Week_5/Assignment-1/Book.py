# Create a class Book

class Book:
    """
        Class represents a book in the library.

        Attributes:
            id_book (str): unique identifier of book.
            title (str): Title of the book.
            author (str): Author of the book.
            publish_year (int): Year of publication.
            genre (str): Genre of the book.
            available (bool): Availability of the book.
    """
    # Initialize an object Book with main attributes.
    def __init__(self, id_book: str = "", title: str = "", author: str = "", publish_year: int = 0, genre: str = "", available: bool = True):
        self.__id_book = id_book
        self.__title = title
        self.__author = author
        self.__publish_year = publish_year
        self.__genre = genre
        self.__available = available
   
    # Getters
    @property
    def id(self):
        return self.__id_book
    
    @property
    def title(self):
        return self.__title
    
    @property
    def author(self):
        return self.__author
    
    @property
    def publish_year(self):
        return self.__publish_year
    
    @property   
    def genre(self):
        return self.__genre
    
    @property
    def availability_status(self):
        return self.__available
    
    # Setters
    @title.setter
    def title(self, new_title: str):
        if not new_title:
            raise ValueError("Title is required!")
        self.__title = new_title
    
    @author.setter  
    def author(self, new_author: str):
        if not new_author:
            raise ValueError("Author is required!")
        self.__author = new_author

    @publish_year.setter
    def publish_year(self, new_publish_year: int):
        if new_publish_year < 0:
            raise ValueError("Publish year must be positive.")
        self.__publish_year = new_publish_year
    
    @genre.setter
    def genre(self, new_genre: str):
        if not new_genre:
            raise ValueError("Genre is required!")
        self.__genre = new_genre

    # Method to borrow book
    def borrow_book(self):
        if self.__available:
            self.__available = False
            print("Book borrowed successfully.")
            return True
        else:
            print("Book is not available for borrowing.")
            return False

    # Method to return book
    def return_book(self):
        self.__available = True
        print("Book returned successfully.")
        return True

    # Method to display book information
    def display_info(self):
        info = "\n_______________________________\n" + f"ID: {self.__id_book}\nTitle: {self.__title}\nAuthor: {self.__author}\nYear: {self.__publish_year}\nGenre: {self.__genre}\nAvailable: {self.availability_status}"
        return info
