import reflex as rx


class TextState(rx.State):
    chat: str = ""
    name: str = ""
    mail: str = ""
