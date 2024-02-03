import random

def random_walker(steps):
    x, y = 0, 0
    directions = ["UP", "DOWN", "LEFT", "RIGHT"]

    print("Starting position: (0, 0)")

    for step in range(steps):
        direction = random.choice(directions)
        
        if direction == "UP":
            y += 1
        elif direction == "DOWN":
            y -= 1
        elif direction == "LEFT":
            x -= 1
        elif direction == "RIGHT":
            x += 1

        print(f"Step {step + 1}: Moved {direction}. New position: ({x}, {y})")

    print("Random Walker finished.")

if __name__ == "__main__":
    num_steps = int(input("Enter the number of steps for the Random Walker: "))
    random_walker(num_steps)
