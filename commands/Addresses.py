from helpers.decorators import input_error
from classes.Record import Record
from helpers.error import IncorrectAddress


class AddressesCommand:

    @input_error
    def add_address(args, book):
        name, city, street, house_number = args

        if not (isinstance(city, str) and isinstance(street, str)):
            return "City and street must be strings"
        
        try:
            house_number = house_number.strip()
            house_number = int(house_number)
        except ValueError:
            return "House number must be a valid number"
    
        house_number = str(house_number)
        address_parts = [city, street, house_number]
        full_address = ", ".join(address_parts)

        record = book.find(name)

        if not record:
            raise IncorrectAddress(
                f"Name {name} is not in the address book")

        record.add_address(full_address)
        return f"{name}'s Address was successfully added"

    @input_error
    def show_address(args, book):
        name = args[0]
        record = book.find(name)

        if not record:
            raise IncorrectAddress(
                f"Name {name} is not in the address book")
  
        address = record.show_address()

        if address:
            return address
        else:
            return f"There is no recorded address for {name}"
