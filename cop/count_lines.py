# python3 cop/count_lines.py

def count_lines(filename):
    count = 0
    with open("foo.txt", 'r') as f:
        for _ in f:
            count += 1
    return count

lines = count_lines('example.txt')
print(f"Number of lines: {lines}")