# Notes (Functions)

Functions are used to encapsulate and organize reusable code that performs a single, specific action. You have been using functions constantly: `setup()`, `draw()`, `rect()`, `fill()`, and `ellipse()` are all functions.

Creating your own functions allows you to avoid repeating code and makes your sketches much more organized.

### Function Structure

The basic structure of a function in Processing is:

```processing
/*
 * Description of what the function does
 */
returnType functionName(type1 param1, type2 param2, ...) {

  
  // body of the function
  
  return expression; // This line is used only if returnType is not 'void'
}
```

This breaks down as follows:

  * **`returnType`**: This is the type of data the function will "give back" or *return*. If the function just *does* something (like draw a shape) and doesn't return a value, you use the special type **`void`**. Other common types are `int`, `float`, `boolean`, or `color`.
  * **`functionName`**: The name of the function. It should be clear and describe its purpose (e.g., `drawCircle`, `calculateDistance`).
  * **`(type1 param1, ...)`**: These are the **parameters** (inputs) the function accepts. You *must* declare a type for every parameter. If the function takes no parameters, you just use empty parentheses: `()`.
  * **`{ ... }` (Body)**: The code that the function will execute. This is defined by curly braces, *not* indentation.
  * **`return`**: This keyword sends a value back from the function. The type of the value you `return` *must* match the `returnType` you declared. If your function is `void`, you don't need a `return` statement.

### Placement

Functions must be defined (written) *outside* of `setup()` and `draw()`. You can place your custom functions anywhere else in your sketch file (typically at the bottom). You can then **call** your function from inside `setup()` or `draw()`.

### Local Variables

A variable declared *inside* a function (like `float cSquare` in the example below) is a **local variable**. It only exists and is only usable *inside* that function. This is the same as in Python.

-----

### Example 1: `void` function (No Return Value)

This is like the Python `menu()` example. It performs an action (drawing) but doesn't give a value back. This function is useful for drawing a complex, reusable shape.

```processing
// In setup():
// size(600, 400);

// In draw():
// background(240);
// drawRobot(100, 150, color(255, 0, 0)); // Call the function
// drawRobot(300, 100, color(0, 0, 255)); // Call it again!

/*
 * Draws a simple robot at a specific (x, y) location and with a
 * specific color. This function is 'void' because it doesn't 
 * return any value; it just draws.
 */
void drawRobot(int x, int y, color bodyColor) {
  // Body
  fill(bodyColor);
  stroke(0);
  strokeWeight(2);
  rect(x - 50, y, 100, 100);

  // Head
  fill(200);
  rect(x - 30, y - 60, 60, 60);
  
  // Eyes
  fill(0);
  ellipse(x - 15, y - 30, 10, 10);
  ellipse(x + 15, y - 30, 10, 10);
}
```

-----

### Example 2: Function with a Return Value

This is like the Python `hypotenuse()` example. It takes data in, performs a calculation, and **returns** the result, which you can then store in a variable or use to draw shapes.

```processing
// In setup():
// size(400, 400);

// In draw():
// background(255);
// float sideA = 100;
// float sideB = 150;
//
// // Call the function and store the result in a new variable 'hyp'
// float hyp = calculateHypotenuse(sideA, sideB);
//
// // Now use that returned value to draw something!
// fill(255, 0, 0, 100); // Transparent red
// ellipse(200, 200, hyp, hyp); // The diameter is the hypotenuse

/*
 * Calculates the hypotenuse and returns it as a float.
 * Uses the Pythagorean theorem: a^2 + b^2 = c^2
 */
float calculateHypotenuse(float sideA, float sideB) {
  // 'cSquare' is a local variable
  float cSquare = (sideA * sideA) + (sideB * sideB);
  
  // Processing's function for square root is sqrt()
  float hypotenuseValue = sqrt(cSquare); 
  
  return hypotenuseValue; // Send the final value back
}
```

-----

