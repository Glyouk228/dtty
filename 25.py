import flet as ft
import numpy as np

def calculate_g(c_input, t_input, result_text):
    # Получаем значения c и t из текстовых полей
    c = float(c_input.value)
    t = float(t_input.value)
    
    # Вычисляем L
    L = np.power(np.cos(c), 2) + 3 * np.power(t, 2) + 4 / np.sqrt(c + t)
    
    # Обновляем текстовое поле с результатом 
    result_text.value =f'L = {L}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №25"
    
    # Создаем текстовые поля для ввода c и t
    c_input = ft.TextField(label="Введите значение для переменной c", width=200)
    t_input = ft.TextField(label="Введите значение для переменной t", width=200)
    
    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления L
    calculate_button = ft.ElevatedButton(text="Вычислить L", on_click=lambda e: calculate_g(c_input, t_input, result_text))

    # Добавляем элементы на страницу
    page.add(c_input, t_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)