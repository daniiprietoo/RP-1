import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python encoder.py <input_file> <output_file>")
        return
    puzzle, col_restrictions, row_restrictions = read_input(sys.argv[1])
    output_path = sys.argv[2]

    thermometers = find_thermometers(puzzle)
    encode_to_clingo(thermometers, col_restrictions, row_restrictions, path=output_path)

    print(f"Clingo encoding written to {output_path}")


def read_input(file_path):
    input_data = []
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                input_data.append(line)

    puzzle = input_data[:-2]

    puzzle = []
    for line in input_data[:-2]:
        puzzle.append(list(line))

    col_restrictions_line = input_data[-2]
    row_restrictions_line = input_data[-1]
    
    col_restrictions = list(map(int, col_restrictions_line.split()))
    row_restrictions = list(map(int, row_restrictions_line.split()))

    print("Puzzle:")
    for row in puzzle:
        print("".join(row))
    print("Column restrictions:", col_restrictions)
    print("Row restrictions:", row_restrictions)

    return puzzle, col_restrictions, row_restrictions


def find_thermometers(puzzle: list[list[str]]):
    bulbs = []

    valid_bulbs = {"R", "L", "U", "D"}

    # a bulb will be (row, col, 'direction')
    for r, row in enumerate(puzzle):
        for c, cell in enumerate(row):
            if cell in valid_bulbs:
                bulbs.append((r, c, cell))

    thermometers = []
    thermo_id_counter = 1
    for bulb in bulbs:
        r, c, direction = bulb
        thermo_id = f"t{thermo_id_counter}"
        thermo_id_counter += 1

        # determine: delta of direction and expected next characters in the direction
        if direction == "U":
            delta_r, delta_c = -1, 0
            char_expected = "^"
        elif direction == "D":
            delta_r, delta_c = 1, 0
            char_expected = "v"
        elif direction == "R":
            delta_r, delta_c = 0, 1
            char_expected = ">"
        elif direction == "L":
            delta_r, delta_c = 0, -1
            char_expected = "<"
        else:
            raise ValueError(f"Invalid direction {direction}")

        positions = [(r, c)]
        while 0 <= r + delta_r < len(puzzle) and 0 <= c + delta_c < len(puzzle[0]):
            char = puzzle[r + delta_r][c + delta_c]
            if char != char_expected:
                break
            r, c = r + delta_r, c + delta_c
            positions.append((r, c))

        thermometers.append((thermo_id, positions))

    return thermometers


def encode_to_clingo(thermometers, col_restrictions, row_restrictions, path):
    n = len(row_restrictions)

    with open(path, "w") as f:
        f.write(f"dim({n}).\n")
        # Write thermometers
        for thermo_id, positions in thermometers:
            for idx, (r, c) in enumerate(positions):
                f.write(f"position(thermometer_{thermo_id},{idx},{r},{c}).\n")  # 0-based indexing

        # Write row restrictions
        for r, restriction in enumerate(row_restrictions):
            f.write(f"row_restriction({r},{restriction}).\n")

        # Write column restrictions
        for c, restriction in enumerate(col_restrictions):
            f.write(f"col_restriction({c},{restriction}).\n")


if __name__ == "__main__":
    main()
