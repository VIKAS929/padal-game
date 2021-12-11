from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty,ReferenceListProperty,ObjectProperty
from kivy.vector import Vector
from random import choice
from kivy.clock import Clock

class PongPaddle(Widget):
    score = ObjectProperty(0)
    def bouns_ball(self,ball):
        if self.collide_widget(ball):
            ball.velocity_x *= -1.1

class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x,velocity_y)
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
class PongoGame(Widget):

    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def update(self,dt):
        self.ball.move()
        if (self.ball.y<0) or (self.ball.y>self.height -50):
            self.ball.velocity_y *=-1
        #player score update
        if self.ball.x<0:
            self.ball.velocity_x *= -1
            self.player2.score +=1
        if self.ball.x>self.width -50:
            self.ball.velocity_x *=-1
            self.player1.score +=1
        if (self.player1.score)==10 or (self.player2.score)==10:

            if self.player1.score > self.player2.score:
                self.ids.result.text="Player 1 Winnner"
                self.ball.pos = self.center
            if self.player2.score > self.player1.score:
                self.ids.result.text="Player 2 Winnner"
                self.ball.pos = self.center


        # bouns boll
        self.player1.bouns_ball(self.ball)
        self.player2.bouns_ball(self.ball)

    def serve_ball(self):
        rot=[5,10,15,5,25,35,20,35,40,75,45,80,85,70,60,30,35,55,65,70,5,10,15,20,35,40,45]
        self.ball.velocity = Vector(4,0).rotate(choice(rot))
    def on_touch_move(self, touch):
            if touch.x < self.width /4:
                self.player1.center_y=touch.y
            if touch.x > self.width *3/4:
                self.player2.center_y = touch.y



class PongApp(App):
    def build(self):
        game = PongoGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)


        return game
if __name__ == '__main__':
    app =PongApp()
    app.run()
