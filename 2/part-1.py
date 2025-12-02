with open("input.txt", "r") as f:
    input = f.read().strip()


ranges = input.split(",")

total_invalid_sum = 0
invalid = []

for range_str in ranges:
    start_str, end_str = range_str.split("-")
    start = int(start_str)
    end = int(end_str)

    for num in range(start, end + 1):
        str_num = str(num)
        length = len(str_num)

        # om udda tal så kan det inte vara upprepade sekvenser
        if length % 2 != 0:
            continue

        midpoint = length // 2

        first_half = str_num[:midpoint]
        second_half = str_num[midpoint:]

        if first_half == second_half:
            total_invalid_sum += num
            invalid.append(num)

print(f"summa ogiltiga IDs: {total_invalid_sum}")
