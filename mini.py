class Library:
    def _init_(self,Listofbooks,nameodlib):
        self.listofbooks = Listofbooks
        self.nameoflibrary = nameodlib
        self.lendbooks = dict()

    def displaybook(self):
        print("We have a collection of Books:")
        count = 1
        for book in self.listofbooks:
            print("{}: {}".format(count,book))
            count += 1

    def lendbook(self,username,bookname):
        if bookname not in self.listofbooks:
            print("Book is not present in our collection")
        elif bookname not in self.lendbooks.keys():
            self.lendbooks.update({bookname:username})
            print("Now you can take this book..!!")
        else:
            print(f"Book is already lend by {self.lendbooks[bookname]}")
            
    def addbook(self,bookname):
        self.listofbooks.append(bookname)
        print("Book has been added to the list..!!")

    def returnbook(self,booksname):
        self.lendbooks.pop(booksname)
        print("Book has been return..!!")


print("Welcome to Affan's Library")
affan = Library(["python","C++","java","html"],"Engr.Affan Library")
while True:
    print("\nWhat would you like to do??..Choose any one operation")
    print(f"1: Display Book \n2: Lend Book \n3: Add book \n4: Return Book \n5: Exit\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        affan.displaybook()

    elif choice == 2:
        user_name = input("Enter name of user:")
        book_name = input("Enter name of book:").lower()
        affan.lendbook(user_name,book_name)

    elif choice == 3:
        Book_name = input("Enter name of book:")
        affan.addbook(Book_name)

    elif choice == 4:
        name_book = input("Enter name of book:")
        affan.returnbook(name_book)
    elif choice == 5:
        print("You are exit..!!")
        exit()