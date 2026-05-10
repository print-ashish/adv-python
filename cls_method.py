class Pizza:
    def __init__(self,ingredients):
        self.ingredients = ingredients

    def __repr__(self):
       return f"Pizza with {self.ingredients}" 

    @classmethod
    def margherita(cls):
        return cls(["cheese", "tomato"])

    @classmethod 
    def veggie(cls):
        return cls(["mushrooms", "onions" , "peppers"])


# custom_pizza = Pizza(["pineapple", "corn"])
# print(custom_pizza)


# pizza1 = Pizza.margherita()
# pizza2 = Pizza.veggie()

# print(pizza1)
# print(pizza2)


class Book: 
    def __init__(self,title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return (f"Title {self.title}  author {self.author}")
    
    @classmethod
    def kindle_edition(cls,title, author):
        return cls(title + "Digital" , author)
    
    @classmethod 
    def hardcover_edition(cls , title , author):
        return cls(title + "Hardcover" , author)


# book1 = Book.kindle_edition("Atomic habits" ,"James Clear")
# print(book1.title)

book1 = Book.hardcover_edition("Atomic habits" ,"James Clear")
print(book1)