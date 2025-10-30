# Notes (Basics)

### Printing strings

When printing strings, you primarily use **double-quotes (`"`)**. Processing uses `print()` to output text to the console and `println()` to output text followed by a new line.

Single-quotes (`'`) are reserved for single **characters** (e.g., `'a'`), not strings.

If you need to include a double-quote within your string, you must "escape" it using a backslash (`\`).

```processing
// println() adds a new line after printing
println("Hello world!");

// print() does not add a new line
print("Hello");
print(" world!");
// This will appear as "Hello world!" on one line

// To print a quote, use \
println("Mr. Seidel said, \"Who's there?\"");
```

### Printing numerical values

When printing numerical values mixed with text, you use **string concatenation** with the `+` operator. Processing will automatically convert the numerical value to a string.

```processing
println(5 + 10); // example 1: Prints 15
println("The result of 5*6 is: " + (5*6)); // example 2
```

### Variables and printing

Variables are used to temporarily store information. In Processing, you must **declare the type** of data a variable will hold *before* you use it.

Variables should be named so that it is easy to tell what the value held by the variable is easily identifiable.

Common variable types include:

  * `int` - Numbers with no decimal component (e.g., `10`, `-5`)
  * `float` - Numbers WITH a decimal part (e.g., `3.14`, `2.0`)
  * `char` - A single key on your keyboard (e.g., `'A'`, `'?'`)
  * `String` - A bunch of characters linked together (e.g., `"Hello"`)
  * `boolean` - `true` or `false` values\!
  * and more\!

#### Printing Variables

```processing
int integerOne = 15;
int integerTwo = 22;
// Use + to combine strings and variables
println("The difference is: " + (integerOne - integerTwo));

String name = "Mr. Brooks";
println("Hello " + name + ", how are you today?");
```

### Mathematical Operations

You can use the standard mathematical operators `+`, `-`, `*`, `/` as well as some other ones:

  * `/` - This is used for **integer division** *if* both numbers are integers.
  * `%` - This is used to find the **remainder** after a division (modulo).
  * `pow()` - This is a **function** used for powers.

<!-- end list -->

```processing
// Integer division: 5 / 2 is 2, not 2.5
int integerDivision = 5 / 2;
println(integerDivision); // Should be 2

// To get a float result, one number must be a float
float floatDivision = 5.0 / 2;
println(floatDivision); // Should be 2.5

int moduloOfIntegers = 5 % 2;
println(moduloOfIntegers);  // Should be 1

// pow(base, exponent)
float powerOfNumbers = pow(2, 3);
println(powerOfNumbers);   // Should be 8.0
```

### Converting between types

You can convert between different data types (this is often called "casting") by using functions such as:

  * `int()` - Will convert to an integer (truncates decimals)
  * `float()` - Will convert to a float value
  * `str()` - Will convert to a string
  * and more\!

<!-- end list -->

```processing
// int() cuts off the decimal, it does not round
int integerConversion = int(5.9);
println(str(integerConversion)); // Prints "5"

float floatConversion = float(2);
println(str(floatConversion)); // Prints "2.0"
```

### Built-in Variables

Processing provides several "built-in" variables that are very useful for creating interactive sketches. You don't need to declare them; you can just use them.

* `width`: The width of your sketch window (in pixels), set by `size()`.
* `height`: The height of your sketch window (in pixels), set by `size()`.
* `mouseX`: The current `int` x-coordinate (horizontal position) of the mouse.
* `mouseY`: The current `int` y-coordinate (vertical position) of the mouse.
* `pmouseX`: The `int` x-coordinate of the mouse in the *previous* frame.
* `pmouseY`: The `int` y-coordinate of the mouse in the *previous* frame.
* `mousePressed`: A `boolean` variable that is `true` if any mouse button is currently pressed, and `false` otherwise.
* `key`: A `char` variable that holds the value of the most recent key that was pressed.
* `keyPressed`: A `boolean` variable that is `true` if any key is currently pressed, and `false` otherwise.
* `frameCount`: An `int` variable that counts the number of frames displayed since the sketch started.
