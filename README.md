# TuteDudePYAssignment4
#Task 1 : Reads a text file and handles error

It should open a file and read the content line by line. 
If file not present , we will get FileNotFound error. 
To avoid that , we should handle it with exception
start with try block
in first line it opens the file named 'sample.txt' in 'r' read mode
then it reads the first line
so , to get the entire text printed in the file we can use file.read 2 times and assigning it to 2 different variables reading , reading1 and print the statements with entire content of characters
so that it prints the content in the file line by line.

in except block
print the statement "Error: The File 'Sample.txt' was not found." . So if the file not present in the system it will not throw error instead , it will print the statement mentioned in except block.

#Task2 : Write and append data to a file
Define a variable FileIn and get input from the user that needs to be wtritten to the file output.txt
Then it opens the file in write mode and writes the user given input to the output.txt file
Then it prints the statement "Data successfully written to output.txt."
then the file closes

Again ask input from the user to add the additional data to the file output.txt. It will be printed in new line
save the input in a variable FileIn
Then it opens the file in append mode and writes the additional content given by the user to the output.txt file.
Then it prints the statement "data successfully appended"
Then file closes

To get the final content of the output.txt file,
it opens the file output.txt file in read mode
it reads the file (file.read()) . to get the content displayed it got assigned to a variable named reading
and it prints the statement in output.txt line by line.
