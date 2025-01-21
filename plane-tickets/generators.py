"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    index = 0
    letters = ["A","B","C","D"]
    for x in range(number):
        if index > 3:
            index = 0
        yield letters[index]
        index += 1


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    amount_of_seats = 0
    row = 1
    seat_letters = generate_seat_letters(number)
    while amount_of_seats <= number:
        if row == 13:
            row += 1
            continue
        for _ in range(4):
            if amount_of_seats >= number:
                return
            yield f"{row}{next(seat_letters)}"
            amount_of_seats += 1
        row += 1
        

        

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    passengers_dict = {}
    seats = generate_seats(len(passengers))
    for passenger in passengers:
        passengers_dict[passenger] = next(seats)
    return passengers_dict


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        ticket_used_len = len(seat) + len(flight_id)
        yield seat + flight_id + "0" * (12 - ticket_used_len)
