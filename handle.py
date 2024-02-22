def read_file(filename):
    lines = []
    with open(filename, "r") as file:
        lines = file.readlines()
    return lines

filename = "sample.txt"
lines = read_file(filename)
print("Lines from file:", lines)

