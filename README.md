# Python-Assignment-4

**Task1**
used try here(we are trying to open and read the file)
opened the file
assigned the strings(line1 and line2 string in different variables) to respective variables
used read command
used exception for FileDoesntExistError -->can prevents retracing by printing something in the output screen
and finally to continue the rest of the code/program.

**Task2**

used a variable to assign file's name in it to later use the variable in functions,
opened the file in w+ mode(can use.. write + '\n' to write next write/append command input in the next line),

USED WRITE CODE STATEMENTS 
#Write = input("Enter text to write to the file: ")
#writing_file = file1.write(Write + "\n")
#print(f"Data successfully written to {x}.")

THEN USED APPEND STATEMENTS TO WRITE THE NEXT STRING
#append = input('\nEnter additional text to append: ')
#appending = file1.write(append)
#print(f"Data successfully appended")

USED SEEK() FXN WITH 0 AS AN ARGUEMENT TO TAKE THE CURSUR TO THE VERY BEGGINING SO THAT IT READS THE FILE FROM START.
#seek = file1.seek(0)
#reading_file = file1.read()
#print(f"\nFinal content of {x}:\n{reading_file}") --> #USED f'' to use multiple datatypes togehter and formated the output as required

file1.close() --> #CLOSED THE FILE
