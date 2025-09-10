from Book import Book
class AudioBook(Book):
    """
        Class representing an audiobook, inheriting from Book.
    
        Attributes:
            narrator (str): Name of the narrator.
            duration (int): Duration of the audiobook in minutes.
            audio_format (str): Format of the audio file (e.g., MP3, WAV).
    """
    def __init__(self, book_id, title, author, publish_year, genre, narrator, duration, audio_format="MP3"):
        super().__init__(book_id, title, author, publish_year, genre)
        self.__narrator = narrator
        self.__duration = duration  # Duration in minutes
        self.__audio_format = audio_format
   
    # Getters
    @property
    def narrator(self):
        return self.__narrator

    @property
    def duration(self):
        return self.__duration

    @property
    def audio_format(self):
        return self.__audio_format
    
    # Setters
    @narrator.setter
    def narrator(self, new_narrator: str):
        if not new_narrator:
            raise ValueError("Narrator is required!")
        self.__narrator = new_narrator

    @duration.setter
    def duration(self, new_duration: int):  
        if new_duration <= 0:
            raise ValueError("Duration must be positive.")
        self.__duration = new_duration
    
    @audio_format.setter
    def audio_format(self, new_format: str):
        if not new_format:
            raise ValueError("Audio format is required!")
        self.__audio_format = new_format

    
    # Override display_info method about audiobook specifics
    def display_info(self):
        base_info = super().display_info()
        return f"\n{base_info}, Narrator: {self.__narrator}, Duration: {self.__duration} mins, Format: {self.__audio_format}"
    
    # Method to simulate playing the audiobook
    def play(self):
        if self.availability_status:
            print(f"...\nPlaying audiobook '{self.title}' narrated by {self.narrator}.\n...")
            return True