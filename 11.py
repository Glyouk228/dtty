import flet as ft
import numpy as np

def calculate_g(n_input, y_input, result_text):
    # Получаем значения n и y из текстовых полей
    n = float(n_input.value)
    y = float(y_input.value)
    
    # Вычисляем D
    D =  np.power(y, 2) + 0.5 * n + 4.8 / np.sin(y)
    
    # Обновляем текстовое поле с результатом 
    result_text.value =f'D = {D}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №11"
    
    # Создаем текстовые поля для ввода n и y
    n_input = ft.TextField(label="Введите значение для переменной n", width=200)
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)
    
    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления D
    calculate_button = ft.ElevatedButton(text="Вычислить D", on_click=lambda e: calculate_g(n_input, y_input, result_text))

    # Добавляем элементы на страницу
    page.add(n_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)