import reflex as rx


def index() -> rx.Component:
    return rx.vstack(
        rx.color_mode.button(position="top-right"),
        rx.vstack(  # カード全体を囲むvstackを追加
            rx.card(
                rx.text("タイムカプセル", font_size="2em", color="white"),
                align_items="center",
                padding="3em 5em",
                margin_bottom="3em",
                border_radius="20px",
                background_color="royalblue",
            ),
            rx.card(
                rx.text(
                    "このサイトでは友人との思い出をタイムカプセルに保存し、忘れたころに友人と開けることで過去を懐かしむサイトです。",
                    font_size="1em",
                    color="dimgray",
                ),
                padding="2em",
                border_radius="10px",
                margin_y="2em",
                background_color="lightgray",
            ),
            rx.hstack(
                rx.button(
                    "制作する",
                    padding="2em 4em",
                    border_radius="8px",
                    background_color="limegreen",
                    color="white",
                ),
                rx.spacer(),
                rx.button(
                    "閲覧する",
                    padding="2em 4em",
                    border_radius="8px",
                    background_color="orange",
                    color="white",
                ),
                justify="center",
                width="50%",
            ),
            align_items="center",  # カード内の要素を中央寄せ
            justify_content="center",  # カード内の要素を中央寄せ
            width="70%",  # カードの幅を調整
            height="50%",  # カードの高さを調整
            max_width="1200px",  # カードの最大幅を調整
            padding="3em",  # カード全体のpaddingを調整
            border_radius="15px",  # カード全体の角丸を調整
            background_color="white",  # カード全体の背景色を白に設定
            box_shadow="0 4px 8px rgba(0, 0, 0, 0.1)",  # カードに影を追加
        ),
        align_items="center",
        justify_content="center",
        height="100vh",
        background_color="lavender",
    )


app = rx.App()
app.add_page(index)
app.add_page(index)
