zeros = 0
position = 50

with open("input.txt", "r") as f:
    for line in f:
        # translate the rotation into a signed tick count
        line = line.strip().replace("L", "-").replace("R", "")
        if not line:
            continue

        n = int(line)
        if n < 0:
            # count how many zeros are crossed while turning left
            end_quotient, _ = divmod(position - 1, 100)
            start_quotient, _ = divmod(position + n - 1, 100)
            zeros += end_quotient - start_quotient
        else:
            # count how many zeros are crossed while turning right
            end_quotient, _ = divmod(position + n, 100)
            start_quotient, _ = divmod(position, 100)
            zeros += end_quotient - start_quotient

        position = (position + n) % 100

print(f"zeros: {zeros}")
