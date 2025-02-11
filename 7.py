import flet as ft
import numpy as np

def calculate_g(m_input, y_input, result_text):
    # Получаем значения m и y из текстовых полей
    m = float(m_input.value)
    y = float(y_input.value)
    
    # Вычисляем N
    N = np.power(m, 2) + 2.8 * m + 0.355 / np.cos(2 * y) + 3.6
    
    # Обновляем текстовое поле с результатом 
    result_text.value =f'N = {N}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №7"
    
    # Создаем текстовые поля для ввода m и y
    m_input = ft.TextField(label="Введите значение для переменной w", width=200)
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)
    
    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления N
    calculate_button = ft.ElevatedButton(text="Вычислить N", on_click=lambda e: calculate_g(m_input, y_input, result_text))

    # Добавляем элементы на страницу
    page.add(m_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)