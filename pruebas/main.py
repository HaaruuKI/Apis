import flet as ft

def main(page: ft.Page):
    text = ft.Text("HElLO WORLD")
    page.add(text)
    
ft.app(main,view=ft.WEB_BROWSER)