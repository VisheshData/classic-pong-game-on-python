# Pong Game 🎮
A classic Pong game built using Python's turtle module. This project includes both Player vs Player and Player vs Computer modes, allowing for competitive gameplay between two users or against an AI.

## Features ✨
### Two Game Modes:
Player vs Player: Both paddles controlled by players.
Player vs Computer: One paddle controlled by the player, the other by AI.
Smooth Ball Movement: The ball bounces off walls and paddles, dynamically increasing speed.
Score System: Each player earns points when the opponent misses the ball.
## Concepts & Programming Logic 🧠
Object-Oriented Programming (OOP) 🔧
The game is built using OOP to manage different components like the ball, paddles, and score. Each class has a specific responsibility:

## Ball Class
Handles ball movement, collision with walls, and bouncing off paddles.

```python

class Ball(Turtle):
    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y *= -1
        
    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
```
The ball moves continuously across the screen, bouncing off walls and paddles.
reset_position() resets the ball to the center after a point is scored.
## Paddle Class
Controls the movement of player paddles or the AI paddle (in computer mode).

```python

class Paddle():
    def player1moveup(self):
        if self.paddle1[-1].ycor() < 280:
            for paddle_segment in self.paddle1:
                new_y = paddle_segment.ycor() + 20
                paddle_segment.goto(paddle_segment.xcor(), new_y)
```
The paddle moves up or down with keypresses (for both players or AI in computer mode).
## AI Logic: The computer follows the ball's position with randomized speed to make it challenging.
```python

def computer(self, ball):
    if ball.ycor() > self.paddle2[2].ycor():
        for paddle_segment in self.paddle2:
            paddle_segment.goto(paddle_segment.xcor(), paddle_segment.ycor() + random.randint(1, 5))
```
## Score System 🏆
Tracks and updates scores as players miss the ball.

```python

class Score(Turtle):
    def l_point(self):
        self.l_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", align="center", font=("Courier", 80, "normal"))
```
Points are awarded when a player misses the ball. The score is visually updated on the screen.
## Collision Detection ⚙️
The ball's interaction with paddles and walls is handled by detecting distance.

``` python

if ball.distance(paddle.paddle1[2]) < 50 and ball.xcor() > 320:
    ball.bounce_x()
```
This logic ensures that when the ball comes close to a paddle, it bounces back, simulating a hit.
## How to Play 🕹️
Clone the repository
Run Main.py file
### Choose your game mode:

Player vs Player: Press 'v'
Player vs Computer: Press 'c'
### Controls:

Player 1 (right paddle):
Move Up: Arrow Up
Move Down: Arrow Down
Player 2 (left paddle or computer):
Move Up: 'W'
Move Down: 'S'
## Learnings 💡
OOP Concepts: Utilized classes to structure the game.
Event-driven Programming: Implemented keypress events to control paddles.
Basic AI: Created a simple AI to control the second paddle in computer mode.
Collision Detection: Managed ball-paddle and ball-wall collisions.
## Requirements 📦
Python 3.x
turtle module (pre-installed with Python)
