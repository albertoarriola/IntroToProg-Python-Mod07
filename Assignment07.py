# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   Alberto Arriola, 3/9/2025, Created Script
#   Alberto Arriola, 3/9/2025, Added code to finally statement to handle file = None
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
"""                                             # menu string output
FILE_NAME: str = "Enrollments.json"             # external json file name

# Define the Data Variables
students: list = []  # list variable containing Student objects with student information
menu_choice: str  # str variable containing user's menu selection


class Person:
    """
    Person class

    ChangeLog: (Who, When, What)
    Alberto Arriola, 3/9/2025, Created Class
    """
    # constructor for Person instance
    def __init__(self, first_name: str = "", last_name: str = ""):
        """ This method is the Person class constructor

        :param first_name: string data with first name
        :param last_name: string data with last name
        :return: None

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/9/2025, Created method
        """
        self._first_name = first_name   # first_name property assignment
        self._last_name = last_name     # last_name property assignment

    # getter for the first_name property
    @property
    def first_name(self):
        """ This method is the first_name getter for the Person class

        :param: None
        :return: first_name string in Title format

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/9/2025, Created method
        """
        return self._first_name.title()     # return first_name string in Title format

    # setter for the first_name property
    @first_name.setter
    def first_name(self, value: str):
        """ This method is the first_name setter for the Person class

        :param: value string
        :return: None

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/9/2025, Created method
        """
        # try-except block to handle ValueError
        try:
            if value.isalpha():     # check if first_name string contains only letters
                self._first_name = value       # first_name string is set to passed value if it contains only letters
            else:
                raise ValueError()      # ValueError is raised if first_name doesn't contain only letters
        except ValueError as e:
            # Call to output_error_messages() function in IO class
            IO.output_error_messages("The student's first name should only contain letters.")
        except Exception as e:
            # Call to out_put_error_messages() function in IO class
            IO.output_error_messages("An unexpected error occurred.", e)

    # getter for the last_name property
    @property
    def last_name(self):
        """ This method is the last_name getter for the Person class

        :param: None
        :return: first_name string in Title format

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/9/2025, Created method
        """
        return self._last_name.title()      # return last_name string in Title format

    # setter for the last_name property
    @last_name.setter
    def last_name(self, value: str):
        """ This method is the last_name setter for the Person class

        :param: value string
        :return: None

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/9/2025, Created method
        """
        # try-except block to handle ValueError
        try:
            if value.isalpha():      # check if last_name string contains only letters
                self._last_name = value     # last_name string is set to passed value if it contains only letters
            else:
                raise ValueError()      # ValueError is raised if first_name doesn't contain only letters
        except ValueError as e:
            # Call to output_error_messages() function in IO class
            IO.output_error_messages("The student's last name should only contain letters.")
        except Exception as e:
            # Call to out_put_error_messages() function in IO class
            IO.output_error_messages("An unexpected error occurred.", e)

    # override __str__() method to return Person data
    def __str__(self):
        """ This method is the __str__() override for the Person class

        :param: None
        :return: f string format of first_name and last_name

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/9/2025, Created method
        """
        return f"{self._first_name}, {self._last_name}"

class Student(Person):
    """
    Student class that inherits from the Person class

    ChangeLog: (Who, When, What)
    Alberto Arriola, 3/9/2025, Created Class
    """
    # Student constructor that calls to the Person constructor for first_name and last_name data
    def __init__(self, first_name: str = "", last_name: str = "", course_name: str = ""):
        """ This method is the Person class constructor

        :param first_name: string data with first name
        :param last_name: string data with last name
        :param course_name: string data with course name
        :return: None

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/9/2025, Created method
        """
        super().__init__(first_name = first_name, last_name = last_name)    # call to Person constructor for first_name and last_name
        self._course_name = course_name     # course_name property assignment

    # getter for course_name property
    @property
    def course_name(self):
        """ This method is the last_name getter for the Person class

        :param: None
        :return: course_name string in Title format

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/9/2025, Created method
        """
        return self._course_name.title()    # return course_name string in Title format

    # setter for course_name property
    @course_name.setter
    def course_name(self, value: str):
        """ This method is the last_name setter for the Person class

        :param: value string
        :return: None

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/9/2025, Created method
        """
        self._course_name = value       # course_name string is set to passed value

    # override __str__() method to return Student data
    def __str__(self):
        """ This method is the __str__() override for the Person class

        :param: None
        :return: f string format of first_name, last_name and course_name

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/9/2025, Created method
        """
        return f"{self._first_name}, {self._last_name}, {self._course_name}"



# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    Alberto Arriola, 3/9/2025, Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file and loads it into a list of dictionary rows

        :param file_name: string data with name of file to read from
        :param student_data: list of dictionary rows to be filled with file data

        :return: list

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/9/2025, Created function
        """
        file: object = None
        # try-except block to handle error reading the external file
        try:
            file = open(file_name, "r")     # open external json file
        except Exception as e:
            # call to output_error_messages() function in IO class
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)
        else:
            student_json = json.load(file)  # load contents of external file into student_json list
            file.close()  # close the external file
            # for loop converts students of type Dictionary to Student type
            for student in student_json:
                student_object: Student = Student(first_name=student["FirstName"],
                                                  last_name=student["LastName"],
                                                  course_name=student[
                                                      "CourseName"])  # convert student Dictionary to Student
                student_data.append(student_object)  # append student_object to student_data list of Students
        # finally statement to make sure the external file is closed
        finally:
            if file is None:        # if statement triggered if file is set to None
                file = open(file_name, "w")     # creates a new external Enrollments.json file
                file.close()
            else:
                file.close()        # close external file if it is still open

        return student_data  # return student_data list of Students to the main body


    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/9/2025,Created function
        """

        # try-except block to handle errors writing to the external file
        try:
            list_of_dictionary_data: list[dict] = []    # declare local list variable
            file = open(file_name, "w")     # open external file
            # for loop to convert students from Student to Dictionary type
            for student in student_data:
                student_json: dict = {"FirstName": student.first_name, "LastName": student.last_name, "CourseName": student.course_name}
                list_of_dictionary_data.append(student_json)
            json.dump(list_of_dictionary_data, file)    # load list_of_dictionary_data to external file using .dump()
            file.close()        # close external file
            # call to output_student_and_course_names() function in IO class
            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)
        # finally statement to make sure the external file is closed
        finally:
            if file.closed == False:    # determine if external file is closed
                file.close()    # close external file if it is still open


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    Alberto Arriola, 3/9/2025, Created Class

    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function displays error messages to the user

        : param message: error message in the form of a string,
        : param error: Python Exception info
        : return: None

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/9/2025, Created function
        """
        print(message, end="\n\n")      # print out error message
        if error is not None:       # determine if Python error information is passed to output_error_messages() function
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        :param menu: string with menu text to display

        :return: None

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/9/2025, Created function
        """
        print(menu)     # print out menu
        print()  # extra printline

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        :return: string with the users choice

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/9/2025, Created function
        """
        choice: str = ""    # declare local str variable
        # try-except block to handle invalid entry
        try:
            choice = input("Enter your menu choice number: ")   # print input statement asking for menu selection
            if choice not in ("1","2","3","4"):  # verify choice is valid
                raise Exception("Please, choose only 1, 2, 3, or 4.")    # custom exception message
        except Exception as e:
            # call to output_error_messages() funcion in IO class
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice   # return choice string value to main body

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """ This function displays the student and course names to the user

        :param student_data: list of Student rows to be displayed

        :return: None

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/9/2025, Created function
        """

        print("-" * 50)

        for student in student_data:
            print(f'Student {student.first_name} '
                  f'{student.last_name} is enrolled in {student.course_name}')  # print out each student in student_data list
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """
        This function asks the user to enter student information and
        appends it to the existing list of student information.

        :param student_data: List of Students containing student data
        :return student_data: List of Students containing student data

        ChangeLog: (Who, When, What)
        Alberto Arriola, 3/9/2025, Created function
        """

        # try-except block for exception handling
        student = Student()     # declare local variable of type Student
        # while loop runs until user enters a valid first name
        while (True):
            student.first_name = input("Enter the student's first name: ") # call to Student constructor to add first_name value to student
            if not student.first_name:      # check if student.first_name is empty
                continue    # continue in while loop if student.first_name is empty
            else:
                break       # break out of loop if student.first_name has a value
        # while loop runs until user enters a valid last name
        while (True):
            student.last_name = input("Enter the student's last name: ")    # call to Student constructor to add last_name value to student
            if not student.last_name:       # check if student.last_name is empty
                continue    # continue in while loop if student.last_name is empty
            else:
                break       # break out of loop if student.last_name has a value
        student.course_name = input("Please enter the name of the course: ")    # call to Student constructor to add course_name value to student
        student_data.append(student)    # append student to student_data list
        print()
        print(f"You have registered {student.first_name} {student.last_name} for {student.course_name}.")   # print student info
        return student_data     # return student_data list to main body


# Start of main body

# Call the read_data_from_file() function from the FileProcessor class
# Send file_name str and student_data list as parameters; returned value is assigned to students list
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Call to output_menu() function in the IO class
    # Send menu str as parameter
    IO.output_menu(menu=MENU)

    # Call to input_menu_choice() function in the IO class
    # returned value is assigned to menu_choice str
    menu_choice = IO.input_menu_choice()

    # If-elif-else statements to process user's menu selection
    # Register a student for a course
    if menu_choice == "1":  # If statement triggered if user enters "1"
        # Call to input_student_data() function in IO class
        students = IO.input_student_data(student_data=students)
        continue    # return to start of while loop

    # Show current data
    elif menu_choice == "2":    # elif statement triggered if user enters "2"
        # Call to output_student_and_course_names() function in IO class
        IO.output_student_and_course_names(students)
        continue    # return to start of while loop

    # Save data to a file
    elif menu_choice == "3":    # elif statement triggered if user enters "3"
        # Call to write_data_to_file() function in FileProcessor class
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue    # return to start of while loop

    # Exit the program
    elif menu_choice == "4":   # else statement triggered if user enters "4"
        break  # break out of the while loop

print("Program Ended")      # Print out message that the program has ended
