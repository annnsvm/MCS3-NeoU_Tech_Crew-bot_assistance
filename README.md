## Chat bot
This console-based bot is a helpful tool that makes it easy for users to organize contact information and notes through a simple text-based interface. It's like having your own digital address book and note-taking system.

### Address Book
The `Address Book` feature allows a user to store and manage contact information. Users can add, view, and update contact details effortlessly.

### Notebook
The `Notebook` feature lets users create and organize their notes with tags. Tags help users categorize and quickly find their notes, making it a handy tool for keeping thoughts and ideas in order.

### Technical requirements
> [!IMPORTANT]
> *NOTE: To ensure proper operation, the installation of `PACKAGE_NAME_HERE_TO_ADD` is required.*

### Commands
| Command | Example | Description |
|:-------|:-------:|:-----------:|
| hello | `hello` | This command displays a greeting message. |
| close or exit | `close` or `exit` | This command ends the interaction with the assistant bot.  |
| all-contacts | `all-contacts` | This command displays all the contacts in the address book. |
| add-contact &lt;name&gt; &lt;phone&gt; | `add-contact Jane 1111111111` | This command adds a new contact to the address book. |
| delete-contact &lt;name&gt; | `delete-contact Jane` | This command allows to delete a contact from the address book by specifying the name. |
| show-phone &lt;name&gt; | `show-phone Jane` | This command allows to find and display phone numbers for a given contact by their name. |
| change-phone &lt;name&gt; &lt;old phone&gt; &lt;new phone&gt; | `change-phone Jane 1111111111 2222222222` | With this command, the user can change the phone number for a specific contact by specifying the name and the old phone number to a new phone number. |
| add-email &lt;name&gt; &lt;email&gt; | `add-email Jane test@gmail.com` | This command adds an email address (email) to the specified contact by name. |
| show-email &lt;name&gt; | `show-email Jane` | This command allows to find and display email for a given contact by their name. |
| add-address &lt;name&gt; &lt;address&gt; | `add-email Jane test@gmail.com` | This command adds an address to the specified contact by name. |
| show-address &lt;name&gt; | `show-address Jane` | This command allows to find and display address for a given contact by their name. |
