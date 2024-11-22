
def tower_of_hanoi(n, src, helper, dest):
    if n == 1:
        print(f"Move disk {n} from {src} to {dest}")
        return

    # Move n-1 disks from src to helper using dest
    tower_of_hanoi(n - 1, src, dest, helper)
    # Move the nth disk from src to dest
    print(f"Move disk {n} from {src} to {dest}")
    # Move n-1 disks from helper to dest using src
    tower_of_hanoi(n - 1, helper, src, dest)


# Example usage
n = 3
src = 1
helper = 2
dest = 3
tower_of_hanoi(n, src, helper, dest)
