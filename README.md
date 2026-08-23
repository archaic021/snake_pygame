# 🐍 Snake Game in Python

A simple **Snake Game** built using **Python** and the **Pygame** library.

The player controls a snake using the arrow keys and tries to reach the food. When the snake hits the boundary of the game window, the game ends.

## 🎮 Features

* 🐍 Control the snake using arrow keys
* 🍎 Randomly generated food
* 🖥️ 800 × 600 game window
* ⚡ Simple and beginner-friendly Python code
* 💀 Game over when the snake hits the boundary

## 📸 Game Preview

The game contains:

* **White square** → Snake
* **Red square** → Food
* **Black background** → Game area

## 🛠️ Technologies Used

* Python
* Pygame

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/snake-game.git
```

### 2. Navigate to the project folder

```bash
cd snake-game
```

### 3. Install Pygame

```bash
pip install pygame
```

### 4. Run the game

```bash
python snake_game.py
```

## 🎯 Controls

| Key            | Action     |
| -------------- | ---------- |
| ⬆️ Up Arrow    | Move Up    |
| ⬇️ Down Arrow  | Move Down  |
| ⬅️ Left Arrow  | Move Left  |
| ➡️ Right Arrow | Move Right |

## 🧠 How It Works

The game uses a grid-based movement system where each movement changes the snake's position by **20 pixels**.

```python
snake_pos[0] += direction[0]
snake_pos[1] += direction[1]
```

Food is generated at a random position within the game window:

```python
food_pos = [
    random.randrange(0, 40) * 20,
    random.randrange(0, 30) * 20
]
```

The game checks whether the snake touches the boundaries:

```python
if snake_pos[0] < 0 or snake_pos[0] >= 800 or \
   snake_pos[1] < 0 or snake_pos[1] >= 600:
    print("Game Over!")
```

## 🚀 Future Improvements

* 🍎 Add a proper snake body that grows after eating food
* 📊 Add a score system
* 💥 Add collision detection with the snake's own body
* 🔄 Add a restart option
* 🎵 Add sound effects and background music
* 🏆 Add a high-score system
* 🎨 Improve the game interface

## 📁 Project Structure

```text
snake-game/
│
├── snake_game.py
└── README.md
```

## 👨‍💻 Author

**Abhirup Ghosh**

---

⭐ If you like this project, consider giving it a **star** on GitHub!
