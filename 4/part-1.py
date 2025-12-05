with open("input.txt", "r") as f:
    grid = list(f.read().strip().split("\n"))

count = 0

for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell != "@":
            continue
        region = [
            subrow[max(0, c - 1) : c + 2] for subrow in grid[max(0, r - 1) : r + 2]
        ]
        if sum(row.count("@") for row in region) <= 4:
            count += 1

print(f"antal angränsande områden: {count}")
