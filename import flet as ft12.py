import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №13"

    # Сохдаем текстовые поля дя ввода y
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    
    # Создием кнопку для вычисления 
    calculate_button = ft.ElevatedButton(text="Вычислить E", on_click=lambda e: calculate())

    # Пле для отображения результата
    result_text = ft.Text("E - ", size=20)

    def calculate():
        try:
            y = float(y_input.value)
            K = np.sqrt(np.abs(3 * np.power(y,2) + 0.5 * y + 4))
            result_text.value = f"K - {K}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()
    # Добавляем элементы на страницу
    page.add(y_input, calculate_button, result_text)
 
# Запускаем приложение
ft.app(target=main)