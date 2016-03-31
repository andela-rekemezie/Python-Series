"""Model for Aircraft"""
# '_' depicts implementation details


class Flight:
    """A flight with particular passenger aircraft"""

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))
        if not (number[2:].isdigit()) and int(number[2:]) <= 9999:
            raise ValueError("Invalid route number '{}'".format(number))
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def _parse_seat(self, seat):
        """
        Args:
            Seat num eg '45R', '90Y'
            """
        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1] # Take the last letter from seat
        if not letter in seat_letters:
            raise ValueError("Invalid row letter '{}'".format(letter))
        row_text = seat[:-1] # Every other item in the iterable but the last
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row '{}'".format(row_text))
        if row not in rows:
            raise ValueError("Invalid text row '{}'".format(row))
        return row, letter

    def seat_allocation(self, seat, passenger):
        row, letter = self._parse_seat(seat)
        if self._seating[row][letter] is not None:
            raise ValueError("Seat '{}' already occupied".format(seat))
        self._seating[row][letter] = passenger

    def relocate_seat(self, from_seat, to_seat):
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError('No passenger to relocate to {}'.format(from_seat))
        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is None:
            raise ValueError('Seat {} already occupied'.format(to_seat))
        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    # Getting the number of seats that are not none
    # Achieved using two nested generators
    # The outer generator filters for all rows which are not empty
    def available_seats (self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not  None)

    def make_boardin_cards(self, card_printer):
        for passenger, seat  in sorted(self._passenger_seat()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seat(self):
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, '{}{}'.format(row, letter))


class AirCraft:
    """AirCraft class"""

    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


# AirBus231 Aircraft class
class AirBus231(AirCraft):

    def model(self):
        return 'AirBus 234'

    def seating_plan(self):
        return range(1, 23), "ABCDF"


# AirBus231 Aircraft class
class Buzzq231(AirCraft):

    def model(self):
        return 'Buzza q231'

    def seating_plan(self):
        return range(1, 56), "ABCDFGHJK"



# instantianing object instances
# seed function
def make_flights():
    f = Flight('RT234', Buzzq231('ERB39-67'))
    f.seat_allocation('12A', 'Rowland')
    f.seat_allocation('11A', 'Maryam')
    f.seat_allocation('10B', 'Emmanuel')
    f.seat_allocation('22C', 'Lawrence')

    g = Flight('RT234', AirBus231('ERB39-67'))
    g.seat_allocation('12A', 'Shuaib')
    g.seat_allocation('11A', 'Dotun')
    g.seat_allocation('10B', 'Akeem')
    g.seat_allocation('22C', 'Ezeh')
    return f, g


# print function for the card
def print_card_console(passenger, seat, flight_number, aircraft):
    output = "| Name: {0} "          \
             "  Seat: {1} "           \
             "  flight_number: {2}"   \
             "  aircraft: {3}"        \
             " |".format(passenger, seat, flight_number, aircraft)
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()     # prints a new line