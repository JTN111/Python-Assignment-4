x = 'output.txt'
file1 = open(x,'w+')

Write = input("Enter text to write to the file: ")
writing_file = file1.write(Write + "\n")
print(f"Data successfully written to {x}.")

append = input('\nEnter additional text to append: ')
appending = file1.write(append)
print(f"Data successfully appended")

seek = file1.seek(0)
reading_file = file1.read()
print(f"\nFinal content of {x}:\n{reading_file}")


file1.close()
