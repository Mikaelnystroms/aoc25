STARTING_POINT = 50


def rotate(current: int, direction: str, n: int) -> int:
    if direction == "R":
        return (current + n) % 100
    elif direction == "L":
        return (current - n) % 100
    else:
        raise ValueError(f"Only left or right allowed, not {direction}")


zeros = 0
position = STARTING_POINT

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        d = line[0]
        n = int(line[1:])

        position = rotate(position, d, n)

        if position == 0:
            zeros += 1

print(f"zeros: {zeros}")
