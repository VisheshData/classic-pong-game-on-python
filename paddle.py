from turtle import Turtle
import random



starting_positions_player=[(350,-40),(350,-20),(350,0),(350,20),(350,40)]
starting_positions_splayer=[(-350,-40),(-350,-20),(-350,0),(-350,20),(-350,40)]

class Paddle():
    def __init__(self):
        self.paddle1=[]
        self.paddle2=[]
        
        self.create_paddle()
    
    def create_paddle(self):
        for i in starting_positions_player:
            
            paddle=Turtle("square")
            paddle.color('white')
            paddle.penup()
            paddle.goto(i)
            self.paddle1.append(paddle)

        for i in starting_positions_splayer:
            
            paddle2=Turtle("square")
            paddle2.color('white')
            paddle2.penup()
            paddle2.goto(i)
            self.paddle2.append(paddle2)
            
    def player1moveup(self):
        if self.paddle1[-1].ycor()<280:
            for i in range(0,len(self.paddle1)):
                new_y=self.paddle1[i].ycor()+20
                self.paddle1[i].goto(self.paddle1[i].xcor(),new_y)

    def player1movedown(self):
        if self.paddle1[0].ycor()>-280:
            for i in range(0,len(self.paddle1)):
                new_y=self.paddle1[i].ycor()-20
                self.paddle1[i].goto(self.paddle1[i].xcor(),new_y)
    
    def player2moveup(self):
        if self.paddle2[-1].ycor()<280:
            for i in range(0,len(self.paddle2)):
                new_y=self.paddle2[i].ycor()+20
                self.paddle2[i].goto(self.paddle2[i].xcor(),new_y)

    def player2movedown(self):
        if self.paddle2[0].ycor()>-280:
            for i in range(0,len(self.paddle2)):
                new_y=self.paddle2[i].ycor()-20
                self.paddle2[i].goto(self.paddle2[i].xcor(),new_y)
      
    def computer(self, ball):
    # Find the center of the paddle (use the middle segment as reference)
        
        paddle_center_y = self.paddle2[2].ycor()
    
        # If the ball is above the center of the paddle, move up
        if ball.ycor() > paddle_center_y and self.paddle2[-1].ycor() < 280:
            p_speed=random.randint(1,5)
            for paddle_segment in self.paddle2:
                
                new_y = paddle_segment.ycor() + p_speed
                paddle_segment.goto(paddle_segment.xcor(), new_y)

        # If the ball is below the center of the paddle, move down
        elif ball.ycor() < paddle_center_y and self.paddle2[0].ycor() > -280:
            p_speed=random.randint(5,10)
            for paddle_segment in self.paddle2:
                
                new_y = paddle_segment.ycor() - p_speed
                paddle_segment.goto(paddle_segment.xcor(), new_y)

        


    


    
