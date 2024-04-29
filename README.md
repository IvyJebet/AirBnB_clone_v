# ALX-Holberton BnB README

## Project Description
The ALX-Holberton BnB represents the culmination of my four-month journey at the ALX-Holberton School, where I have been immersed in the fullstack software engineering program. This project aims to replicate the functionality of the Airbnb website using my own server. The final version of this project will include:

- A command interpreter facilitating data manipulation without a visual interface, similar to a shell (primarily for development and debugging purposes).
- A website (front-end) offering both static and dynamic functionalities.
- A robust database to manage backend operations effectively.
- An API facilitating communication between the front and backend of the system.

## Key Concepts
Throughout this project, you'll encounter various fundamental concepts, including:

- Creation of Python packages.
- Development of a command interpreter in Python using the cmd module.
- Implementation of Unit testing in a large-scale project.
- Serialization and deserialization of a Class.
- Handling JSON files for data storage.
- Management of datetime.
- Utilization of UUIDs.
- Understanding and application of *args and **kwargs.
- Handling named arguments in functions.

## File Structure
- The `models` directory contains all classes used in the project, with each class representing an object/instance.
- The `tests` directory houses all unit tests.
- `console.py` serves as the entry point for our command interpreter.
- `models/base_model.py` contains the base class for all models, incorporating common elements such as `id`, `created_at`, and `updated_at`, along with methods like `save()` and `to_json()`.
- The `models/engine` directory hosts all storage classes, initially featuring `file_storage.py`.

## Project Phases
### Phase One
- Establish a robust storage system to abstract object storage and persistence.
- Implementation includes:
  - Introducing a parent class (`BaseModel`) to handle initialization, serialization, and deserialization of future instances.
  - Creating a simple flow for serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
  - Defining classes for AirBnB objects (User, State, City, Place, etc.) inheriting from `BaseModel`.
  - Development of the initial storage engine: File storage.
  - Writing unit tests to validate all classes and storage engines.
- Key functionalities:
  - Creation of a data model.
  - Object management (creation, update, deletion, etc.) via a console/command interpreter.
  - Storage and persistence of objects to JSON files.

## Command Interpreter Overview
### Commands
- `quit`: Quits the console.
- `Ctrl+D`: Quits the console.
- `help` or `help <command>`: Displays all commands or instructions for a specific command.
- `create <class>`: Creates an object of a specified class, saves it to a JSON file, and prints the object's ID.
- `show <class> <ID>`: Shows the string representation of an object.
- `destroy <class> <ID>`: Deletes an object.
- `all` or `all <class>`: Prints string representations of all objects or all objects of a specific class.
- `update <class> <id> <attribute name> "<attribute value>"`: Updates an object with a specified attribute (new or existing).
- `<class>.all()`: Equivalent to `all <class>`.
- `<class>.count()`: Retrieves the number of objects of a certain class.
- `<class>.show(<ID>)`: Equivalent to `show <class> <ID>`.
- `<class>.destroy(<ID>)`: Equivalent to `destroy <class> <ID>`.
- `<class>.update(<ID>, <attribute name>, <attribute value>)`: Equivalent to `update <class> <ID> <attribute name> <attribute value>`.
- `<class>.update(<ID>, <dictionary representation>)`: Updates an object based on a dictionary representation of attribute names and values.

## Execution
The shell operates in both interactive and non-interactive modes:

### Interactive Mode:
```bash
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
(hbnb) 
(hbnb) quit
$
```

### Non-interactive Mode:
```bash
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
```

## Conclusion
The ALX-Holberton BnB project offers an in-depth exploration of various software engineering concepts, providing a comprehensive learning experience in full-stack development. Through this README, you're equipped with essential information to navigate and contribute effectively to this project.

## Contact
For any inquiries or feedback, please contact [Ivy Jebet, Earljoe Kadima](mailto:your-jebetivy388@gmail.com, ).
