class Star_Cinema:

    __hall_list = []
    def entry_hall(self, hall):
        Star_Cinema.__hall_list.append(hall)

class Hall(Star_Cinema):

    def __init__(self, rows, cols, hall_no) -> None:

        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []
        self.entry_hall(self)

    def entry_show(self, movie_id, movie_name, time):

        movies = (movie_id, movie_name, time)
        self.show_list.append(movies)
        seats_matrix = [[0 for i in range(self.rows)] for j in range(self.cols)]
        self.seats[movie_id] = seats_matrix

    def book_seats(self, show_id, list):

        grid = self.seats[show_id]
        for i in list:
            row = i[0]
            col = i[1]
            if grid[row][col] == 0:
                grid[row][col] = 1
                print("--------------")
                print(f"Seat ({row,col}) booked for show {show_id}")
                print("--------------")
            elif grid[row][col] == 1:
                print("--------------")
                print("This seat is already booked ! ")
                print("--------------")      

    def view_show_list(self):
        print(self.show_list)

    def view_available_seats(self, movie_id):
        
        print("--------------")
        print(f"Available seat for show {movie_id}")
        print("--------------")
        grid = self.seats[movie_id]
        for i in grid:
            print(i)
        print(" ")

object = Hall(6,6,10)
object.entry_show(101, "Avatar", "20/06/2024 10:00")
object.entry_show(102, "How to train your dragon", "23/06/2024 13:00")

run = True

while run:
    print("1. View All Show Today")
    print("2. View Available Seats")
    print("3. Book Ticket")
    print("4. Exit")

    option = int(input("Enter Option: "))

    if option == 1:
        moivie_list = object.show_list
        if len(moivie_list) != 0:
            print("--------------")
            for value in moivie_list:
                print(f"Movie Name: {value[1]}({value[0]}) Show Id: {value[0]} Time: {value[2]}")
            print("--------------")
        else:
            print("--------------")
            print("No Movie are running today.")
            print("--------------")
    
    elif option == 2:
        movie_id = int(input("Enter movie id: "))
        all_show = object.show_list
        flag = False
        for values in all_show:
            if values[0] == movie_id:
                flag = True
                object.view_available_seats(movie_id)
        if flag == False:
            print("-------------")
            print("Invalid movie id ! ")
            print("-------------")

    elif option == 3:

        booking_id = int(input("Show id: "))

        all_show = object.show_list
        flag = False
        for values in all_show:
            if values[0] == booking_id:
                seat_count = int(input("Number of ticket?: "))
                flag = True
                ticket_list = []
                for i in range(seat_count):
                    row = int(input("Enter seat row: "))
                    col = int(input("Enter seat col: "))
                    if row < object.rows and col < object.cols:
                        touple = (row,col)
                        ticket_list.append(touple)
                    else:
                        print(f"Invalid Seat. Please Enter between Rows: {object.rows} And Cols: {object.cols} ")
                        
                object.book_seats(booking_id, ticket_list)
        if flag == False:
            print("-------------")   
            print("Invalid show id ! ")   
            print("-------------")

    elif option == 4:
        run = False
