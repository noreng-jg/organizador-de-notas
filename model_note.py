class Note:

    def __init__(self, _title, _datetimefield, _category, _author, _message):
        self.title=_title
        self.datetimefield=_datetimefield
        self.category=_category
        self.author=_author
        self.message=_message

    def __str__(self):
        return self.title

    



