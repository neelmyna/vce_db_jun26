import book_crud_operations as bco

def menu(choice):
    match choice:
        case 1 : bco.add_book()
        case 2 : bco.delete_book()
        case 3 : bco.update_book()
        case 4 : bco.search_book()
        case 5 : bco.list_books()
        case _ : print('Invalid choice entered')

def run_book_app():
    while True:
        print('1:Add 2:Delete 3:Update 4:Search 5: List 6:Exit')
        choice = int(input('Enter your choice: '))
        if choice == 6:
            break # break the loop
        menu(choice)
    print('Book App closed')

run_book_app()
