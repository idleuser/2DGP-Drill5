from pico2d import *

open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('link_sprite.png')

def handle_events():
    global state,dirX,dirY
    global x,y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            state = 0
        elif event.type == SDL_KEYDOWN:
            if x > 770:
                dirX = 0
                x -= 10
            elif x < 20:
                dirX = 0
                x += 10
            elif y > 570:
                dirY = 0
                y -= 10
            elif y < 30:
                dirY = 0
                y += 10
            elif event.key == SDLK_RIGHT and x < 770:
                dirX += 10
                state = 8
            elif event.key == SDLK_LEFT and x > 20:
                dirX -= 10
                state = 6
            elif event.key == SDLK_UP and y < 570:
                dirY += 10
                state = 7
            elif event.key == SDLK_DOWN and y > 30:
                dirY -= 10
                state = 5
            elif event.key == SDLK_ESCAPE:
                state = 0
        elif event.type == SDL_KEYUP:
            dirX = 0
            dirY = 0
            if event.key == SDLK_RIGHT:
                state = 4
            elif event.key == SDLK_LEFT:
                state = 2
            elif event.key == SDLK_UP:
                state = 3
            elif event.key == SDLK_DOWN:
                state = 1

dirX = 0
dirY = 0
state = 1
x = 800 // 2
y = 600 // 2
frame = 0

while state:
    clear_canvas()
    ground.draw(400,300)
    #character.clip_composite_draw(frame * 100, 0, 100, 100,0,'h', x, y,100,100)
    if state == 1:
        character.clip_draw(frame * 90, 7*98, 90, 98, x, y)
        frame = (frame + 1) % 3
    elif state == 2:
        character.clip_draw(frame * 90, 6*98, 90, 98, x, y)
        frame = (frame + 1) % 3
    elif state == 3:
        character.clip_draw(frame * 90, 5*98, 90, 98, x, y)
        frame = 0
    elif state == 4:
        character.clip_draw(frame * 90, 4*98, 90, 98, x, y)
        frame = (frame + 1) % 3
    elif state == 5:
        character.clip_draw(frame * 90, 3*98, 90, 98, x, y)
        frame = (frame + 1) % 10
    elif state == 6:
        character.clip_draw(frame * 90, 2*98, 90, 98, x, y)
        frame = (frame + 1) % 10
    elif state == 7:
        character.clip_draw(frame * 90, 1*98, 90, 98, x, y)
        frame = (frame + 1) % 10
    elif state == 8:
        character.clip_draw(frame * 90, 0, 90, 98, x, y)
        frame = (frame + 1) % 10
    update_canvas()
    handle_events()
    x += dirX
    y += dirY
    delay(0.1)


close_canvas()