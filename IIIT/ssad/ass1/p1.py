def reset_A():
	global A
	A=[['.','.','.','.','.','.','.','.','.','.','.','X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.','.','.','X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.','.','.','X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.','.','.','X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.','.','.','X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.','.','.','X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
	['X','X','X','X','X','X','X','X','X','X','.','X','X','X','X','X','X','X','X','X','.','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
	['.','.','X','X','.','.','.','.','.','.','.','X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
	['.','.','.','X','.','.','.','.','.','.','.','X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
	['.','.','.','X','.','.','.','.','.','.','.','X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
	['.','.','.','X','.','.','.','.','.','.','.','X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.','.','.','X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.','.','.','X','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
	]
import random

class Board():
	def __init__(self,counter):
		self.counter=counter
	def disp(self):
	 	return self.counter
	def add(self):
		self.counter+=1
class Person():
	def __init__(self,x,y):
		self.x=x
		self.y=y
	
	def __eq__(self,that):
		return self.x==that.x and self.y==that.y
	
	def x_position(self):
		return self.x
	
	def y_position(self):
		return self.y

	def checkWall(self):
		if A[self.x][self.y] == 'X' :
			return True
		else :
			return False

	def checkCoin(self):
		if A[self.x][self.y] == 'C' :
			return True
		else :
			return False

	def checkGhost(self):
		if A[self.x][self.y]=='G':
			return True
		else:
			return False

	def new_cord(self, dx, dy):
		self.x = dx
	        self.y = dy


class Ghost(Person):
	def __init__(self,p):
		self.x=p.x
		self.y=p.y

	def ghostPosition(self):
		return (self.x, self.y)



class Pacman(Person):
	def __init__(self,p):
		self.score=0
		self.x=p.x
		self.y=p.y
	
	def collectCoin(self):
		self.score=self.score+1

	def score(self):
		return self.score
	def changescore(self,sc):
	 	self.score=sc
	

def start():
	global b1

	b1=Board(0)

def create_game():
	import random
#	global counter
#	counter=0
	count=25   #  Number of coins
	while count!=0 :
		cx=random.randint(0,14)
		cy=random.randint(0,34)
		if A[cx][cy]=='.':
			A[cx][cy]='C'
			count=count-1

	count=0
	while 1:
		if count==1:
			break
		p1x=random.randint(0,14)
		p1y=random.randint(0,34)
		if A[p1x][p1y]=='.':
			p1=Person(p1x,p1y)
			global P1
			P1=Pacman(p1)
			A[p1x][p1y]='P'
			count=count+1

	s=b1.disp()*25
	P1.changescore(s)		
	count=10    # Number of ghosts  set
	f=0
	global gh,per
	gh=list()
	per=list()
	while count!=0:
		p2x=random.randint(0,14)
		p2y=random.randint(0,34)
		if A[p2x][p2y]=='.':
			p=Person(p2x,p2y)
			per.append(p)
			gh.append(Ghost(per[f]))
			f+=1
			A[p2x][p2y]='G'
			count=count-1

	global blue,green,red,end,reds
	blue = '\033[94m'
	green = '\033[92m'
	red = '\033[93m'
	reds = '\033[91m'
	end = '\033[0m'

	for i in A:
		for j in i:
			if j=='P':
				print green + j + end,
			elif j=='G':
				print red + j + end,
			elif j=='X':
				print blue + j + end,

			elif j=='C':	
				print reds + j + end,
			else:	
				print j,

		print
	print 'Score :',P1.score
	if b1.disp()!=0:
		play_game()
def play_game():
	v=25
	while 1 :
		print 'Enter move :',
  		import sys, tty, termios
	  	fd = sys.stdin.fileno()
	  	old_settings = termios.tcgetattr(fd)
	  	try:
			tty.setraw(sys.stdin.fileno())
		        move = sys.stdin.read(1)
		finally:
		        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		print move


#		move=raw_input()
		move_ghost()
		if move == 'q':
			return
		elif move == 'w' or move=='s' or move=='a' or move=='d':
			a=P1.x_position()
			b=P1.y_position()
			if move=='w':
				if a>0:
					P1.new_cord(a-1,b)
				else:
					prints()
					continue
			elif move=='s':
				if a<14:
					P1.new_cord(a+1,b)
				else:
					prints()
					continue
			elif move=='a':
				if b>0:
					P1.new_cord(a,b-1)
				else:
					prints()
					continue
			elif move=='d':
				if b<34:
					P1.new_cord(a,b+1)
				else:	
					prints()
					continue
			if P1.checkWall() == False :
				if A[P1.x_position()][P1.y_position()]=='C':
					P1.collectCoin()
					v-=1
				if P1.checkGhost() == True:
					A[a][b]='.'
					prints()
					print 'Game Over....'
					return
				A[P1.x_position()][P1.y_position()]='P'
				if A[a][b]=='G':
					A[a][b]='G'
				else:
					A[a][b]='.'
			else:
				P1.new_cord(a,b)	


		prints()
		if v==0:
			break
	b1.add()
	reset_A()
	create_game()
			

def prints():
	for i in A:
		for j in i:
			if j=='P':
				print green + j + end,
			elif j=='G':
				print red + j + end,
			elif j=='C':	
				print reds + j + end,
			elif j=='X':
				print blue + j + end,
			else:	
				print j,
		print
	print 'Score :',P1.score


def move_ghost():
	
	a=len(gh)
	i=0
	while a!=0:
		x,y=gh[a-1].ghostPosition()
		b=random.randint(0,4)  #0 for right,1 for left,2 for up,3 for down, 4 for same posn
		if b==0:
			if y<34:
				gh[a-1].new_cord(x,y+1)
			else:
				continue
		elif b==1:	
			if y>0:
				gh[a-1].new_cord(x,y-1)
			else:
				continue
		elif b==2:
			if x>0:
				gh[a-1].new_cord(x-1,y)
			else:
				continue
		elif b==3:
			if x<14:
				gh[a-1].new_cord(x+1,y)
			else:
				continue
		if gh[a-1].checkWall() == False and gh[a-1].checkCoin()==False and gh[a-1].checkGhost()==False :
			        A[gh[a-1].x_position()][gh[a-1].y_position()]='G'
				A[x][y]='.'
		else:
			gh[a-1].new_cord(x,y)

		x,y=gh[a-1].ghostPosition()
		a-=1
start()
reset_A()	
create_game()
play_game()
