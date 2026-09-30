# class Pet:
#     def __init__(self, name: str, species:str) -> None:
#         self.name = name
#         self.species = species



# # Do not modify below this line
# my_pet = Pet("Fluffy", "cat")
# print(f"My pet is a {my_pet.species} named {my_pet.name}")


class Movie:
    def __init__(self, movieName: str, totalSeats: int, ticketPrice: float) -> None :
        self.movieName = movieName
        self.totalSeats = totalSeats
        self.ticketPrice = ticketPrice
        self.bookedSeats = 0

    def bookTickets(self, numTickets:int) -> None :
        if numTickets > self.totalSeats - self.bookedSeats:
            print("Not enough Seats available")
        else:
            self.bookedSeats += numTickets
            self.totalSeats -= numTickets
            print(f"your tickets are booked")
            print(f"Total Cost {self.ticketPrice * numTickets}")


    
    def showStatus(self) -> None: 
        seatsAvailable = self.totalSeats - self.bookedSeats
        print(f"{self.movieName}, has {seatsAvailable} available and seats booked so far {self.bookedSeats}")


movie = Movie("Deadpool", 150, 300)
movie.bookTickets(3)
movie.showStatus()


 

    
