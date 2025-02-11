import flet as ft
import numpy as np

def calculate_g(d_input, y_input, result_text):
    # Получаем значения d и y из текстовых полей
    d = float(d_input.value)
    y = float(y_input.value)
    
    # Вычисляем F
    F = np.log10(d) + 3.5 * np.power(d, 2) + 1  /  np.cos(2 * y)
    
    # Обновляем текстовое поле с результатом 
    result_text.value =f'F = {F}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №2"
    
    # Создаем текстовые поля для ввода d и y
    d_input = ft.TextField(label="Введите значение для переменной d", width=200)
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)
    
    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления F
    calculate_button = ft.ElevatedButton(text="Вычислить F", on_click=lambda e: calculate_g(d_input, y_input, result_text))

    # Добавляем элементы на страницу
    page.add(d_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)