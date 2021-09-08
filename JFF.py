from tkinter import*
import sqlite3
import pygame
import random

win = Tk()
win.title("Database")

# create a database or connect
conn = sqlite3.connect('gamebook0.db')

# Create cursor
c = conn.cursor()
'''
# Create Table
c.execute("""CREATE TABLE addresses(
name text
)""")
'''


# Create Submit function
def start():

    # create a database or connect
    conn = sqlite3.connect('gamebook0.db')

    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO ADDRESSES VALUES (:name)",
              {
                  'name': name.get(),

              })

    # Commit Changes
    conn.commit()

    # Close connection
    conn.close()
    # To save player's name
    key = name.get().upper()

    # Destory the window created using tkinter
    win.destroy()

    # Initalize pygame
    pygame.init()

    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    dis_width = 700
    dis_height = 400

    # Create a window for the game
    dis = pygame.display.set_mode((dis_width, dis_height))

    # Set a name for the window
    pygame.display.set_caption('Snake Game by RK')

    # To make the snake move at certain time
    clock = pygame.time.Clock()

    # Size of snake
    snake_block = 10
    snake_speed = 13

    just_font = pygame.font.SysFont("times", 25)

    def Your_score(score):
        value = just_font.render("Score: " + str(score), True, yellow)
        dis.blit(value, [0, 0])

    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

    def message(msg, color):
        mesg = just_font.render(msg, True, color)
        dis.blit(mesg, [dis_width / 6, dis_height / 3])

    def gameLoop():
        game_over = False
        game_close = False

        x1 = dis_width / 2
        y1 = dis_height / 2

        x1_change = 0
        y1_change = 0

        snake_List = []
        Length_of_snake = 1

        foodx = round(random.randrange(0, dis_width - 2 * snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - 2 * snake_block) / 10.0) * 10.0

        while not game_over:

            while game_close == True:
                dis.fill(blue)
                message("You Lost! Press R to Retry or Q to Quit", red)
                score = Length_of_snake - 1
                Your_score(score)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_r:
                            gameLoop()
                        global value
                        value = Length_of_snake - 1

                        # Save the player name
                        file0 = open('abc.txt', 'r+')
                        file0.read()
                        file0.write(key + ' - ' + str(value) + '\n')
                        file0.close()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(blue)

            appleImg = pygame.image.load("apple.png")
            dis.blit(appleImg, [foodx, foody, snake_block, snake_block])

            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)

            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            our_snake(snake_block, snake_List)
            Your_score(Length_of_snake - 1)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1

            clock.tick(snake_speed)

        pygame.quit()
        quit()

    gameLoop()


def destroy():
    win.destroy()

def start0():
    if len(name.get())==0:
        Label(win, text='Please enter your name', bg="black", fg="red", font=('times',15)).grid(pady=(0, 20), row=2, column=0, columnspan=2)
    else:
        start()


# Create text boxe
name = Entry(win, bg="grey", fg="white", font=('times', 20), bd=3)
name.grid(row=1, padx=10, pady=10,column=0,columnspan=2)


# Create Label
Label(win, bg="black", fg="white", text='Player Name:', font=('times',20)).grid(row=0, column=0)

# Frames for play buttons
frame = LabelFrame(win, text='Play', bd=5, padx=10, pady=4, fg='black', font=('times', 20), width=312, height=272.5, bg="grey")
frame.grid(row=3,columnspan=2)

# Create play Button
Button(frame, text='Classic', command=start0, bd=5, padx=10, pady=4, bg='black', fg='white', font=('times', 10)).grid(row=3, column=0)
Button(frame, text='Classic_Reverse', command=start0, bd=5, padx=10, pady=4, bg='black', fg='white', font=('times', 10)).grid(row=3, column=1)
Button(frame, text='Duo', command=start0, bd=5, padx=10, pady=4, bg='black', fg='white', font=('times', 10)).grid(row=3, column=2)
Button(win, text='Quit', command=destroy, bd=5, padx=10, pady=4, bg='black', fg='white', font=('times', 20)).grid(row=4, column=0,columnspan=2)

# Query the database
c.execute("SELECT *, oid FROM addresses")
records = c.fetchall()

# Loop through records
print_records = ''
for record in records:
    print_records += str(record[0]) + '\n'

query_label = Label(win, text=print_records, bg="black", fg="white", font=('times',20))
query_label.grid(pady=6,columnspan=2, row=6)

Label(win, bg="black", fg="white", text='Previous Scores:', font=('times',20)).grid(pady=(20, 0), row=5, column=0)

# Commit Changes
conn.commit()

# Close connection
conn.close()

win.config(bg="black")

win.mainloop()