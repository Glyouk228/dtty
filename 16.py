import flet as ft
import numpy as np

def calculate_g(r_input, e_input, t_input, y_input, result_text):
    # Получаем значения r и t и e и y из текстовых полей
    r = float(r_input.value)
    t = float(t_input.value)
    e = float(e_input.value)
    y = float(y_input.value)
    
    # Вычисляем W
    W = 4 * np.power(t, 3) + np.log(r) / np.exp(e,y + r) + 7.2 * np.sin(r)
    
    # Обновляем текстовое поле с результатом 
    result_text.value =f'W = {W}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №16"
    
    # Создаем текстовые поля для ввода r и t и e и y
    r_input = ft.TextField(label="Введите значение для переменной r", width=200)
    t_input = ft.TextField(label="Введите значение для переменной t", width=200)
    e_input = ft.TextField(label="Введите значение для переменной e", width=200)
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)
    
    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления W
    calculate_button = ft.ElevatedButton(text="Вычислить W", on_click=lambda e: calculate_g(r_input, e_input, t_input,y_input, result_text))

    # Добавляем элементы на страницу
    page.add(r_input, e_input, t_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)