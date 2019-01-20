class BookStore:
    def __init__(self, bookList, coffeeShop):
        self.bookList = bookList
        self.coffeeShop = coffeeShop
    def bookSearch(self, title):
        for i in self.bookList:
            if i.title == title:
                return i
         
    def authorSearch(self, firstname, lastname):
        for book in self.bookList:
            if book.firstname == firstname and book.lastname == lastname:
                return book
         
    def coffeeSearch(self,drink,roast):
        return self.coffeeShop.coffeeSearch(drink,roast)
    def sale(self,bookSold=[],coffeeSold=[]):
        total = 0
        for i in bookSold:
            if self.bookSearch(i) != None:
                total += self.bookSearch(i).sold()
        for i in coffeeSold:
            i = i.split(" ")
            if self.coffeeSearch(i[0],i[1]) != None:
                total += self.coffeeSearch(i[0],i[1]).sold()
        return total
class Book:
    def __init__(self,title,firstName,lastName,price,quantity):
        self.title = title
        self.firstName = firstName
        self.lastName = lastName
        self.price = price
        self.quantity = quantity
    def getTitle(self):
        return self.title
    def getFirstName(self):
        return self.firstName
    def getLastName(self):
        return self.lastName
    def getPrice(self):
        return self.price
    def getQuantity(self):
        return self.quantity
    def inStock(self):
        if self.getQuantity > 0:
            return True
        else:
            return False
    def sold(self):
        self.quantity -= 1
        return self.getPrice()
    def __repr__(self):
        print(str(self.title) + " is a book that we have")
    def toString(self):
        return self.__repr__()


class CoffeeShop:
    def __init__(self,coffeeList):
        self.coffeeList= coffeeList
    def coffeeSearch(self,drink,roast):
        for i in self.coffeeList:
            if i.drink == drink and i.roast == roast:
                return i
         
    def sale(self,coffeesold):
       total =0
       for i in coffeesold:
            i = i.split()
            if self.coffeeSearch(i[0],i[1]) != None:
                total += self.coffeeSearch(i).sold()
       return total


class Coffee:
    def __init__(self,drink,roast,price,quantity):
        self.drink = drink
        self.roast = roast
        self.price = price
        self.quantity = quantity
    def getDrink(self):
        return (str(self.drink))
    def getRoast(self):
        return (str(self.roast))
    def getPrice(self):
        return (float(self.price))
    def getQuantity(self):
        return (int(self.quantity))
    def inStock(self):
        if quantity > 0:
            return True
        else:
            return False
    def sold(self):
        self.quantity -= 1
        return self.getPrice()
    def __repr__(self):
        return self.drink +", " +self.roast +", "+ str(self.price) +", "+str(self.quantity)
    def toString(self):
        return self.__repr__()
        

        
        

        