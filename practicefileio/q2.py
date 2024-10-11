# Open the file in read mode to read its content
f = open("practice.txt", "r")
data = f.read()
f.close()  # Close the file after reading

# Replace "Java" with "Python" in the content
new_data = data.replace("Java", "Python")
print(new_data)  # Print the modified content

# Open the file again in write mode to overwrite it with the modified content
f = open("practice.txt", "w")
f.write(new_data)
f.close()  # Close the file after writing
