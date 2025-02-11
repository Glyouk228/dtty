import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №22"
    
    # Создаем текстовые поля для ввода y, x, u
    
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)
    u_input = ft.TextField(label="Введите значение для переменной u", keyboard_type=ft.KeyboardType.NUMBER)
    
    # Создаем кнопку для вычисления
     
    calculate_button = ft.ElevatedButton(text="Вычислить T", on_click=lambda e: calculate())
     
     # Поле для отображения результатов
    result_text = ft.Text("T =", size= 20)
    
    def calculate():
        try:
            y = float(y_input.value)
            x = float(x_input.value)
            u = float(u_input.value)
            T = np.sin(2 * u)*np.log10(2 * np.power(y,2) + np.sqrt(x))
            result_text.value = f"T = {T}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения"
            page.update()
            
# Добавляем элементы на страницу

    page.add(y_input, x_input, u_input, calculate_button, result_text) 
    
# Запускаем приложение
ft.app(target=main)