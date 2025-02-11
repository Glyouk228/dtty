import flet as ft
import numpy as np

def calculate_g(t_input, e_input, y_input, l_input, result_text):
    # Получаем значения t и l и y и e из текстовых полей
    t = float(t_input.value)
    l = float(l_input.value)
    y = float(y_input.value)
    e = float(e_input.value)
    
    # Вычисляем K
    K = 2 * np.power(t, 2) + 3 * l +7.2 / np.log10(y) + np.power(e, 2 * l)

    # Обновляем текстовое поле с результатом 
    result_text.value =f'K = {K}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №20"
    
    # Создаем текстовые поля для ввода t и l и y и e
    t_input = ft.TextField(label="Введите значение для переменной t", width=200)
    l_input = ft.TextField(label="Введите значение для переменной l", width=200)
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)
    e_input = ft.TextField(label="Введите значение для переменной e", width=200)

    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления K
    calculate_button = ft.ElevatedButton(text="Вычислить K", on_click=lambda e: calculate_g(t_input, e_input, y_input , l_input, result_text))

    # Добавляем элементы на страницу
    page.add(t_input, y_input ,e_input, l_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)