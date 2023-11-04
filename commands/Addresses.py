from helpers.decorators import input_error
from classes.Record import Record


class AddressesCommand:

    @input_error
    def add_address(args, book):
        if len(args) != 2:
            return "Give me some address please"
        
        name, address = args
        record = book.find(name)
        record.add_address(address)
        return f"{name}'s Address was successfully added"

    @input_error
    def show_address(args, book):
        name = args[0]
        record = book.find(name)
        address = record.show_address()
        if address:
            return address
        else:
            return f"There is no recorded address for {name}"
