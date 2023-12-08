import flet as ft
import json
from steam import Steam
from decouple import config

KEY = config("STEAM_API_KEY")

steam = Steam(KEY)

user = steam.apps.search_games("indie")


def main(page: ft.Page):
    page.title = "OASIS VIRTUAL"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50
    page.update()

    images = ft.Row(expand=0, wrap=False, scroll="always")

    for game in user["apps"]:
        name = game["name"]
        price = game["price"]
        imgs = game["img"]
        image = ft.Image(
                src=imgs,
                width=200,
                height=200,
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
        )
        column = ft.Column(expand=0, alignment="center")
        column.controls.append(image)
        column.controls.append(ft.Text(f"{name}"))
        column.controls.append(ft.Text(f"{price}"))
        images.controls.append(column)

    page.add(images)
    page.update()

ft.app(target=main,view=ft.WEB_BROWSER)
