import pygame, sys                                   
pygame.init()             

WIDTH=450                 
HEIGHT=WIDTH*1.5                                                   
size=(WIDTH,HEIGHT)
surface = pygame.display.set_mode(size)

pygame.display.set_caption("Tonga")

BLACK    = (0, 0, 0)                             #Color Constants 
WHITE    = (255, 255, 255)
GRASS    = (19, 133, 16)
RED      = (206, 17, 38)
GRAY = (128, 128,128)
SKY = (135, 206, 235)


# Makes the screen into a 65 by 85 graph
xu = WIDTH/66
yu = HEIGHT/85


clock = pygame.time.Clock()             


def showMessage(words, coords, font, font_size, color, bg=None):
    words_font = pygame.font.SysFont(font, font_size, True, False)
    text_image = words_font.render(words, True, color, bg)
    #get a bounding box for centering
    text_bounds = text_image.get_rect()
    #center text - change center of ret to location
    text_bounds.center = coords
    surface.blit(text_image, text_bounds)

def drawCross(x, y, FlagX): 
    pygame.draw.rect(surface, RED, (x-3*FlagX,y-6*FlagX, 4*FlagX, 10*FlagX),0) #Vertical
    pygame.draw.rect(surface, RED, (x-6*FlagX,y-3*FlagX, 10*FlagX, 4*FlagX),0) #horizontal

def draw_Tonga(x, y, sf): 
    FlagX = WIDTH/3*sf
    FlagY = (2/3)*FlagX
    FlagXU = FlagX/48
    FlagYU = FlagY/24

    pygame.draw.rect(surface, RED, (x, y, 48*FlagXU, 24*FlagYU), 0)
    pygame.draw.rect(surface, WHITE, (x, y, 20*FlagXU, 12*FlagYU), 0)

    drawCross(x+10*FlagXU,y+6*FlagYU, FlagXU)

    pygame.draw.line(surface,GRAY,(x-FlagXU,y),(x,HEIGHT),int(FlagXU))

# -------- Main Program Loop -----------
def main():                               
    while True:
        for event in pygame.event.get():
            if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)): #end game
                pygame.quit()                          
                sys.exit()
      
        surface.fill(SKY)                             
        pygame.draw.rect(surface, GRASS, [0, 70*yu, WIDTH, 15*yu], 0)
        
        draw_Tonga(13*xu, 16*yu, 1)
        draw_Tonga(4*xu, 51*yu, 0.75)
        draw_Tonga(44*xu, 56*yu, 0.5)
        showMessage("Tonga", (WIDTH/2, 8*yu), "Times New Roman", WIDTH//5, RED)
        
    
        pygame.display.update()
        
#----------------------------------------------------------------            
main()                                                   #runs the game