class Bus:
    def __init__(self,bus_no,bus_name,from_,to,dep_time,arr_time,price,total_seats):
        self.bus_no=bus_no
        self.bus_name=bus_name
        self.from_=from_
        self.to=to
        self.dep_time=dep_time
        self.arr_time=arr_time
        self.price=price
        self.total_seats=total_seats
        self.booked_seats=[]
details = []
bookings = []
def add_bus():
    bus_no=input("Enter bus number : ")
    bus_name=input("Enter bus name : ")
    from_=input("Enter where the bus is coming from : ")
    to=input("Enter where the bus going to : ")
    dep_time=input("Enter departure time : ")
    arr_time=input("Enter arrival time : ")
    price=int(input("Enter ticket price :"))
    total_seats=int(input("Enter total number of seats in the bus : "))
    details.append(Bus(bus_no,bus_name,from_,to,dep_time,arr_time,price,total_seats))
    print("Bus added Successfully")
def view_buses():
    if len(details)==0:
        print("no buses available")
        return
    print("===available===")
    for d in details:
        available=d.total_seats-len(d.booked_seats)
        print(f"Bus No:{d.bus_no}\nBus Name:{d.bus_name}\nFrom:{d.from_}\nTo:{d.to}\nDeparture:{d.dep_time}\nArrival:{d.arr_time}\nPrice:₹{d.price}\nAvailable:{available}")
def search_buses():
    from_=input("from : ")
    to=input("to : ")
    for d in details:
        if d.from_==from_ and d.to==to:
            available = d.total_seats - len(d.booked_seats)
            print(f" Bus NO : {d.bus_no}\n Bus Name : {d.bus_name}\n Departure : {d.dep_time}\n Arrival : {d.arr_time}\nPrice : {d.price}\n Available sears:{d.total_seats}")                                         
            return
    print("Bus not found!!")
def view_seats():
    bus_no = input("Enter bus number : ")
    for d in details:
        if d.bus_no == bus_no:
            print("\n========== AVAILABLE SEATS ==========")
            for seat in range(1, d.total_seats + 1):
                if seat not in d.booked_seats:
                    print(seat, end=" ")
            print()
            return
    print("Bus not found!!")
def book_tickets():
    booking_count=1001
    name=input("Enter passenger name : ")
    age=int(input("Enter Age : "))
    phn_no=input("Enter phone number : ")
    bus_no=input("Enter bus number : ")
    seat_no=int(input("Enter seat number : "))
    for d in details:
        if d.bus_no==bus_no:
            if seat_no < 1 or seat_no > d.total_seats:
                print("Invalid seat number")
                return
            if seat_no in d.booked_seats:
                print("Seat already booked!!")
                return
            d.booked_seats.append(seat_no)
            booking_id = "B" + str(booking_count)
            booking_count += 1
            booking = {
                "booking_id": booking_id,
                "name": name,
                "age": age,
                "phone": phn_no,
                "bus_no": bus_no,
                "seat_no": seat_no,
                "from": d.from_,
                "to": d.to,
                "price": d.price,
                "status": "Confirmed"
            }
            bookings.append(booking)
            print("\n========== BUS TICKET ==========")
            print("Booking ID :", booking_id)
            print("Passenger  :", name)
            print("Age        :", age)
            print("Phone      :", phn_no)
            print("Bus No     :", d.bus_no)
            print("From       :", d.from_)
            print("To         :", d.to)
            print("Seat No    :", seat_no)
            print("Amount     : ₹", d.price)
            print("Status     : Confirmed")
            print("================================")
            print("Ticket booked successfully")
            return
    print("Bus not found!!")
def cancel_ticket():
    booking_id=input("Enter booking id : ")
    for b in bookings:
        if b["booking_id"] == booking_id:
            if b["status"] == "Cancelled":
                print("Ticket is already cancelled")
                return
            b["status"] = "Cancelled"
            for d in details:
                if d.bus_no == b["bus_no"]:
                    d.booked_seats.remove(b["seat_no"])
                    break
            print("Ticket cancelled successfully.")
            print("Seat", b["seat_no"], "is now available.")
            return
    print("Booking ID not found!!")
def view_booking():
     if len(bookings) == 0:
        print("No bookings available")
        return
     print("\n=======bookings========")
     for b in bookings:
        print("Booking ID :", b["booking_id"])
        print("Passenger  :", b["name"])
        print("Bus No     :", b["bus_no"])
        print("Seat       :", b["seat_no"])
        print("Status     :", b["status"])
        print("------------------------------")
while True:
    print("================================")
    print("    BUS RESERVATION SYSTEM      ")
    print("================================")
    print("1.Add Bus")
    print("2.View Buses")
    print("3.Search Bus")
    print("4.View Available Seats")
    print("5.Book Ticket")
    print("6.Cancel Ticket")
    print("7.View Bookings")
    print("8.Exit")
    choice=input("Enter your Choice : ")
    if choice == "1":
        add_bus()
    elif choice == "2":
        view_buses()
    elif choice == "3":
        search_buses()
    elif choice == "4":
        view_seats()
    elif choice == "5":
        book_tickets()
    elif choice == "6":
        cancel_ticket()
    elif choice == "7":
        view_booking()
    elif choice == "8":
        print("thank you")
        break
    else:
        print("Invalid choice")
