import flet as ft
import numpy as np

def calculate_g(p_input, y_input, result_text):
    # Получаем значения p и y из текстовых полей
    p = float(p_input.value)
    y = float(y_input.value)
    
    # Вычисляем Z
    Z = np.sin(np.power(p + 0.4, 2)) / np.power(y, 2) + 7.325 * p
    
    # Обновляем текстовое поле с результатом 
    result_text.value =f'Z = {Z}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №27"
    
    # Создаем текстовые поля для ввода p и y
    p_input = ft.TextField(label="Введите значение для переменной p", width=200)
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)
    
    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления Z
    calculate_button = ft.ElevatedButton(text="Вычислить Z", on_click=lambda e: calculate_g(p_input, y_input, result_text))

    # Добавляем элементы на страницу
    page.add(p_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)