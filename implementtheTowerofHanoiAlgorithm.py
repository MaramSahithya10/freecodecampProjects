def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    moves = []

    def record():
        moves.append(f"{rods[0]} {rods[1]} {rods[2]}")

    def move_disk(source, target):
        disk = rods[source].pop()
        rods[target].append(disk)
        record()

    def solve(disks, source, target, auxiliary):
        if disks == 1:
            move_disk(source, target)
            return

        solve(disks - 1, source, auxiliary, target)
        move_disk(source, target)
        solve(disks - 1, auxiliary, target, source)

    record()
    solve(n, 0, 2, 1)

    return "\n".join(moves)