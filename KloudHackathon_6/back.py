import reflex as rx

import KloudHackathon_6.state as state
from KloudHackathon_6 import style


def go_to_production_page():  # 制作ページへ移動するための関数
    return rx.redirect("/production_page")


def go_to_info_page():  # 情報登録ページへ移動するための関数
    return rx.redirect("/info_page")


def index() -> rx.Component:
    return rx.vstack(
        rx.box(
            "タイムカプセル",
            align_items="center",  # 要素を中央寄せ
            padding="3em 5em",  # パディング（上下3em、左右5em）
            margin_bottom="3em",  # 下マージン（3em）
            border_radius="20px",  # 角丸（20px）
        ),
        rx.box(  # カードコンポーネント（説明文）
            "このサイトでは友人との思い出をタイムカプセルに保存し、忘れたころに友人と開けることで過去を懐かしむサイトです。",
        ),
        rx.hstack(  # 水平方向に要素を配置するhstackコンポーネント
            rx.button(  # ボタンコンポーネント（制作する）
                "制作する",
                align_items="center",
                padding="2em 4em",  # パディング（上下2em、左右4em）
                border_radius="8px",  # 角丸（8px）
                background_color="limegreen",  # 背景色（ライムグリーン）
                on_click=go_to_production_page,  # 制作ページへ移動
            ),
            justify="center",  # 要素を中央寄せ
            width="50%",  # 幅（50%）
        ),
        align_items="center",  # カード内の要素を中央寄せ
        justify_content="center",  # カード内の要素を中央寄せ
        width="70%",  # カードの幅（70%）
        height="50%",  # カードの高さ（50%）
        max_width="1200px",  # カードの最大幅（1200px）
        padding="3em",  # カード全体のパディング（3em）
        border_radius="15px",  # カード全体の角丸（15px）
        background_color="white",  # カード全体の背景色（白）
        box_shadow="0 4px 8px rgba(0, 0, 0, 0.1)",  # カードに影を追加
    )


def production_page() -> rx.Component:
    return rx.vstack(  # 垂直方向に要素を配置するvstackコンポーネントを返す
        rx.color_mode.button(
            position="top-right"
        ),  # カラ―モード切り替えボタンを右上に配置
        rx.card(  # カードコンポーネント（制作ページのタイトル）
            rx.text("制作ページ", font_size="2em", color="white"),
            align_items="flex-start",  # 要素を上部に固定
            padding="3em 5em",  # パディング（上下3em、左右5em）
            margin_bottom="3em",  # 下マージン（3em）
            border_radius="20px",  # 角丸（20px）
            background_color="royalblue",  # 背景色（ロイヤルブルー）
            width="300px",
            height="50px",
        ),
        rx.hstack(  # カード全体を囲むvstackを追加
            rx.card(  # カードコンポーネント（説明文）
                rx.input(  # 【注意】このインプットは複数選択及び送信がまだ出来ていません。
                    type="file",  # ファイルを受け取るinput
                    placeholder="ファイルを投げる場所",
                    id="file_input",
                ),
                width="450px",  # カードの幅(450px)
                height="500px",  # カードの高さ(500px)
                padding="2em",  # パディング（2em）
                border_radius="10px",  # 角丸（10px）
                margin_y="2em",  # 上下マージン（2em）
                background_color="lightgray",  # 背景色（薄いグレー）
            ),
            rx.card(  # カードコンポーネント（説明文）
                rx.text(f"ログ: {state.TextState.chat}"),  # 入力されたテキストを表示
                # ログとして機能していない
                width="450px",  # カードの幅(450px)
                height="500px",  # カードの高さ(500px)
                padding="2em",  # パディング（2em）
                border_radius="10px",  # 角丸（10px）
                margin_y="2em",  # 上下マージン（2em）
                background_color="lightgray",  # 背景色（薄いグレー）
            ),
        ),
        rx.hstack(
            rx.input(
                type="text",  # テキストを受け取るinput
                placeholder="テキストを入力",
                id="chat_input",
                width="300px",  # 入力ウィンドウの幅
                on_change=state.TextState.set_chat,
            ),
            rx.button(
                rx.text("->"),  # このボタンを押したら入力内容を保存してログに入れたい
            ),
        ),
        rx.vstack(  # ココに通知する日時など...
            rx.card(
                width="750px",
                height="550px",
            ),
            margin_y="5em",
        ),
        rx.button(  # ボタンコンポーネント（制作する）
            "制作終了",
            align_items="center",
            padding="2em 4em",  # パディング（上下2em、左右4em）
            border_radius="8px",  # 角丸（8px）
            background_color="limegreen",  # 背景色（ライムグリーン）
            color="white",  # 文字色（白）
            on_click=go_to_info_page,  # 制作ページへ移動
        ),
        align_items="center",  # 要素を中央寄せ
        justify_content="center",  # 要素を中央寄せ
        height="160vh",  # 高さ（160vh）
        background_color="lavender",  # 背景色（ラベンダー）
    )


def info_page() -> rx.Component:
    return rx.vstack(
        rx.color_mode.button(position="top-right"),
        rx.card(  # カードコンポーネント（情報登録ページのタイトル）
            rx.text("情報登録ページ", font_size="2em", color="white"),
            align_items="flex-start",  # 要素を上部に固定
            padding="3em 5em",  # パディング（上下3em、左右5em）
            margin_bottom="3em",  # 下マージン（3em）
            border_radius="20px",  # 角丸（20px）
            background_color="royalblue",  # 背景色（ロイヤルブルー）
            width="300px",
            height="50px",
        ),
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
        background_color="lavender",  # 背景色（ラベンダー）
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


app = rx.App()  # アプリケーションインスタンスを作成
app.add_page(index, route="/")  # index関数をページとして追加
app.add_page(production_page, route="/production_page")
app.add_page(info_page, route="/info_page")
app.add_page(view_page, route="/view_page")
app.add_page(chat_page, route="/chat_page")  # 試験実装
