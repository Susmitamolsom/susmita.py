from tkinter import*
import random,time

class Ball:
	def __init__(self,canvas,paddle,color):
		self.canvas=canvas
		self.id=canvas.create_oval(10,10,25,25,fill=color)
		self.canvas.move(self.id,245,100)
		self.x=0
		self.y=-1
		self.canvas_height=self.canvas.winfo_height()
		self.canvas_width=self.canvas.winfo_width()
		starts=[-3,-2,-1,1,2,3]
		random.shuffle(starts)
		self.x=starts[0]
		self.y=-3
		self.hit_bottom=False

	def hit_paddle(self,pos):
		paddle_pos =self.canvas.coords(paddle.id)
		if pos[2] >=paddle_pos[0] and pos[0] <=paddle_pos[2]:
			if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
				return True
		return False
	def draw(self):
		self.canvas.move(self.id,self.x,self.y)
		pos=self.canvas.coords(self.id)
		if pos[1]<=0:
			self.y=3
		if pos[3]>=self.canvas_height:
			self.y=-3
		if pos[3]>=self.canvas_height:
			self.hit_bottom=True
		if self.hit_paddle(pos)==True:
			self.y=-3
		if pos[0]<=0:
			self.x=3
		if pos[2]>=self.canvas_width:
			self.x=-3

class Paddle:
	def __init__(self,canvas,color):
		self.canvas=canvas
		self.id=canvas.create_rectangle(0,0,120,10,fill=color)
		self.canvas.move(self.id, 300, self.canvas.winfo_height()-80)
		self.x=0.01
		self.canvas_width=self.canvas.winfo_width()
		self.stop=False
		self.canvas.bind_all("<KeyPress-Left>",self.turn_left)
		self.canvas.bind_all("<KeyPress-Right>",self.turn_right)
		self.canvas.bind_all("<Button-1>",self.stop_ball)

	def turn_left(self,evt):
		self.x=-2

	def turn_right(self,evt):
		self.x=2
	def draw(self):
		self.canvas.move(self.id,self.x,0)
		pos=self.canvas.coords(self.id)
		if pos[0]<=0:
			self.x=0
		elif pos[2]>=self.canvas_width:
			self.x=0
	def stop_ball(self,evt):
		self.stop=True
play=Tk()
play.title("Bounce Ball")
play.resizable(0,0)
play.wm_attributes("-topmost",1)
canvas=Canvas(play,width=720,height=540,bd=0,highlightthickness=0)
canvas.pack()
play.update()

paddle=Paddle(canvas,"blue")
ball=Ball(canvas,paddle,"red")
end_game=canvas.create_text(250,200,text="GAME OVER",state="hidden")

while 1:
	if ball.hit_bottom==False and paddle.stop==True:
		ball.draw()
		paddle.draw()
	if ball.hit_bottom==True:
		canvas.itemconfig(end_game,state="normal")
	play.update_idletasks()
	play.update()
	time.sleep(0.01)
