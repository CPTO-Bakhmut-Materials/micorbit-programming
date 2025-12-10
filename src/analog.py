TICK_TIME = 1000                    # Змінна - час очікування
point_x = 2                         # Змінна - X координата
point_y = 2                         # Змінна - Y координата

led.plot(point_x, point_y)          # Засвітити діод на позиції

def on_forever():                   # Оголошуємо функцію яка міститиме наш головний код
    led.unplot(point_x, point_y)    # Виключити діод
    led.plot(point_x, point_y)      # Ввімкнути діод
    pause(TICK_TIME)                # Очікуємо 1000 мілісекунд
forever(on_forever)                 # Говоримо компютеру щоб він постійно викликав функцію