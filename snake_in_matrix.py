from typing import List

class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        row, col = 0, 0

        direction_map = {
            "UP": (-1, 0),
            "DOWN": (1, 0),
            "LEFT": (0, -1),
            "RIGHT": (0, 1)
        }

        for command in commands:
            if command in direction_map:
                dr, dc = direction_map[command]
                row += dr
                col += dc

        final_cell = row * n + col
        return final_cell

solution = Solution()
n1 = 2
commands1 = ["RIGHT", "DOWN"]
print(solution.finalPositionOfSnake(n1, commands1))  # Output: 3

n2 = 3
commands2 = ["DOWN", "RIGHT", "UP"]
print(solution.finalPositionOfSnake(n2, commands2))  # Output: 1
