class Document():
    welcome_str = 'Welcome! The context for this book is {}.'

    def __init__(self, title, author, context):
        print('init function called')
        self.title = title
        self.author = author
        self.__context = context


    @classmethod
    def create_empty_book(cls, title, author):
        return cls(title=title, author=author, context='nothing')

    def get_context_length(self):
        return len(self.__context)

    @staticmethod
    def get_welcome(context):
        return Document.welcome_str.format(context)


empety_book=Document.create_empty_book('li','ls')
print(empety_book.get_welcome('indeed nothing'))
print(empety_book.get_context_length())
print(empety_book.get_welcome('indeed nothing'))