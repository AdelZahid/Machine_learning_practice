def isSafe(arr, x, y, n):
    """Check if the cell (x, y) is safe to visit."""
    if x < n and y < n and arr[x][y] == 1:
        return True
    return False

def ratInMaze(arr, x, y, n, sol):
    """Solve the maze using backtracking."""
    # Base condition: If destination is reached
    if x == n - 1 and y == n - 1:
        sol[x][y] = 1
        return True

    if isSafe(arr, x, y, n):
        # Mark the current cell as part of the solution path
        sol[x][y] = 1
        
        # Move down in the maze
        if ratInMaze(arr, x + 1, y, n, sol):
            return True

        # Move right in the maze
        if ratInMaze(arr, x, y + 1, n, sol):
            return True
        
        # Backtrack: Unmark this cell as part of the solution
        sol[x][y] = 0

    return False

# Driver code
n = int(input("Enter the size of the matrix (n x n): "))

# Initialize the maze
print(f"Enter the {n} x {n} matrix row by row (1 for path, 0 for wall):")
arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

# Initialize the solution matrix
sol = [[0 for _ in range(n)] for _ in range(n)]

if ratInMaze(arr, 0, 0, n, sol):
    print("Solution matrix:")
    for row in sol:
        print(" ".join(map(str, row)))
else:
    print("No solution exists for the given maze.")
