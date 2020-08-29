### Assignment

In this project you will use object oriented programming to create a Rectangle class and a Square class. The Square class should be a subclass of Rectangle and inherit methods and attributes.

#### Rectangle class
When a Rectangle object is created, it should be initialized with `width` and `height` attributes. The class should also contain the following methods:
* `set_width`
* `set_height`
* `get_area`: Returns area (`width * height`)
* `get_perimeter`: Returns perimeter (`2 * width + 2 * height`)
* `get_diagonal`: Returns diagonal (`(width ** 2 + height ** 2) ** .5`)

Additionally, if an instance of a Rectangle is represented as a string, it should look like: `Rectangle(width=5, height=10)`

#### Square class
The Square class should be a subclass of Rectangle. When a Square object is created, a single side length is passed in. The `__init__` method should store the side length in both the `width` and `height` attributes from the Rectangle class.

The Square class should be able to access the Rectangle class methods but should also contain a `set_side` method. If an instance of a Square is represented as a string, it should look like: `Square(side=9)`

#### Usage example
```py
rect = shape_calculator.Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
```
That code should return:
```
50
26
Rectangle(width=3, heigh=10)
81
5.656854249492381
Square(side=4)
```

The unit tests for this project are in `test_module.py`.

### Development

Write your code in `shape_calculator.py`. For development, you can use `main.py` to test your `shape_calculator()` function. Click the "run" button and `main.py` will run.

### Testing 

We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.

### Submitting

Copy your project's URL and submit it to freeCodeCamp.
