# Sub-Spire Game
import pygame
import sys
from button import Button
import time

pygame.init()

# stuff
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sub-Spire: Start Screen")
clock = pygame.time.Clock()

# Fonts
title_font = pygame.font.Font("Pixeltype.ttf", 150)
font = pygame.font.SysFont("Pixeltype.ttf", 32)
get_font = pygame.font.SysFont("arialblack", 20)

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (28, 245, 20)
BLUE = (20, 196, 245)
RED = (220, 50, 50)
GRAY = (80, 80, 80)

# bar values
money = 30
popularity = 30

current_customer = 0
game_state = "PLAYING"

# images
start_BG = pygame.image.load("Start screen.png")

level_one_bg = pygame.image.load("Photos/level1.png")
dialogue = pygame.image.load("Photos/Dialogue Box.png")
tutorial_guys = pygame.image.load("Photos/tutorial_vid.png")
arrow = pygame.image.load("Photos/Arrow.png")
mini_dialogue = pygame.image.load('Photos/mini_dialogue_box.png')
customers = [
    pygame.image.load("Photos/customer_kid.png"),
    pygame.image.load("Photos/mean guy.png"),
    pygame.image.load("Photos/fatha.png"),
    pygame.image.load("Photos/friend.png"),
    pygame.image.load("Photos/geek_kid.png")
]

#placeholder questions
level_one_questions = [
    {
        "name": "Kid",
        "choices": [
            ("Make cheap game", 10, -5),
            ("Make good game", -5, 10),
            ("Refuse job", 5 , -5),
            ("Give old games", 0, 5)
        ]
    },
    {
        "name": "Bully",
        "choices": [
            ("Give what he wants", 5, 5),
            ("Treat fairly", 10, 0),
            ("Give discount", 0, 10),
            ("Refuse Job", 5, -5)
        ]
    },
    {
        "name": "Father",
        "choices": [
            ("Take advice", 10, 5),
            ("Wave off", 0, -5),
            ("Refuse advice", 5, 5)
        ]
    },
    {
        "name": "Friend",
        "choices": [
            ("Make free game", -5, 10),
            ("Charge him", 10, 5),
            ("Refuse job", 0, -5),
        ]
    },
    {
        "name": "Nice Kid",
        "choices": [
            ("Anime style game", 5, 10),
            ("Spin-off game", 5, 5),
            ("Basic game", 5, 0),
            ("Don't make game", 0, -5)
        ]
    }
]

# Draw Texts
def draw_text(text, text_font, text_col, x, y):
    img = text_font.render(text, True, text_col)
    screen.blit(img, (x, y))

# TYPEWRITER!!!! (took me hours to create ts)
def typewriter(text, x_cord, y_cord, bg_img=None, box_img=None,speaker=None, show_money=False,
               show_popularity=False,show_arrow=False):

    char_count = 0
    speed_counter = 0

    max_chars_per_line = 700 // 14

    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()

        if len(test_line) <= max_chars_per_line:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    total_chars = len("\n".join(lines))

    while char_count <= total_chars + 30:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        speed_counter += 1

        if speed_counter >= 3:
            char_count += 1
            speed_counter = 0

        # Background
        if bg_img:
            screen.blit(bg_img, (0, 0))

        # Money bar
        if show_money:

            pygame.draw.rect(screen,GRAY,(50, 30, 250, 30))
            pygame.draw.rect(screen,GREEN,(50, 30, money * 2.5, 30))
            draw_text(f"Money: {money}/100",font,WHITE,55,32)

        # Popularity bar
        if show_popularity:
            pygame.draw.rect(screen,GRAY,(50, 75, 250, 30))
            pygame.draw.rect(screen,BLUE,(50, 75, popularity * 2.5, 30))
            draw_text(f"Popularity: {popularity}/100",font,WHITE,55,77)

        # Arrow
        if show_arrow:
            screen.blit(arrow, (40, 115))

        # Dialogue box
        if box_img:
            screen.blit(box_img, (50, 350))

        # Character
        if speaker:
            screen.blit(speaker, (62.5, 382.5))

        # Text
        remaining_chars = char_count
        line_spacing = 30

        for index, line in enumerate(lines):
            if remaining_chars <= 0:
                break

            visible_text = line[:remaining_chars]

            text_surface = font.render(visible_text,True,BLACK)

            screen.blit(text_surface,(x_cord, y_cord + index * line_spacing))

            remaining_chars -= len(line) + 1

        pygame.display.flip()
        clock.tick(120)

