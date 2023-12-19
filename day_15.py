from collections import defaultdict, OrderedDict

def hash_sequence(seq):
    x = 0
    for s in seq:
        x += ord(s)
        x *= 17
        x = x % 256
    return x


if __name__ == '__main__':
    with open('data/day_15/input') as f:
    #with open('data/day_15/example') as f:
        line = f.readline()

    hash_sequence("HASH")
    hashes = [hash_sequence(s.strip()) for s in line.split(",")]

    print(f"Part 1: {sum(hashes)}")

    lens  = [s.strip() for s in line.split(",")]

    boxes = defaultdict(OrderedDict)

    for i, l in enumerate(lens):
        op = "-" if l.endswith("-") else "="

        if op == "=":
            label, focal_str = l.split("=")
            h = hash_sequence(label)
            focal_length = int(focal_str)
            boxes[h][label] = focal_length

        if op == "-":
            label = l[:-1]
            h = hash_sequence(label)
            if label in boxes[h]:
                boxes[h].pop(label)

        # print(f"\nAfter: {l}")
        # for h, v in boxes.items():
        #     box_str = " ".join([f"[{label} {fl}]" for (label, fl) in v.items()])
        #     print(f"Box {h} : {box_str}")

    score = 0
    for h, v in boxes.items():
        for i, (name, fl) in enumerate(v.items()):
            score += (h+1) * (i+1) * fl

    print(f"Part 2: {score}")