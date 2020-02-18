import  pygame
import process_digits
import  process_leters

# defining colors
black = [0,0,0]
white = [255,255,255]

# dimensions
width  = 640
height = 800

radius = 7
last_pos = (0, 0)
draw_on = False
typ = ''

print("\n1)Digits \n2)Letters \nEnter your choice : ",end="")
ch = int(input())

if ch == 1 :
    typ = 'digits'
else :
    typ = 'letters'


# start the screen
screen = pygame.display.set_mode((width*2,height))
screen.fill(white)
pygame.font.init()

def crope(original) :
    cropped = pygame.Surface((width-5, height-5))    
    cropped.blit(original, (0, 0), (0, 0, width-5, height-5))
    return cropped

def roundline(scrn, color, start, end, radius=1):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0] + float(i) / distance * dx)
        y = int(start[1] + float(i) / distance * dy)
        pygame.draw.circle(scrn, color, (x, y), radius)

def draw_partition_line():
    pygame.draw.line(screen, black, [width, 0], [width,height ], 8)

def show_output_image(img):
    out_screen = pygame.pixelcopy.make_surface(img)
    out_screen = pygame.transform.rotate(out_screen, -270)
    out_screen = pygame.transform.flip(out_screen, 0, 1)
    screen.blit(out_screen, (width+2, 0))

try :
    while True :

        # wait for events
        event = pygame.event.wait()

        draw_partition_line()

        # termination
        if event.type == pygame.QUIT :
            raise StopIteration

        # clean the screen
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 :
            screen.fill(white)

        #start drawing
        if event.type == pygame.MOUSEBUTTONDOWN and event.button != 3 :
            color = black
            pygame.draw.circle(screen, color, event.pos, radius)
            draw_on = True

        # stop drawing
        if event.type == pygame.MOUSEBUTTONUP and event.button != 3 :
            draw_on = False
            img_name = "snap.png"

            img = crope(screen)
            pygame.image.save(img, img_name)

            if ch == 1 :
                output_image = process_digits.get_output_image(img_name,typ)
            else :
                output_image = process_leters.get_output_image(img_name,typ)
            show_output_image(output_image)

        # start drawing line on screen if draw is true
        if event.type == pygame.MOUSEMOTION:
            if draw_on:
                pygame.draw.circle(screen, color, event.pos, radius)
                roundline(screen, color, event.pos, last_pos, radius)
            last_pos = event.pos

        pygame.display.flip()

except StopIteration :
    pass

pygame.quit()