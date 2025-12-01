## Радіо сигнали

Будемо створювати маленьку програму по передачі радіо сигналу.

Логіка наступна: при натисканні клавіші інший пристрій виводитиме рядок

1. Відкриваємо https://makecode.microbit.org і створюємо новий проект, вибираємо Python як мову

1. Компоненти які нам потрібні, radio - для передачі, basic для виводу, input для роботи з кнопками
    ```python
    import radio
    import basic
    import input
    ```

1. Додамо функцію обробник надходження даних по радіо

    | Компонент | Опис |
    | - | - |
    | show_string(receivedString) | виклик функції яка виведе на екран рядочок |
    |  pause(100) | зачекати 100 мілісекунд |
    | basic.clear_screen() | очистити екран |
    | radio.on_received_string(on_received_string) | ініціалізувати прослуховування |
    
    ```python
    def on_received_string(receivedString):
        basic.show_string(receivedString)
        pause(100)
        basic.clear_screen()
    radio.on_received_string(on_received_string)
    ```

1. Додаємл функцію для реакції на ввід користувача

    | Компонент | Опис |
    | - | - |
    | radio.send_string("Hello!") | відіслати рядок |
    |  input.on_button_pressed(Button.A, on_button_pressed_a) | ініціалізувати обробку натискання |

    ```python
    def on_button_pressed_a():
        radio.send_string("Hello!")
    input.on_button_pressed(Button.A, on_button_pressed_a)
    ```

1. Ініціалізуємо радіо
    ```python
    radio.set_group(5)
    ```

1. Щоб перевірити роботу нам потрібно перейти https://makecode.microbit.org/---multi# і завантажити проект на два пристрої