import pygame
import random as rd
pygame.init()
win=pygame.display.set_mode((500,480))


pygame.display.set_caption("Snake Game")
clk=pygame.time.Clock()
class snake:
    def __init__(self,x,y,width,height):
        self.width=width
        self.height=height
        self.x=x
        self.y=y
    
        
class food:
    def __init__(self,width,height):
        
        self.width=width
        self.height=height
f=food(10,10)

pygame.display.update()
m=snake(100,100,10,10)
b1=snake(111,100,10,10)


l=[]
l1=[100,100]
l.append(m)
l.append(b1)
path=[[144,100],[133,100],[122,100],[111,100]]
run=True
move_left=False
move_right=False
move_up=False
move_down=False
x1=100
y1=100
t=-5
pygame.draw.rect(win,(255,0,0),(x1,y1,f.width,f.height))
pygame.display.update()
eatten=False
while(run):
    pygame.time.delay(100)
    l1[0]=m.x
    l1[1]=m.y
    if m.x>0 and m.x<495 and m.y>30 and m.y<475:
        
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
            
                
            pygame.draw.rect(win,(255,0,0),(0,30,500,5))
            pygame.draw.rect(win,(255,0,0),(495,30,5,480))
            pygame.draw.rect(win,(255,0,0),(0,475,500,5))
            pygame.draw.rect(win,(255,0,0),(0,30,5,480))
            font = pygame.font.SysFont('comicsans',30,True)
            text = font.render("Score:"+str(t),1,(255,0,0))
            win.blit(text,(250,3))
            
            pygame.draw.rect(win,(255,0,0),(m.x,m.y,m.width,m.height))
            pygame.display.update()
            for i in range(0,len(path)):
                pygame.draw.rect(win,(255,0,0),(path[i][0],path[i][1],b1.width,b1.height))
                pygame.display.update()
    
            pygame.display.update()
            
            
            
            if m.x in range(x1,(x1+12)) and m.y in range(y1,(y1+12)):
                eatten=True
                t+=5
            else:
                if move_left or move_right or move_up or move_down:
                  path.pop(0)
                eatten=False
            if eatten==True:
                x1=rd.randint(10,480)
                y1=rd.randint(30,460)
                
            pygame.draw.rect(win,(255,0,0),(x1,y1,f.width,f.height))
            pygame.display.update()
            keys=pygame.key.get_pressed()
            if move_left:
                 l[0].x-=11
            if move_right:
                 l[0].x+=11
            if move_up:
                l[0].y-=11
            if move_down:
                l[0].y+=11
            
            if keys[pygame.K_UP]:
                move_up=True
                move_left=False
                move_right=False
                move_down=False
            if keys[pygame.K_DOWN]:
                move_up=False
                move_left=False
                move_right=False
                move_down=True
            if keys[pygame.K_LEFT]:
                move_left=True
                move_up=False
                move_right=False
                move_down=False
            if keys[pygame.K_RIGHT]:
                move_right=True
                move_up=False
                move_left=False
                move_down=False
            if m.x ==x1 or m.y ==y1:
                eatten=True

            
            
            if move_left or move_right or move_up or move_down:
                path.append([m.x,m.y])
            
            win.fill((0,0,0))
        
        
    else:
        print("Game Over:")
        print("Your Score:"+str(t))
        break
        
    
pygame.quit()
