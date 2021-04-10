class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_string(cls, string_params):

    @classmethod
    def from_list(cls, list_params):


# 코드를 쓰세요

# 유저 생성 및 초기값 설정
siwan = User.from_string("박시완,pswan3168@gmail.com,123456")
donghun = User.from_list(["김동훈", "donghun@gmail.com", "abcdef"])

print(siwan.name, siwan.email, siwan.password)
print(donghun.name, donghun.email, donghun.password)