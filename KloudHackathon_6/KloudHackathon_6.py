import reflex as rx  # Reflexライブラリをインポート


def index() -> rx.Component:  # index関数を定義（ページのコンテンツを返す）
    return rx.vstack(  # 垂直方向に要素を配置するvstackコンポーネントを返す
        rx.color_mode.button(
            position="top-right"
        ),  # カラ―モード切り替えボタンを右上に配置
        rx.vstack(  # カード全体を囲むvstackを追加
            rx.card(  # カードコンポーネント（タイムカプセルのタイトル）
                rx.text(
                    "タイムカプセル", font_size="2em", color="white"
                ),  # テキスト「タイムカプセル」
                align_items="center",  # 要素を中央寄せ
                padding="3em 5em",  # パディング（上下3em、左右5em）
                margin_bottom="3em",  # 下マージン（3em）
                border_radius="20px",  # 角丸（20px）
                background_color="royalblue",  # 背景色（ロイヤルブルー）
            ),
            rx.card(  # カードコンポーネント（説明文）
                rx.text(  # テキスト（説明文）
                    "このサイトでは友人との思い出をタイムカプセルに保存し、忘れたころに友人と開けることで過去を懐かしむサイトです。",
                    font_size="1em",  # フォントサイズ（1em）
                    color="dimgray",  # 文字色（濃いグレー）
                ),
                padding="2em",  # パディング（2em）
                border_radius="10px",  # 角丸（10px）
                margin_y="2em",  # 上下マージン（2em）
                background_color="lightgray",  # 背景色（薄いグレー）
            ),
            rx.hstack(  # 水平方向に要素を配置するhstackコンポーネント
                rx.button(  # ボタンコンポーネント（制作する）
                    "制作する",
                    padding="2em 4em",  # パディング（上下2em、左右4em）
                    border_radius="8px",  # 角丸（8px）
                    background_color="limegreen",  # 背景色（ライムグリーン）
                    color="white",  # 文字色（白）
                ),
                rx.spacer(),  # ボタンの間隔を空ける
                rx.button(  # ボタンコンポーネント（閲覧する）
                    "閲覧する",
                    padding="2em 4em",  # パディング（上下2em、左右4em）
                    border_radius="8px",  # 角丸（8px）
                    background_color="orange",  # 背景色（オレンジ）
                    color="white",  # 文字色（白）
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
        ),
        align_items="center",  # 要素を中央寄せ
        justify_content="center",  # 要素を中央寄せ
        height="100vh",  # 高さ（100vh）
        background_color="lavender",  # 背景色（ラベンダー）
    )


app = rx.App()  # アプリケーションインスタンスを作成
app.add_page(index)  # index関数をページとして追加
