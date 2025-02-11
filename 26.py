import flet as ft
import numpy as np

def calculate_g(u_input, y_input, result_text):
    # Получаем значения u и y из текстовых полей
    u = float(u_input.value)
    y = float(y_input.value)
    
    # Вычисляем T
    T = np.sin(2 * u) / np.log10(2 * y + u)
    
    # Обновляем текстовое поле с результатом 
    result_text.value =f'T = {T}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №26"
    
    # Создаем текстовые поля для ввода u и y
    u_input = ft.TextField(label="Введите значение для переменной u", width=200)
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)
    
    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления T
    calculate_button = ft.ElevatedButton(text="Вычислить T", on_click=lambda e: calculate_g(u_input, y_input, result_text))

    # Добавляем элементы на страницу
    page.add(u_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)