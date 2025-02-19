import random
#Vincent's game with Luke's profiling at the end
def react_test():
    import pygame

    #Variables to keep track of the score, and amount of rounds
    score = 0
    rounds = 0

    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    click_detected = False
    waiting_for_click = False
    start_time = None  
    reaction_start_time = None  # Timer for reaction delay

    while running:
        screen.fill("black")  # Clear the screen

        # Handle Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and waiting_for_click:
                click_detected = True
                print("Mouse clicked!")

        # If waiting for the delay before reaction starts
        if reaction_start_time is not None:
            if pygame.time.get_ticks() >= reaction_start_time:  # Check if delay is over
                screen.fill("white") #Screen goes white
                pygame.display.flip()
                start_time = pygame.time.get_ticks()  # Starts timer
                reaction_start_time = None  # Stop timer to wait random amount of time
                waiting_for_click = True  # Wait for click
                click_detected = False  # Reset to make sure isn't already clicked

        # If not waiting for a click, make a new wait time
        if not waiting_for_click and reaction_start_time is None:
            cnt = random.randint(1, 10) * 1000  # Random delay in MILLESECONDS
            reaction_start_time = pygame.time.get_ticks() + cnt  # Set time to make screen white

        # Check if a click happened when screen white
        if waiting_for_click:
            elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # Convert milleseconds to seconds
            if click_detected:

                #Add to score and rounds
                rounds += 1
                score += 1
                print("Click detected in time! Score increased.")  
                waiting_for_click = False  # Reset reaction phase
                screen.fill("black")
                pygame.display.flip()
            elif elapsed_time > round((random.uniform(0.1,1)), 2):  # If it was not clicked in random amount of time, 0.1-1 seconds long
                rounds += 1
                print("Too slow!")
                waiting_for_click = False  # Reset reaction phase
                screen.fill("black")
                pygame.display.flip()

        clock.tick(60)  # Limit FPS to 60

    pygame.quit()



    print(f"{score}/{rounds}")

    #This is Luke's part





def guess_1_4():
    rpt = 1
    score = 0
    rounds = 0
    while rpt > 0:
        gs = int(input("\n\nGuess a number 1-4!\n"))
        cgs = random.randint(1,4)
        if gs == cgs:
            score += 1
            rounds += 1
            print("You guessed the computer's number!")
            print(score,"/",rounds)
            ask = input("Would you like to play again?\n1 for yes\n2 for no\n")
            if ask == "1":
                rpt = 1
            else:
                rpt = 0
        else:
            rounds += 1
            print("You did not guess the correct number!")
            print(score,"/",rounds)
            ask = input("Would you like to play again?\n1 for yes\n2 for no\n")
            if ask == "1":
                rpt = 1
            else:
                rpt = 0
    print("\n\n\n",score,"/",rounds)
    print("This is your final score")
    #This is Luke's part
ans = int(input("Which game would you like to play?\n1 for reaction test\n2 for number guess\n"))
if ans == 1:
    react_test()
elif ans == 2:
    guess_1_4()