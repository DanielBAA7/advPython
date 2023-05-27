fp = open("names_for_chapter1")
names = [name for line in fp for name in line.split()]
fp.close()

# 1. prints the longest name in the file
print("1. The longest name is: " + max(names, key=len))

# 2. prints the total length of all names
print("2. The total length of all the names: " + str(sum([len(name) for name in names])))

# 3. prints the lowest length names in separate rows
min_length = len(min(names, key=len))
print("3. " + "\n".join([name for name in names if len(name) == min_length]))

# 4. creating a new file with the lengths of the names
names_length_file = open("names_lengths_file_for_chapter1.txt", "w")
names_length_file.write("\n".join([str(len(name)) for name in names]))

# 5. prints the names their lengths is the length the user entered
length = int(input("4. Enter a length please: "))
print("\n".join([name for name in names if len(name) == length]))
