class User:
    def __init__(self, name):
        if not (4 <= len(name) <= 20):
            raise ValueError(f"{name}はルール違反です")
        self.name = name

    def screen_name(self):
        return self.name.upper()

    def self_introduction(self):
        return f"私の名前は{self.name.upper()}です"


# UserNameクラスのインスタンス化
tanaka = User(name="tanaka")

# クラスの値の出力
print(tanaka.screen_name())
print(tanaka.self_introduction())
