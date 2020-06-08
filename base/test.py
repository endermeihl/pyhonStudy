import module3
import fib
import Person
import Triangle

# module3.foo()
# fib.main()
Person.main()

a = int(input('a'))
b = int(input('b'))
c = int(input('c'))
if Triangle.is_valid(a, b, c):
    t = Triangle(a, b, c)
    print(t.perimeter())
    # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
    # print(Triangle.perimeter(t))
    print(t.area())
    # print(Triangle.area(t))
else:
    print('无法构成三角形.')
