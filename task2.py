import turtle

def koch_snowflake(length, level):
    if level == 0:
        turtle.forward(length)
    else:
        koch_snowflake(length / 3, level - 1)
        turtle.left(60)
        koch_snowflake(length / 3, level - 1)
        turtle.right(120)
        koch_snowflake(length / 3, level - 1)
        turtle.left(60)
        koch_snowflake(length / 3, level - 1)

def draw_snowflake(length, level):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-length / 2, length / 3)
    turtle.pendown()

    for _ in range(3):
        koch_snowflake(length, level)
        turtle.right(120)

    turtle.done()

# Запитуємо користувача про рівень рекурсії
level = int(input("Введіть рівень рекурсії (від 0 до 5): "))

# Задаємо довжину сторони сніжинки
length = 300

# Викликаємо функцію для малювання сніжинки Коха
draw_snowflake(length, level)