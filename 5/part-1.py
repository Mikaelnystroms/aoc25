with open("input.txt", "r") as f:
    lines = f.readlines()


empty_line_index = lines.index("\n")
ranges = lines[:empty_line_index]
ids = lines[empty_line_index + 1 :]
ranges = [r.strip() for r in ranges]
ids = [int(i.strip()) for i in ids]

fresh_ids = []

for current_id in ids:
    in_range = False
    for raw_range in ranges:
        range_start, range_end = [int(value) for value in raw_range.split("-")]
        if range_start <= current_id <= range_end:
            fresh_ids.append(current_id)
            in_range = True
            break
    if not in_range:
        continue

print(f"fresh IDs: {len(fresh_ids)}")
