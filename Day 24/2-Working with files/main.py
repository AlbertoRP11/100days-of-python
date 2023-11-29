# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close() this way we can forget to close the file
# So we use this structure to READ a file
with open("../../../Desktop/my_file.txt") as file:
    content = file.read()
    print(content)
# absolute path: "/Users/User/Desktop/my_file.txt"
# relative path: "../../../Desktop/my_file.txt"

# WRITING in a file
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text")

# if we try to write in a file that doesn't exist, it will create for us
# with open("new_file.txt", mode="w") as file:
#     file.write("New text")
