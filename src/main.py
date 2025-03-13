import flet as ft


def main(page: ft.Page):
    page.add(
        ft.Row(controls=[
            ft.TextField(label='Email ou Usuário'),
            ft.TextField(label='senha',password=True, can_reveal_password=True),
            ft.ElevatedButton(text='Login')
        ])
    )
    


ft.app(main)
