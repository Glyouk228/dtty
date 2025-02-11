import flet as ft
import numpy as np

def calculate_g(q_input, y_input, result_text):
    # Получаем значения q и y из текстовых полей
    q = float(q_input.value)
    y = float(y_input.value)
    
    # Вычисляем E
    E = np.log(0.7 * y + 2 * q) / np.sqrt(3 * np.power(y, 2)) + 0.5 * y + 4
    
    # Обновляем текстовое поле с результатом 
    result_text.value =f'E = {E}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №19"
    
    # Создаем текстовые поля для ввода q и y
    q_input = ft.TextField(label="Введите значение для переменной q", width=200)
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)
    
    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления E
    calculate_button = ft.ElevatedButton(text="Вычислить E", on_click=lambda e: calculate_g(q_input, y_input, result_text))

    # Добавляем элементы на страницу
    page.add(q_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)