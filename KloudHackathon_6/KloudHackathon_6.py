from turtle import width

import reflex as rx

import KloudHackathon_6.state as state


def header(title: str) -> rx.Component:
    return rx.flex(
        rx.button(
            "ホーム",
            on_click=rx.redirect("/"),
            margin="1em",
        ),
        rx.box(
            title,
            font_size="2em",
            width="100%",
            text_align="center",
        ),
        align="center",
        justify="center",
        width="100%",
        min_height="60px",
    )


def index() -> rx.Component:
    return rx.vstack(
        header("ようこそ"),
        rx.flex(
            rx.card(
                "かぷせるもーめんと",
                font_size="2em",
                align_items="center",  # 要素を中央寄せ
                padding="3em 5em",  # パディング（上下3em、左右5em）
                margin_bottom="2em",  # 下マージン（3em）
            ),
            rx.card(  # カードコンポーネント（説明文）
                "このサイトでは友人との思い出をタイムカプセルに保存し、忘れたころに友人と開けることで過去を懐かしむサイトです。",
            ),
            rx.hstack(  # 水平方向に要素を配置するhstackコンポーネント
                rx.button(  # ボタンコンポーネント（制作する）
                    "制作する",
                    padding="2em 4em",  # パディング（上下2em、左右4em）
                    on_click=rx.redirect("/production"),  # 制作ページへ移動
                ),
                justify="center",
                width="70%",
            ),
            direction="column",
            align="center",
            justify="center",
            spacing="4",
            width="70%",
            height="100%",
        ),
        align="center",
        width="100vw",
        height="100vh",
    )


def production_page() -> rx.Component:
    return rx.vstack(
        header("制作ページ"),
        rx.flex(
            rx.vstack(  # カード全体を囲むvstackを追加
                rx.card(  # カードコンポーネント（説明文）
                    rx.input(  # 【注意】このインプットは複数選択及び送信がまだ出来ていません。
                        type="file",  # ファイルを受け取るinput
                        placeholder="ファイルを投げる場所",
                        id="file_input",
                    ),
                    width="100%",
                    height="80%",
                ),
                width="50%",  # カードの幅(450px)
                height="100%",  # カードの高さ(500px)
            ),
            rx.vstack(
                rx.card(  # カードコンポーネント（説明文）
                    rx.text(f"ログ: {state.TextState.chat}"),
                    width="100%",
                    height="80%",
                ),
                rx.hstack(
                    rx.input(
                        type="text",  # テキストを受け取るinput
                        placeholder="テキストを入力",
                        id="chat_input",
                        # width="300px",  # 入力ウィンドウの幅
                        on_change=state.TextState.set_chat,
                    ),
                    rx.button("->"),
                    height="20%",
                ),
                width="50%",
                height="100%",
            ),
            direction="row",
            align="center",
            justify="center",
            width="80%",
            height="80%",
        ),
        rx.button(
            "制作終了",
            on_click=rx.redirect("/info"),  # 制作ページへ移動
        ),
        align="center",
        width="100vw",
        height="100vh",
    )


def info_page() -> rx.Component:
    return rx.vstack(
        header("情報登録ページ"),
        rx.card(
            rx.hstack(
                rx.input(
                    placeholder="名前を入力してください",
                    id="name_input",
                    width="300px",
                    on_change=state.TextState.set_name,
                ),
                rx.input(
                    type="email",
                    placeholder="メールアドレスを入力してください",
                    id="email_input",
                    width="300px",
                    on_change=state.TextState.set_mail,
                ),
            ),
            width="900px",
            height="800px",
        ),
        align_items="center",  # 要素を中央寄せ
        justify_content="center",  # 要素を中央寄せ
        height="100vh",  # 高さ（100vh）
    )


def view_page() -> rx.Component:
    return rx.vstack(
        rx.color_mode.button(position="top-right"),
        rx.card(  # カードコンポーネント（閲覧ページのタイトル）
            rx.text("閲覧ページ", font_size="2em", color="white"),
            align_items="flex-start",  # 要素を上部に固定
            padding="3em 5em",  # パディング（上下3em、左右5em）
            margin_bottom="3em",  # 下マージン（3em）
            border_radius="20px",  # 角丸（20px）
            background_color="royalblue",  # 背景色（ロイヤルブルー）
            width="300px",
            height="50px",
        ),
        rx.hstack(
            rx.card(
                rx.text("一覧表示"),
                width="450px",  # カードの幅(450px)
                height="500px",  # カードの高さ(500px)
                padding="2em",  # パディング（2em）
                border_radius="10px",  # 角丸（10px）
                margin_y="2em",  # 上下マージン（2em）
                background_color="lightgray",  # 背景色（薄いグレー）
            ),
            rx.card(
                rx.text("詳細表示"),
                width="450px",  # カードの幅(450px)
                height="500px",  # カードの高さ(500px)
                padding="2em",  # パディング（2em）
                border_radius="10px",  # 角丸（10px）
                margin_y="2em",  # 上下マージン（2em）
                background_color="lightgray",  # 背景色（薄いグレー）
            ),
        ),
        align_items="center",  # 要素を中央寄せ
        justify_content="center",  # 要素を中央寄せ
        height="100vh",  # 高さ（100vh）
        background_color="lavender",  # 背景色（ラベンダー）
    )


def chat_page() -> rx.Component:
    return rx.vstack(
        rx.text("名前を入力してください"),
        rx.input(
            placeholder="名前",
            id="name_input",
            width="300px",
            on_change=state.TextState.set_chat,
        ),
        rx.text(f"あなたが入力した名前: {state.TextState.chat}"),
    )


app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
        accent_color="teal",
        box_border="1em",
    )
)
app.add_page(index, route="/")  # index関数をページとして追加
app.add_page(production_page, route="/production")
app.add_page(info_page, route="/info")
app.add_page(view_page, route="/view")
app.add_page(chat_page, route="/chat")  # 試験実装
