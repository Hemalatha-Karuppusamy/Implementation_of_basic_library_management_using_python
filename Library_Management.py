class library:
  def __init__(self,books):
    self.books = books

  def show(self):
    print(*self.books, sep = "|",)

  def bookavailability(self,book):
    if book in self.books:
         print("Book is Available")
    else:
         print("Book is Not available")
     
  def availbook(self, book):
    if book in self.books:
      self.books.remove(book)
      print("Book successfully issued")
      return True
    else:
      print("Book is not available")
      return False

  def donate(self):
    book = input("enter the book name you donate ")
    self.books.append(book)
    print("Thanks for your donation!...")

class student:
  def __init__(self):
    self.lst=[]

  def availedbooks(self,Book_name):
    self.lst.append(Book_name)

  def request_book(self):
    print('Enter the book ')
    self.book = input()
    return self.book

  def retbook(self):
    ret = input("Return book name: ")
    if ret in self.lst:
      self.lst.remove(ret)
      print("Book Successfully returned")
      print("your database holds ",len(self.lst), "books")
    else:
      print("It seems your are trying to donate a book kindly select 4 for Book Donation")

mylib = library(["Book1","Book2","Book3","Book4","Book1","Book6","Book5","Book2"])
hema = student()

while True:
  print("Welcome to the world of reading")
  print('''select your request code
  1 to view books available in the library
  2 to Lend a book
  3 to Return a book
  4 to Donate a book
  6 to Check availability of a book
  5 Exit''')
  print("________________________________")
  Input = int(input("Enter you operation code: "))

  if Input == 1:
    mylib.show()
  elif Input == 2:
    book = hema.request_book()
    Result = mylib.availbook(book)
    if Result == True:
      hema.availedbooks(book)
  elif Input == 3:
    hema.retbook()
  elif Input == 4:
    mylib.donate()
  elif Input == 5:
    break
  elif Input == 6:
    book = input("Enter the Book Name:")
    mylib.bookavailability(book)
  else:
    print("Enter a valid characters")
