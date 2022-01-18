
def setup():
    size(800,600)
    #img = loadImage("Yin_and_Yang_symbol.png")
    global points
    points = []
    n = 40
    for i in range(n):
        x = random(width)
        y = random(height)
        points.append( Circle(x,y,1) )
    
    
def draw():
    background(100,100,150)
    for p in range(len(points)):
        points[p].grow()
        points[p].draw()
        for p2 in range(p+1,len(points)):
            dist_ = ( (points[p].x - points[p2].x)**2 + (points[p].y - points[p2].y)**2 )**0.5
            if dist_ <= (points[p].r + points[p2].r):
                points[p].growing = False
                points[p2].growing = False
    
    attempt = add_new_circle(points)
    if attempt != [0,0]:
        points.append( Circle(attempt[0], attempt[1], 1) )
    
    
class Circle():
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.growing = True 
        
    def draw(self):
        fill(self.r*10)
        ellipse(self.x, self.y, self.r*2, self.r*2)
        
    def hits_edges(self):
        return ((self.x-self.r < 0) or (self.x+self.r > width) or (self.y-self.r < 0) or (self.y+self.r > height))
    
    def grow(self):
        if self.growing:
            self.r += 1
        if self.hits_edges():
            self.growing = False
         
               
def add_new_circle(existing_circles):
    x = random(width)
    y = random(height)
    outside_all = True
    for c in existing_circles:
        dist_ = ( (x - c.x)**2 + (y - c.y)**2 )**0.5
        if dist_ <= c.r:
            outside_all = False
            break
    if outside_all:
        return x, y
    else:
        return [0,0]
