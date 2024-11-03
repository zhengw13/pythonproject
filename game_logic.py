import random


def initialize_grid():
    grid = [[0] * 4 for _ in range(4)]
    add_random_two(grid)
    add_random_two(grid)
    return grid


def add_random_two(grid):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = 2


def move_left(grid):
    new_grid, merged = [], False
    for row in grid:
        new_row, merged_row = compress_and_merge(row)
        if new_row != row:
            merged = True
        new_grid.append(new_row)
    return new_grid, merged


def move_right(grid):
    reversed_grid = [row[::-1] for row in grid]
    new_grid, merged = move_left(reversed_grid)
    return [row[::-1] for row in new_grid], merged


def move_up(grid):
    transposed_grid = transpose(grid)
    new_grid, merged = move_left(transposed_grid)
    return transpose(new_grid), merged


def move_down(grid):
    transposed_grid = transpose(grid)
    new_grid, merged = move_right(transposed_grid)
    return transpose(new_grid), merged


def compress_and_merge(row):
    non_zero = [num for num in row if num != 0]
    new_row = []
    merged = False
    skip = False
    for i in range(len(non_zero)):
        if skip:
            skip = False
            continue
        if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
            new_row.append(non_zero[i] * 2)
            skip = True
            merged = True
        else:
            new_row.append(non_zero[i])
    new_row.extend([0] * (4 - len(new_row)))
    return new_row, merged


def transpose(grid):
    return [list(row) for row in zip(*grid)]


def check_game_over(grid):
    for row in grid:
        if 0 in row:
            return False
    for i in range(4):
        for j in range(4):
            if j + 1 < 4 and grid[i][j] == grid[i][j + 1]:
                return False
            if i + 1 < 4 and grid[i][j] == grid[i + 1][j]:
                return False
    return True


def check_win(grid):
    for row in grid:
        if 2048 in row:
            return True
    return False


def print_grid(grid):
    for row in grid:
        print("\t".join(str(num) if num != 0 else "." for num in row))
    print("\n")

def main():
    try:
        ans1 = input("Initialize game: Yes/No")
    except:
        print("Your Input is not valid please try again")
    if ans1 == "Yes":
        grid = initialize_grid()
        add_random_two(grid)
        iswin = check_win(grid)
        isgameover = check_game_over(grid)
        print_grid(grid)
        while not iswin and not isgameover:
            try:
                next_move = input("give me your next move: L,R,U,D")
            except:
                print("your Input is not valid please try again")
                continue
            if next_move == 'L':
                move_left(grid)
                print_grid(grid)
            elif next_move == 'R':
                move_right(grid)
                print_grid(grid)
            elif next_move == 'U':
                move_up(grid)
                print_grid(grid)
            else:
                move_down(grid)
                print_grid(grid)
            iswin = check_win(grid)
            isgameover = check_game_over(grid)
    else:
        print("play next time thank you!")