# starting cutscene
def start_cutscene():

    pygame.display.set_caption("Start Cutscene")

    frames = [
        (pygame.image.load("start_cutscene/cutscene_1.png"), 1000),
        (pygame.image.load("start_cutscene/cutscene_2.png"), 1000),
        (pygame.image.load("start_cutscene/cutscene_3.png"), 1000),
        (pygame.image.load("start_cutscene/cutscene_4.png"), 1000),
        (pygame.image.load("start_cutscene/cutscene_5.png"), 1000),
        (pygame.image.load("start_cutscene/cutscene_6.png"), 1000),
        (pygame.image.load("start_cutscene/cutscene_7.png"), 1000),
        (pygame.image.load("start_cutscene/cutscene_8_vers2.png"), 2000),
        (pygame.image.load("start_cutscene/cutscene_9.2.png"), 2000),
        (pygame.image.load("start_cutscene/cutscene_10.png"), 1000),
        (pygame.image.load("start_cutscene/cutscene_11.png"), 1000),
        (pygame.image.load("start_cutscene/cutscene_12.png"), 1000),
        (pygame.image.load("start_cutscene/cutscene_13.png"), 1000),
        (pygame.image.load("start_cutscene/cutscene_14.png"), 1000),
        (pygame.image.load("start_cutscene/cutscene_15.png"), 1000),
        (pygame.image.load("start_cutscene/cutscene_16.png"), 1000),
        (pygame.image.load("start_cutscene/cutscene_17.png"), 1000)
    ]

    #Skip button
    btn_img = pygame.image.load("blank button.png")

    skip_button = Button(image=btn_img,pos=(100, 25),text_input="Skip Cutscene",font=get_font,base_color="White",hovering_color="Green")

    current_frame = 0
    last_update_time = pygame.time.get_ticks()

    while True:
        clock.tick(60)

        current_time = pygame.time.get_ticks()
        mouse_pos = pygame.mouse.get_pos()

        # Change frame
        if current_time - last_update_time > frames[current_frame][1]:

            current_frame += 1
            last_update_time = current_time

            if current_frame >= len(frames):
                Tutorial_Cutscene()
                return

        screen.blit(frames[current_frame][0], (0, 0))

        #Draw skip button
        skip_button.changeColor(mouse_pos)
        skip_button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if skip_button.checkForInput(mouse_pos):
                    Tutorial_Cutscene()
                    return

        pygame.display.update()

