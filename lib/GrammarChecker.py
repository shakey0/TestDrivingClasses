class GrammarStats:

    def __init__(self):
        self.check_records = []

    def check(self, text):
        text = text.strip()
        if text[0].isupper() and text[-1] in ["!", "?", "."]:
            self.check_records.append(1)
            return True
        else:
            self.check_records.append(0)
            return False
    
    def percentage_good(self):
        return round((sum(self.check_records) / len(self.check_records)) * 100)
    