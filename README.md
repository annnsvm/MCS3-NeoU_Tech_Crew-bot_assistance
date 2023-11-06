## Chat bot
This console-based bot is a helpful tool that makes it easy for users to organize contact information and notes through a simple text-based interface. It's like having your own digital address book and note-taking system.

### Address Book
The `Address Book` feature allows a user to store and manage contact information. Users can add, view, and update contact details effortlessly.

### Notebook
The `Notebook` feature lets users create and organize their notes with tags. Tags help users categorize and quickly find their notes, making it a handy tool for keeping thoughts and ideas in order.

### Technical requirements
> [!IMPORTANT]
> *NOTE: To ensure proper operation, the installation of `prompt_toolkit` is required.*

### Install as a package
`python3 -m venv .env`

Linux, Mac OS: `source .env/bin/activate`  
Windows: `.env/Scripts/activate`

`pip install .`

### Commands
| Command | Example | Description |
|:-------|:-------:|:-----------:|
| help | `help` | This command displays all commands. |
| hello | `hello` | This command displays a greeting message. |
| close or exit | `close` or `exit` | This command ends the interaction with the assistant bot.  |
| all-contacts | `all-contacts` | This command displays all the contacts in the address book. |
| add-contact &lt;name&gt; &lt;phone&gt; | `add-contact Jane 1111111111` | This command adds a new contact to the address book. |
| delete-contact &lt;name&gt; | `delete-contact Jane` | This command allows to delete a contact from the address book by specifying the name. |
| show-phone &lt;name&gt; | `show-phone Jane` | This command allows to find and display phone numbers for a given contact by their name. |
| change-phone &lt;name&gt; &lt;old phone&gt; &lt;new phone&gt; | `change-phone Jane 1111111111 2222222222` | With this command, the user can change the phone number for a specific contact by specifying the name and the old phone number to a new phone number. |
| add-email &lt;name&gt; &lt;email&gt; | `add-email Jane test@gmail.com` | This command adds an email address (email) to the specified contact by name. |
| show-email &lt;name&gt; | `show-email Jane` | This command allows to find and display email for a given contact by their name. |
| add-address &lt;name&gt; &lt;city&gt; &lt;street&gt; &lt;house number&gt; | `add-address Jane Kyiv Khreshchatyk 1` | This command adds an address to the specified contact by name. |
| show-address &lt;name&gt; | `show-address Jane` | This command allows to find and display address for a given contact by their name. |
| add-birthday &lt;name&gt; &lt;birthday&gt; | `add-birthday Jane 01.01.2000` | This command adds a birthday date to the specified contact by name. |
| show-birthday &lt;name&gt; | `show-birthday Jane` | This command allows to find and display birthday for a given contact by their name. |
| birthdays | `birthdays` | This command displays all birthdays for the upcoming week and organizes them by the day of the week. |
| all-notes | `all-notes` | This command displays all the notes in the notebook. |
| add-note &lt;title&gt; "&lt;description&gt;" &lt;tag&gt;, &lt;tag&gt;| `add-note Monday "Meeting with friends" friends, rest` | This command adds a note, description, and tags. They are added optionally. |
| about-note &lt;title&gt; | `about-note Monday` | This command provides information about a specific note by its title. |
| replace-note-text &lt;title&gt; "&lt;description&gt;" | `replace-note-text Monday "Meeting with friends - 18.00"` | This command replaces the description of a note by its title with the new text. |
| add-text-to-note &lt;title&gt; "&lt;description&gt;" | `add-text-to-note Monday "Take board games"` | This command adds new description to a note by its title. |
| add-tags &lt;title&gt;: &lt;tag&gt;, &lt;tag&gt;  | `add-tags Monday: game, evening` | This command adds tags to a note by its title. |
| remove-tag &lt;title&gt;: &lt;tag&gt;  | `remove-tag Monday: evening` | This command removes one tag from a note by its title. |
| remove-note &lt;title&gt;  | `remove-note Monday` | This command removes a note by its title. |
| show-note &lt;title&gt;  | `show-note Monday` | This command shows the description of a note by its title. |
| find-tagged-notes &lt;tag&gt;  | `find-tagged-notes rest` | This command displays the titles of all notes with this tag. |
| tags  | `tags` | This command shows all tags. |