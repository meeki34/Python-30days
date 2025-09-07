#Magic method = Dunder method( double underscore method)
# They are automatically called by python interpreter
#  
# 

class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages   

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self,other):
        return self.pages < other.pages 
    
    def __getstate__(self) -> object:
        return self.title, self.author, self.pages
    
    def __add__ (self,other):
        return Book(self.title, self.author, self.pages + other.pages)
                    
    def __contains__(self, item):
        return item in self.title or item in self.author    

    def __getitem__(self, index):
        if index == 0:
            return self.title
        elif index == 1:
            return self.author
        elif index == 2:
            return self.pages
        else:
            return "Invalid index"
book1 = Book("Python", "Jose", 200)
book2 = Book("C++", "Jose", 200)

def main():
    print(book1)
    print(book2)
    print(book1 == book2)
    print(book2 < book1)
    print(len(book1))
    print(book1 + book2)
    print("Python" in book1)
    print("Java" in book1)
    print(book1.__getstate__())
    
    print(book1['author'])
if __name__ == "__main__":
    main()

