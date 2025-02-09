import pygame
import random

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
            screen.fill("white")  # Show reaction screen
            pygame.display.flip()
            start_time = pygame.time.get_ticks()  # Start reaction timer
            reaction_start_time = None  # Stop the delay timer
            waiting_for_click = True  # Now waiting for user click
            click_detected = False  # Reset click flag

    # If not waiting for a click, start a new reaction cycle
    if not waiting_for_click and reaction_start_time is None:
        cnt = random.randint(1, 10) * 1000  # Random delay in milliseconds
        reaction_start_time = pygame.time.get_ticks() + cnt  # Set future time to trigger reaction phase

    # Check if a click happened within the allowed reaction time
    if waiting_for_click:
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # Convert ms to seconds
        if click_detected:
            rounds += 1
            score += 1
            print("Click detected in time! Score increased.")  
            waiting_for_click = False  # Reset reaction phase
            screen.fill("black")
            pygame.display.flip()
        elif elapsed_time > round((random.uniform(0,1)), 2):  # Reaction time window expired
            rounds += 1
            print("Too slow!")
            waiting_for_click = False  # Reset reaction phase
            screen.fill("black")
            pygame.display.flip()

    clock.tick(60)  # Limit FPS to 60

pygame.quit()



print(f"{score}/{rounds}")

#This is Luke's part