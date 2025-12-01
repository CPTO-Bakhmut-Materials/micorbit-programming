## Створення кубика для гри

1. Відкриваємо https://makecode.microbit.org і створюємо новий проект

1. Перш за все потрібно додати наші управляючі функції одну для скидання стану, інша буде обробляти події струшування

    | Компонент | Опис |
    | - | - |
    | pass | в python не може бути пустих функції, якщо функція нічого не робить потрібно додавати pass |

    ```python
    def reset():
        basic.clear_screen()
    input.on_button_pressed(Button.A, reset)

    def do_roll():
        pass
    input.on_gesture(Gesture.SHAKE, do_roll)
    ```

1. Додамо базову анімації яка буде програватися

    | Компонент | Опис |
    | - | - |
    | roll_animation = [ ... ] | це масив, тобто декілька об'єктів одного типу |
    | """ ... """ | використовується для того щоб написати ініціалізатор для тексту на декількох рядках редактора |
    | for x in y | це цикл, повторює операції допоки не пройде всі елементи які є в y |

    ```python
        roll_animation = [
            images.create_image("""
                . . . . .
                . # # # .
                . # # # .
                . # # # .
                . . . . .
                """),
            images.create_image("""
                . . . . .
                . . # . .
                . # # # .
                . . # . .
                . . . . .
                """),
            images.create_image("""
                . . . . .
                . # # # .
                . # . # .
                . # # # .
                . . . . .
                """),
        ]

    def play_animation():
        for cycle in range(int(Math.random() * 2) + 1):
            for index in range(len(roll_animation)):
                roll_animation[index].show_image(0)
                pause(100)

    def on_forever():
        play_animation()
    basic.forever(on_forever)
    ```

1. Модифікуємо нашу програму щоб мати стан всередині який буде відповідати за те що ти кинули кубик

    | Компонент | Опис |
    | - | - |
    | is_rolled = False | Створює або записує комірку пам'яті(is_rolled) залежить від контексту |
    | global is_rolled | Змінює контекст - всі операції будуть записом в is_rolled |

    ```python
    is_rolled = False

    def reset():
        global is_rolled
        is_rolled = False
        basic.clear_screen()
    input.on_button_pressed(Button.A, reset)

    def do_roll():
        global is_rolled
        is_rolled = True
    input.on_gesture(Gesture.SHAKE, do_roll)
    ```

1. Тепер додамо головну логіку яка буде відповідати за обчислення кінцевого значення

    ```python
    dice_images = [
        images.create_image("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """),
        images.create_image("""
            . . . . .
            . # . . .
            . . . . .
            . . . # .
            . . . . .
            """),
        images.create_image( """
            . . . . .
            . . . # .
            . . # . .
            . # . . .
            . . . . .
            """),
        images.create_image( """
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            . . . . .
            """),
        images.create_image( """
            . . . . .
            . # . # .
            . . # . .
            . # . # .
            . . . . .
            """),
        images.create_image( """
            . . . . .
            . # # # .
            . . . . .
            . # # # .
            . . . . .
            """),
        ]

    def on_forever():
        global is_rolled
        if is_rolled:
            play_animation()

            roll = Math.round(Math.random() * 5)
            image_to_show = dice_images[int(roll) % len(dice_images)]
            image_to_show.show_image(0)
            pause(100)

            is_rolled = False
    basic.forever(on_forever)
    ```
