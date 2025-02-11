import flet as ft
import numpy as np

def calculate_g(i_input, y_input, result_text):
    # Получаем значения i и y из текстовых полей
    i = float(i_input.value)
    y = float(y_input.value)
    
    # Вычисляем L
    L = 0.81 * np.cos(i) / np.log10(y) + 2 * np.power(i, 3)
    
    # Обновляем текстовое поле с результатом 
    result_text.value =f'L = {L}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №6"
    
    # Создаем текстовые поля для ввода i и y
    i_input = ft.TextField(label="Введите значение для переменной i", width=200)
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)
    
    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления L
    calculate_button = ft.ElevatedButton(text="Вычислить L", on_click=lambda e: calculate_g(i_input, y_input, result_text))

    # Добавляем элементы на страницу
    page.add(i_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)