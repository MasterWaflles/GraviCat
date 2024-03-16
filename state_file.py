
# Function to store texts as tile maps
def state_file(file):
    # Open the file to read and specify the character set
    with open(file, "r", encoding='utf-8') as file:
        level = file.readlines()
        # Loop to strip all the "\n", which by default are inserted into the end of the lines
        for index in range(0, len(level)):
            line = level[index]
            line = line.rstrip("\n")
            level[index] = line

    return level
