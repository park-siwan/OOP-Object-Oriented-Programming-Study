class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_string(cls, string_params):
        parameter_list = string_params.split(",")
        name = parameter_list[0]
        email = parameter_list[1]
        password = parameter_list[2]
        return cls(name, email, password)

    @classmethod
    def from_list(cls, list_params):
        name = list_params[0]
        email = list_params[1]
        password = list_params[2]
        return cls(name, email, password)

# 유저 생성 및 초기값 설정
siwan = User.from_string("박시완,pswan3168@gmail.com,123456")
donghun = User.from_list(["김동훈", "donghun@gmail.com", "abcdef"])

print(siwan.name, siwan.email, siwan.password)
print(donghun.name, donghun.email, donghun.password)