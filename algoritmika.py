class Square():
    def area(self, x):
        S = x*x
        return S
figure = Square()
side_length = int(input("Введите длину стороны квадрата: "))
print(figure.area(side_length))