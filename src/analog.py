TICK_TIME = 1000                    # Змінна - час очікування
point_x = 2                         # Змінна - X координата
point_y = 2                         # Змінна - Y координата
calibrated_v_x = infinity           # Змінна - X який буде 0
calibrated_v_y = infinity           # Змінна - Y який буде 0

def on_button_pressed_a():                              # Оголошуємо функцію яка буде опрацьовуватися при натисканні
    global calibrated_v_x, calibrated_v_y               # Використати глобальнні змінні
    calibrated_v_x = pins.analog_read_pin(AnalogPin.P0) # Зчитати пін 0 і записати його для подальшої роботи
    calibrated_v_y = pins.analog_read_pin(AnalogPin.P1) # Зчитати пін 1 і записати його для подальшої роботи
input.on_button_pressed(Button.A, on_button_pressed_a)  # Говоримо комп'ютеру яку функцію викликати при натисканні кнопки

led.plot(point_x, point_y)          # Засвітити діод на позиції

def on_forever():                   # Оголошуємо функцію яка міститиме наш головний код
    global point_x, point_y         # Використати глобальнні змінні

    v_x = pins.analog_read_pin(AnalogPin.P0) # Зчитати пін 0
    v_y = pins.analog_read_pin(AnalogPin.P1) # Зчитати пін 1
    led.unplot(point_x, point_y)    # Виключити діод
    point_x = point_x + v_x         # Змістити координату X
    point_y = point_y + v_y         # Змістити координату Y
    led.plot(point_x, point_y)      # Ввімкнути діод
    pause(TICK_TIME)                # Очікуємо 1000 мілісекунд
forever(on_forever)                 # Говоримо комп'ютеру щоб він постійно викликав функцію