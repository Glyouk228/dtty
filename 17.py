import flet as ft
import numpy as np

def calculate_g(n_input, y_input, result_text):
    # Получаем значения n и y из текстовых полей
    n = float(n_input.value)
    y = float(y_input.value)
    
    # Вычисляем H
    H = np.power(y, 2) - 0.8 * y + np.sqrt(y) / 23.1 * np.power(n, 2) + np.cos(n)
    
    # Обновляем текстовое поле с результатом 
    result_text.value =f'H = {H}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №17"
    
    # Создаем текстовые поля для ввода n и y
    n_input = ft.TextField(label="Введите значение для переменной n", width=200)
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)
    
    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления H
    calculate_button = ft.ElevatedButton(text="Вычислить H", on_click=lambda e: calculate_g(n_input, y_input, result_text))

    # Добавляем элементы на страницу
    page.add(n_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)