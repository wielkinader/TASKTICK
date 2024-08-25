#Tasktick
Tasktick is a simple CLI based To-Do List application which keeps as simple as possible to avoid distractions.

## How To Run
### Installing Dependencies
To run the file navigate to the `src` folder in your terminal to find the `main.py` file which is required to run the program.
>`venv`
>> `src`


1. **Create and Activate a Virtual Environment**
   - On macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
     
## Running the file
To run the file simply type `python` or `python3` in your terminal followed by the path to `main.py`.

## Usage
The Tasktick program operates on 4 main commands:
- `help` - This command gives you a list of all commands and their use
- `add` - This command adds new tasks which will be marked ‘In Progress’ when added
- `progress` - This command tells you which tasks you have, and haven’t completed
- `tick` - This command checks -off tasks to mark them complete
- `clear` - This removes an **completed** tasks from the database
- `clearall` - This removes **ALL** tasks from the database
- `quit` - This command closes the application
