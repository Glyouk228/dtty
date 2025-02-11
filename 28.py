import flet as ft
import numpy as np

def calculate_g(v_input, e_input, y_input, result_text):
    # Получаем значения v и e из текстовых полей
    v = float(v_input.value)
    e = float(e_input.value)
    y = float(y_input.value)
    
    # Вычисляем W
    W = 0.004 * v + np.power(e ,2 * y) / np.power(e , y / 2)
    
    # Обновляем текстовое поле с результатом 
    result_text.value =f'W = {W}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №28"
    
    # Создаем текстовые поля для ввода v и e
    v_input = ft.TextField(label="Введите значение для переменной v", width=200)
    e_input = ft.TextField(label="Введите значение для переменной e", width=200)
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)
    
    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления W
    calculate_button = ft.ElevatedButton(text="Вычислить W", on_click=lambda e: calculate_g(v_input, y_input, e_input, result_text))

    # Добавляем элементы на страницу
    page.add(v_input, y_input, e_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)