Here are two complete, runnable example programs to demonstrate these concepts.

### Example Program 1: `void` (No Return) Function

```processing
/*-----------------------------------------------------------------------------
 Name:        FunctionVoidExample
 Purpose:     Demonstrates 'void' functions (no return value) by creating
              a reusable function to draw a complex shape.
 
 Author:      C. Brooks-Prenger
 Created:     02-Nov-2025
 Updated:     02-Nov-2025
-----------------------------------------------------------------------------*/

void setup() {
  size(600, 400);
  background(240);
  noLoop(); // Run draw() only once
}

void draw() {
  // Call our custom function multiple times.
  // This is much cleaner than repeating all the rect/ellipse calls.
  drawRobot(150, 200, color(0, 150, 200));  // Blue robot
  drawRobot(300, 250, color(200, 100, 0)); // Orange robot
  drawRobot(450, 200, color(150, 0, 200)); // Purple robot
}

/*
 * --- Our Custom Function ---
 * Draws a simple robot at a specific (x, y) location and with a
 * specific color. This function is 'void' because it doesn't 
 * return any value; it just draws.
 */
void drawRobot(int x, int y, color bodyColor) {
  // Body
  fill(bodyColor);
  stroke(0);
  strokeWeight(2);
  rectMode(CENTER);
  rect(x, y, 80, 100);

  // Head
  fill(200);
  rect(x, y - 70, 50, 50);
  
  // Eyes
  fill(0);
  ellipse(x - 10, y - 70, 8, 8);
  ellipse(x + 10, y - 70, 8, 8);
  
  // Legs
  strokeWeight(4);
  line(x - 20, y + 50, x - 20, y + 100);
  line(x + 20, y + 50, x + 20, y + 100);
}
```

### Example Program 2: `return` Value Function

```processing
/*-----------------------------------------------------------------------------
 Name:        FunctionReturnExample
 Purpose:     Demonstrates a function that takes parameters, performs
              a calculation, and returns a 'float' value.
 
 Author:      C. Brooks-Prenger
 Created:     02-Nov-2025
 Updated:     02-Nov-2025
-----------------------------------------------------------------------------*/

void setup() {
  size(600, 400);
  background(255);
  noLoop(); // Run draw() only once
}

void draw() {
  // Define the two sides of a triangle
  float sideA = 100;
  float sideB = 200;
  
  // 1. Call our custom function to get the hypotenuse
  float hypotenuse = calculateHypotenuse(sideA, sideB);
  
  // 2. Use the returned value to draw shapes
  
  // Draw the original triangle for context
  stroke(0);
  strokeWeight(4);
  fill(0, 0, 255, 50); // Transparent blue
  triangle(50, 350, 50 + sideA, 350, 50, 350 - sideB);

  // Draw a red line representing the hypotenuse
  stroke(255, 0, 0);
  strokeWeight(6);
  line(50, 350 - sideB, 50 + sideA, 350);
  
  // Draw a circle whose diameter is the length of the hypotenuse
  fill(255, 0, 0, 100); // Transparent red
  noStroke();
  ellipse(400, 200, hypotenuse, hypotenuse);
  
  // Draw text showing the calculated value
  fill(0);
  textSize(16);
  text("Side A: " + sideA, 350, 300);
  text("Side B: " + sideB, 350, 320);
  text("Hypotenuse: " + hypotenuse, 350, 340);
}

/*
 * --- Our Custom Function ---
 * Calculates the hypotenuse and returns it as a float.
 * Uses the Pythagorean theorem: a^2 + b^2 = c^2
 */
float calculateHypotenuse(float sideA, float sideB) {
  // 'cSquare' is a local variable
  float cSquare = (sideA * sideA) + (sideB * sideB);
  
  // Processing's function for square root is sqrt()
  float hypotenuseValue = sqrt(cSquare); 
  
  // Send the final value back to wherever the function was called
  return hypotenuseValue; 
}
```
