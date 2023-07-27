import math

class DiaryEntry:

    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.list_words = contents.split()
    
    def format(self):
        return f"{self.title}: {self.contents}"
    
    def count_words(self):
        return len(self.contents.split())
    
    def reading_times(self, wpm):
        return round(self.count_words() / wpm)
    
    def reading_chunk(self, wpm, minutes):
        if len(self.list_words) == 0:
            self.list_words = self.contents.split()
        chunk = []
        for _ in range(wpm * minutes):
            if len(self.list_words) > 0:
                chunk.append(self.list_words[0])
                self.list_words.pop(0)
            else:
                break
        return " ".join(chunk)