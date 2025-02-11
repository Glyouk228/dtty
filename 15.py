import flet as ft
import numpy as np

def calculate_g(j_input, y_input, result_text):
    # Получаем значения w и y из текстовых полей
    j = float(j_input.value)
    y = float(y_input.value)
    
    # Вычисляем F
    F = 2 * np.sin(0.354 * y + 1) / np.log10(y + 2 * j)
    
    # Обновляем текстовое поле с результатом 
    result_text.value =f'F = {F}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №15"
    
    # Создаем текстовые поля для ввода j и y
    j_input = ft.TextField(label="Введите значение для переменной j", width=200)
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)
    
    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления F
    calculate_button = ft.ElevatedButton(text="Вычислить F", on_click=lambda e: calculate_g(j_input, y_input, result_text))

    # Добавляем элементы на страницу
    page.add(j_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)