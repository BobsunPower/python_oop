class Music:
    def __init__(self, title, artist, lyrics):
        self.title, self.artist, self.lyrics = title, artist, lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return f"{self.lyrics}"