#control menu (troll)
def controls_menu():

    pygame.display.set_caption("Controls Menu")
    controls_bg = pygame.image.load("controls menu.png")

    while True:
        screen.blit(controls_bg, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        back_button = Button(
            image=pygame.image.load("blank button.png"),pos=(400, 275),text_input="Back to menu",font=get_font,base_color="Violet",hovering_color="White")

        back_button.changeColor(mouse_pos)
        back_button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(mouse_pos):
                    start_menu()
                    return

        pygame.display.update()

# the start menu
def start_menu():

    pygame.display.set_caption("Main Menu")

    while True:
        screen.blit(start_BG, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        play_button = Button(
            image=pygame.image.load("blank button.png"),pos=(125, 200),text_input="Start Game",font=get_font,base_color="Blue",hovering_color="White")

        controls_button = Button(
            image=pygame.image.load("blank button.png"),pos=(125, 300),text_input="Controls",font=get_font,base_color="Blue",hovering_color="White")

        quit_button = Button(
            image=pygame.image.load("blank button.png"),pos=(125, 400),text_input="Quit Game",font=get_font,base_color="Blue",hovering_color="White")

        play_button.changeColor(mouse_pos)
        play_button.update(screen)

        controls_button.changeColor(mouse_pos)
        controls_button.update(screen)

        quit_button.changeColor(mouse_pos)
        quit_button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(mouse_pos):
                    start_cutscene()
                    return

                elif controls_button.checkForInput(mouse_pos):
                    controls_menu()
                    return

                elif quit_button.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# Start screen (what player sees first)
def start_screen():

    pygame.display.set_caption("Sub-Spire")

    while True:
        screen.blit(start_BG, (0, 0))

        title = title_font.render("Sub-Spire",False,"#FFD1DC")

        screen.blit(title, (163, 0))

        mouse_pos = pygame.mouse.get_pos()

        start_button = Button(
            image=pygame.image.load("Photos/start button.png"), pos=(400, 450),
            text_input="Press to start", font=get_font,
            base_color="Blue", hovering_color="White"
        )

        start_button.changeColor(mouse_pos)
        start_button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.checkForInput(mouse_pos):
                    start_menu()
                    return

        pygame.display.update()

# the best text cutscene
def Tutorial_Cutscene():
    while True:
        pygame.display.set_caption("Tutorial")

        btn_img = pygame.image.load("blank button.png")
        skip_button = Button(image=btn_img, pos=(100, 25), text_input="Skip Cutscene", font=get_font,
                             base_color="White",
                             hovering_color="Green")
        mouse_pos = pygame.mouse.get_pos()

        # Draw skip button
        skip_button.changeColor(mouse_pos)
        skip_button.update(screen)
        message = (
            "Welcome to 'How to build a business 101'. This is Naugh Treel and Asca Amh, and for the small price of $500 dollars, we will teach you everything there is to know about businesses.")
        typewriter(message,150,375,bg_img=level_one_bg,box_img=dialogue,speaker=tutorial_guys)
        time.sleep(1)

        typewriter("*In the background* Asca: Naugh, our business just got put on the news",150,375,bg_img=level_one_bg,box_img=dialogue,speaker=tutorial_guys)
        typewriter("*talking offscreen* Naugh: Wait, really?",150,375,bg_img=level_one_bg,box_img=dialogue,speaker=tutorial_guys)
        time.sleep(1)

        typewriter("Asca: Yeah.",150,375,bg_img=level_one_bg,box_img=dialogue,speaker=tutorial_guys)
        time.sleep(1)

        typewriter("Naugh: So, we're famous and soon to be successful?",150,375,bg_img=level_one_bg,box_img=dialogue,speaker=tutorial_guys)
        time.sleep(1)

        typewriter("Asca: No",150,375,bg_img=level_one_bg,box_img=dialogue,speaker=tutorial_guys)
        time.sleep(1)

        typewriter("Naugh: What do you mean, 'No'? You said our business is on the news",150,375,bg_img=level_one_bg,box_img=dialogue,speaker=tutorial_guys)
        time.sleep(1)

        typewriter(
            "Asca: Yeah. I 'accidently' lit a fire in the middle of the city "
            "with our company name, and may or may not be responsible "
            "for the harm towards 13 people, and igniting a graveyard. Accidently.",150,375,bg_img=level_one_bg,box_img=dialogue,speaker=tutorial_guys)
        time.sleep(1)

        typewriter(
            "Naugh: ...",
            150,375,
            bg_img=level_one_bg,box_img=dialogue,speaker=tutorial_guys)

        typewriter(
            "Asca: ...",
            150,375,
            bg_img=level_one_bg,box_img=dialogue,speaker=tutorial_guys)

        typewriter(
            "Asca: We're business partners so you'll take half of my sentence, right?",
            150,375,
            bg_img=level_one_bg,box_img=dialogue,speaker=tutorial_guys)
        time.sleep(1)

        typewriter(
            "*LOUD SLAP*",
            150,375,
            bg_img=level_one_bg,box_img=dialogue,speaker=tutorial_guys)
        time.sleep(1)

        typewriter(
            "*Long pause*",
            150,375,
            bg_img=level_one_bg,box_img=dialogue,speaker=tutorial_guys)
        time.sleep(1)

        typewriter(
            "Bob (You): ...",
            75,375,
            bg_img=level_one_bg,box_img=dialogue)
        time.sleep(1)

        typewriter(
            "You: That... was certainly interesting.",
            75,375,
            bg_img=level_one_bg,box_img=dialogue)
        time.sleep(1)

        typewriter(
            "Naugh: *in a more irked tone* This is how to start your own business",
            150,375,
            bg_img=level_one_bg,box_img=dialogue,speaker=tutorial_guys)
        time.sleep(2)

        # Short black transition before the tutorial
        screen.fill(BLACK)
        pygame.display.update()
        time.sleep(1)
        Tutorial()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if skip_button.checkForInput(mouse_pos):
                        Tutorial()
                        return

#The tutorial
def Tutorial():

    pygame.display.set_caption("Tutorial")

    typewriter(
        "Naugh: A good business has customers. Don't discriminate, even if they are a baby.",
        150,375,
        bg_img=level_one_bg,box_img=dialogue,speaker=tutorial_guys)
    time.sleep(0.5)

    typewriter(
        "Naugh: Wait, no. Why would a baby be asking for a game?",
        150,375,
        bg_img=level_one_bg,box_img=dialogue,speaker=tutorial_guys)
    time.sleep(1)

    # Money bar
    typewriter(
        "Naugh: This is your money bar. Don't go bankrupt or else you'll be out of business.",
        150,375,
        bg_img=level_one_bg,box_img=dialogue,speaker=tutorial_guys,show_money=True,show_arrow=True)
    time.sleep(2)

    # Popularity meter
    typewriter(
        "Naugh: And this is your popularity bar. If it gets to 0, you will have no customers, and you'll also be out of business.",
        150,375,
        bg_img=level_one_bg,box_img=dialogue,speaker=tutorial_guys,show_money=True,show_popularity=True,show_arrow=True)
    time.sleep(2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
                Level_1()
                return

    Level_1()

#stats of money and popularity
def draw_stats():

    # Money bar -
    pygame.draw.rect(screen,GRAY,(50, 30, 250, 30))
    pygame.draw.rect(screen,GREEN,(50, 30, money * 2.5, 30))
    draw_text(f"Money: {money}/100",font,WHITE,55,32)

    # Popularity bar
    pygame.draw.rect(screen,GRAY,(50, 75, 250, 30))
    pygame.draw.rect(screen,BLUE,(50, 75, popularity * 2.5, 30))
    draw_text(f"Popularity: {popularity}/100",font,WHITE,55,77)

#draw customer
def draw_customer():
    customer = customers[current_customer]

    screen.blit(
        customer,
        (325, 375)
    )

#creates choices
def make_choice(choice):

    #make these accessible across all functions
    global money
    global popularity
    global current_customer
    global game_state

    selected_choice = level_one_questions[current_customer]["choices"][choice]

    #Change stats
    money += selected_choice[1]
    popularity += selected_choice[2]

    #stats 0-100
    money = max(0, min(100, money))
    popularity = max(0, min(100, popularity))

    #special endings
    if money == 100 and popularity == 0:
        game_state = "MONEY_MAX_POP_ZERO"
        return

    if popularity == 100 and money == 0:
        game_state = "POP_MAX_MONEY_ZERO"
        return

    #win
    if money == 100 or popularity == 100:
        game_state = "WIN"
        return

    #loss (neutral)
    if money == 0 or popularity == 0:
        game_state = "LOSS"
        return

    #next customer
    current_customer += 1

    #ends game
    if current_customer >= 5:
        game_state = "MEDIOCRE"
        return

    # Show a short cutscene before the next customer's choices
    level_one_customer_interactions()

#makes the choice buttons
def draw_choice_buttons():

    buttons = []

    choices = level_one_questions[current_customer]["choices"]

    positions = [
        (240, 135),
        (540, 135),
        (240, 260),
        (540, 260)
    ]

    for i, choice in enumerate(choices):

        button = Button(
            image=pygame.image.load("Photos/mini_dialogue_box.png"),
            pos=positions[i],
            text_input=f"{i + 1}. {choice[0]}",font=get_font,
            base_color="Black",hovering_color="White"
        )
        button.changeColor(pygame.mouse.get_pos())
        button.update(screen)
        buttons.append(button)
    return buttons

# Makes the ending based on bar scores
def draw_ending():

    screen.fill(BLACK)

    if game_state == "WIN":

        draw_text("YOU WIN!", title_font, GREEN,220,100)

        draw_text("Your business became successful!", font, WHITE,200,300)

    elif game_state == "LOSS":

        draw_text("YOU LOSE!", title_font, RED,200,100)

        draw_text("Your business failed.",font,WHITE,250, 300)

    elif game_state == "MONEY_MAX_POP_ZERO":

        draw_text("HOW DID YOU DO THIS?",font,RED,220,150)

        draw_text("You have all the money...", font, WHITE,230,250)

        draw_text("...but literally nobody likes you.", font, WHITE,180,300)

        draw_text("You're basically a politician, but for games.", font, WHITE, 200, 350)

    elif game_state == "POP_MAX_MONEY_ZERO":

        draw_text("CONGRATULATIONS?", font, BLUE,250,150)

        draw_text("Everyone loves your business!", font, WHITE,210,250)

        draw_text("Unfortunately, you have no money. L", font, WHITE,190,300)

    elif game_state == "MEDIOCRE":

        draw_text("CONGRATULATIONS...", font, WHITE,240,150)

        draw_text("Your company is completely mediocre.", font, WHITE,180,250)

        draw_text("You didn't fail. You didn't succeed.",font,WHITE,190,300)

        draw_text("You just... exist.", font, WHITE, 280,350)

#interactions between player and customer
def level_one_customer_interactions():
    # Customer 1 - Mean Kid
    if current_customer == 0:
        message = "Kid: Hey. Aren't you too old to be working out of a stand like this?"
        kid = pygame.image.load('Photos/customer_kid.png')
        typewriter(message, 175, 375, bg_img=level_one_bg, box_img=dialogue, speaker=kid, show_money=True,
                   show_popularity=True)
        time.sleep(1)

        message = "You: ..."
        typewriter(message, 75, 375, bg_img=level_one_bg, box_img=dialogue, show_money=True, show_popularity=True)

        message = "You: (This is why I hate kids. I'm going to smack the hell out of him)"
        typewriter(message, 75, 375, bg_img=level_one_bg, box_img=dialogue, show_money=True, show_popularity=True)
        time.sleep(1)

        message = "You: What do YOU want kid?"
        typewriter(message, 75, 375, bg_img=level_one_bg, box_img=dialogue, show_money=True, show_popularity=True)
        time.sleep(0.5)

        message = "Kid: Well, your sign says you make games. Make me a game."
        typewriter(message, 175, 375, bg_img=level_one_bg, box_img=dialogue, speaker=kid, show_money=True,
                   show_popularity=True)
        time.sleep(0.5)

        message = "You: God, what has happened to manners nowadays."
        typewriter(message, 75, 375, bg_img=level_one_bg, box_img=dialogue, show_money=True, show_popularity=True)

    # Customer 2 - Bully
    elif current_customer == 1:
        bully = pygame.image.load('Photos/mean guy.png')

        typewriter(
            "Tommy: Hey... Bobby, right? The loser from high school?",
            175, 375, bg_img=level_one_bg, box_img=dialogue, speaker=bully,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)

        typewriter(
            "You: What do you want, Tommy?",
            75, 375, bg_img=level_one_bg, box_img=dialogue,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)

        typewriter(
            "Bully: *Laughs*",
            175, 375, bg_img=level_one_bg, box_img=dialogue, speaker=bully,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)

        typewriter(
            "You: What are you laughing at?",
            75, 375, bg_img=level_one_bg, box_img=dialogue,
            show_money=True, show_popularity=True
        )

        typewriter(
            "Bully: You. You're a freaking loser, just exactly how I thought you would be.",
            175, 375, bg_img=level_one_bg, box_img=dialogue, speaker=bully,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)

        typewriter(
            "You: I'm going to murder you",
            75, 375, bg_img=level_one_bg, box_img=dialogue,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)
        typewriter(
            "Bully: Chill broke boy. You're working a child's stand on the road. You need me, the customer, to save your broke loser ass. Make me a game.",
            175, 375, bg_img=level_one_bg, box_img=dialogue, speaker=bully,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)

    # Customer 3 - Father
    elif current_customer == 2:
        father = pygame.image.load('Photos/fatha.png')

        typewriter(
            "Dad: So this is your new business? Finally you did something useful with your life.",
            175, 375, bg_img=level_one_bg, box_img=dialogue, speaker=father,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)

        typewriter(
            "You: Wow, really sensitive dad.",
            75, 375, bg_img=level_one_bg, box_img=dialogue,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)

        typewriter(
            "Dad: Your mother and I didn't send you to Harvard just for you to waste away playing your little computer games, or to make posts on that tik-tak app.",
            175, 375, bg_img=level_one_bg, box_img=dialogue, speaker=father,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)

        typewriter(
            "You: Ok, well. First of all, I was about to enter a tournament to win 5k, and I don't even post on 'tik-tok'. What do you even want anyways?",
            75, 375, bg_img=level_one_bg, box_img=dialogue,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)

        typewriter(
            "Dad: Since you look like you're struggling, let me give you a word of advice.",
            175, 375, bg_img=level_one_bg, box_img=dialogue, speaker=father,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)

    # Customer 4 - Friend
    elif current_customer == 3:
        Friend = pygame.image.load("Photos/friend.png")

        typewriter(
            "Mark: Hey B! What are you doing?",
            175, 375, bg_img=level_one_bg, box_img=dialogue, speaker=Friend,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)

        typewriter(
            "You: Hey M. Got kicked out of my house and now I got to work for a living.",
            75, 375, bg_img=level_one_bg, box_img=dialogue,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)

        typewriter(
            "Mark: Dude. You for real? We got the tourney coming up soon. Do you need somewhere to crash at for a bit?",
            175, 375, bg_img=level_one_bg, box_img=dialogue, speaker=Friend,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)

        typewriter(
            "You: I think I'll be fine, but I'll let you know if I my mind.",
            75, 375, bg_img=level_one_bg, box_img=dialogue,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)

        typewriter(
            "Mark: Alright. Well, let me see something. Make me game.",
            175, 375, bg_img=level_one_bg, box_img=dialogue, speaker=Friend,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)

    # Customer 5 - Nice Kid
    elif current_customer == 4:
        nice_kid = pygame.image.load("Photos/geek_kid.png")

        typewriter(
            "Kid #2: Hey! You! Guy in the cardboard stand!",
            175, 375, bg_img=level_one_bg, box_img=dialogue, speaker=nice_kid,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)

        typewriter(
            "You: *Thinking* Ughh. Another kid. I've got to keep my composure this time",
            175, 375, bg_img=level_one_bg, box_img=dialogue,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)

        typewriter(
            "You: Hi, yes. What can I do for you little man?",
            175, 375, bg_img=level_one_bg, box_img=dialogue,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)

        typewriter(
            "Kid #2: Do you play games??",
            175, 375, bg_img=level_one_bg, box_img=dialogue, speaker=nice_kid,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)

        typewriter(
            "You: *Thinking* I run a stand that makes games. Of course I do, you idiot.",
            175, 375, bg_img=level_one_bg, box_img=dialogue,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)

        typewriter(
            "You: Ah, yes. I guess I do. I make games as well.",
            175, 375, bg_img=level_one_bg, box_img=dialogue,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)

        typewriter(
            "Kid #2: Do you watch anime? I watch one piece! My shirt is a devil fruit!",
            175, 375, bg_img=level_one_bg, box_img=dialogue, speaker=nice_kid,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)

        typewriter(
            "You: *He's annoying, but has good taste at least*",
            175, 375, bg_img=level_one_bg, box_img=dialogue,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)

        typewriter(
            "You: Oh... Nice.",
            175, 375, bg_img=level_one_bg, box_img=dialogue,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)

        typewriter(
            "Kid #2: Hey! You said you make games! Can you make me a game? Please!Please!Please!Please!Please!Please!Please!Please!Please!",
            175, 375, bg_img=level_one_bg, box_img=dialogue, speaker=nice_kid,
            show_money=True, show_popularity=True
        )
        time.sleep(0.5)

#level 1 gameplay handler
def Level_1():
    global money
    global popularity
    global current_customer
    global game_state

    pygame.display.set_caption(
        "Level 1: (Very) Humble Beginnings"
    )

    money = 30
    popularity = 30
    current_customer = 0
    game_state = "PLAYING"

    # Show the first customer's cutscene before the first decision
    level_one_customer_interactions()

    while True:
        # actual gameplay
        if game_state == "PLAYING":

            # Draw the background
            screen.blit(level_one_bg, (0, 0))

            # Draw the bars every frame so they stay on screen and auto update after every choice
            draw_stats()

            # Draw the customer
            draw_customer()

            # Draw choice buttons
            buttons = draw_choice_buttons()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i, button in enumerate(buttons):
                        if button.checkForInput(pygame.mouse.get_pos()):
                            make_choice(i)

        # endings
        else:
            draw_ending()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(60)

start_screen()