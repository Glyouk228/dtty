import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №17"
    
    # Создаем текстовое поле для ввода y
    
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    
    # Создаем кнопку для вычисления
     
    calculate_button = ft.ElevatedButton(text="Вычислить N", on_click=lambda e: calculate())
     
     # Поле для отображения результатов
    result_text = ft.Text("N =", size= 20)
    
    def calculate():
        try:
            y = float(y_input.value)
            N = 3 * np.power(y,2) + np.sqrt(y + 1)
            result_text.value = f"N = {N}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения"
            page.update()
            
# Добавляем элементы на страницу

    page.add(y_input, calculate_button, result_text) 
    
# Запускаем приложение
ft.app(target=main)