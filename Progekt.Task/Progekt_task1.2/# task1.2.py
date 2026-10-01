# task1.2
import mymodule
from mymodule import circle_area, VERSION
from mymodule import circle_len as perimeter
import mymodule as mm

print('1) mymodule.circle_area(5) =', mymodule.circle_area(5))
print('2) circle_area(5)          =', circle_area(5))
print('3) perimeter(5)            =', mm.PI)

print('dir(mymodole) ->', [n for n in dir(mymodule) if not n.startswith('__')])
print('mymodule.__name__ =', mymodule.__name__)
print('mymodule.__file__ =', mymodule.__file__)

print('mm._helper() =', mm._helper())
 # это работает потому что есть одно нижнее подчеркивание это говорит о том, что функция преднозначена для внутреннего использования
