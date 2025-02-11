import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №21"
    
    # Создаем текстовое поле для ввода y и h
    
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    h_input = ft.TextField(label="Введите значение для переменной h", keyboard_type=ft.KeyboardType.NUMBER)
    
    # Создаем кнопку для вычисления
     
    calculate_button = ft.ElevatedButton(text="Вычислить P", on_click=lambda e: calculate())
     
     # Поле для отображения результатов
    result_text = ft.Text("P =", size= 20)
    
    def calculate():
        try:
            y = float(y_input.value)
            h = float(h_input.value)
            P = np.exp(y + 5.5) + 9.1 * np.power(h,3)
            result_text.value = f"P = {P}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения"
            page.update()
            
# Добавляем элементы на страницу

    page.add(y_input, h_input, calculate_button, result_text) 
    
# Запускаем приложение
ft.app(target=main)