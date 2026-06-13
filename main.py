from graphics import Canvas
import random
import time

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400

PLAYER_SIZE = 25
ZOMBIE_SIZE = 25
SUPPLY_SIZE = 15


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

        # Dark city background
    canvas.create_rectangle(
        0,
        0,
        CANVAS_WIDTH,
        CANVAS_HEIGHT,
        "#222222"
    )
    canvas.create_rectangle(
        180,
        5,
        430,
        45,
        "#8B0000"
    )
    # Title
    canvas.create_text(
        220,
        25,
        "ZOMBIE SURVIVAL",
        "white",
        18
    )

    # Information panel
    canvas.create_rectangle(
        0,
        45,
        170,
        100,
        "darkgreen"
    )

    health_text = canvas.create_text(
        20,
        60,
        "Health: 100",
        "white",
        18
    )

    score_text = canvas.create_text(
    20,
    85,
    "Score: 0",
    "white",
    18
    )

    # Player
    player_x = CANVAS_WIDTH // 2
    player_y = CANVAS_HEIGHT // 2

    player = canvas.create_oval(
        player_x,
        player_y,
        player_x + PLAYER_SIZE,
        player_y + PLAYER_SIZE,
        "blue"
    )
    target_x = player_x
    target_y = player_y
    health = 100
    score = 0
    game_over = False
    game_won = False
    # Create zombies and store their data
    zombies = []

    for i in range(5):
        x = random.randint(0, CANVAS_WIDTH - ZOMBIE_SIZE)
        y = random.randint(120, CANVAS_HEIGHT - ZOMBIE_SIZE)

        zombie = canvas.create_oval(
            x,
            y,
            x + ZOMBIE_SIZE,
            y + ZOMBIE_SIZE,
            "red"
        )

        zombies.append([zombie, x, y])

    # Supplies
    supplies = []

    for i in range(5):
        x = random.randint(0, CANVAS_WIDTH - SUPPLY_SIZE)
        y = random.randint(120, CANVAS_HEIGHT - SUPPLY_SIZE)

        supply = canvas.create_rectangle(
            x,
            y,
            x + SUPPLY_SIZE,
            y + SUPPLY_SIZE,
            "yellow"
        )

        supplies.append([supply, x, y])
    # Zombie movement
        # Game loop
    while True:
            
            key = canvas.get_last_key_press()

            if key == "UP_ARROW" and player_y > 100:
                canvas.move(player, 0, -10)
                player_y -= 10

            elif key == "DOWN_ARROW" and player_y < CANVAS_HEIGHT - PLAYER_SIZE:
                canvas.move(player, 0, 10)
                player_y += 10

            elif key == "LEFT_ARROW" and player_x > 0:
                canvas.move(player, -10, 0)
                player_x -= 10

            elif key == "RIGHT_ARROW" and player_x < CANVAS_WIDTH - PLAYER_SIZE:
                canvas.move(player, 10, 0)
                player_x += 10
            # Keep player inside screen
            if player_x < 0:
                player_x = 0

            if player_x > CANVAS_WIDTH - PLAYER_SIZE:
                player_x = CANVAS_WIDTH - PLAYER_SIZE

            if player_y < 100:
                player_y = 100

            if player_y > CANVAS_HEIGHT - PLAYER_SIZE:
                player_y = CANVAS_HEIGHT - PLAYER_SIZE
            if game_over or game_won:
                break
            for supply in supplies[:]:

                sx = supply[1]
                sy = supply[2]

                if abs(player_x - sx) < 20 and abs(player_y - sy) < 20:

                    canvas.delete(supply[0])

                    supplies.remove(supply)

                    score += 10

                    canvas.change_text(
                        score_text,
                        "Score: " + str(score)
                    )
                    if len(supplies) == 0 and not game_won:

                        canvas.create_rectangle(
                            120,
                            140,
                            480,
                            280,
                            "darkblue"
                        )

                        canvas.create_text(
                            220,
                            180,
                            "YOU WIN!",
                            "yellow",
                            30
                        )

                        canvas.create_text(
                            180,
                            220,
                            "All supplies collected!",
                            "white",
                            18
                        )

                        canvas.create_text(
                            200,
                            250,
                            "Final Score: " + str(score),
                            "white",
                            18
                        )

                        game_won = True
            # Move zombies towards player
            for zombie in zombies:
                shape = zombie[0]
                x = zombie[1]
                y = zombie[2]
                # Collision detection
                distance_x = abs(player_x - x)
                distance_y = abs(player_y - y)

                if distance_x < PLAYER_SIZE and distance_y < PLAYER_SIZE:

                    if health > 0:
                        health -= 1 

                        canvas.change_text(
                            health_text,
                            "Health: " + str(health)
                        )

                        if health == 0:
                            canvas.create_text(
                                220,
                                200,
                                "GAME OVER",
                                "red",
                                30
                            )

                            canvas.create_text(
                                200,
                                240,
                                "Zombie infection defeated you!",
                                "white",
                                18
                            )

                            game_over = True
                if x < player_x:
                    x += 1
                elif x > player_x:
                    x -= 1

                if y < player_y:
                    y += 1
                elif y > player_y:
                    y -= 1

                canvas.move(
                    shape,
                    x - zombie[1],
                    y - zombie[2]
                )

                zombie[1] = x
                zombie[2] = y


            # Move player automatically for testing
            # (we will replace this with mouse control next)

            time.sleep(0.1)

if __name__ == "__main__":
    main()
                
