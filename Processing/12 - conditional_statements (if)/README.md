# Notes (Conditional Statements)

**Conditional statements** (or `if` statements) allow your program to make decisions and run different code based on whether a condition is `true` or `false`.

In Processing, this lets you change what you draw based on user input (like `mouseX` or `keyPressed`) or other variables.

### The `if` Statement

An `if` statement checks a condition. If the condition is `true`, the code inside the **curly braces `{ }`** is executed. If the condition is `false`, the code block is skipped.

```processing
// In setup(), set size(400, 400);
background(240);

// Check if the mouse is on the left side of the screen
if (mouseX < 200) {
  // If true: draw a red circle
  fill(255, 0, 0);
  ellipse(100, 200, 80, 80);
}

// This code is outside the if-block, so it *always* runs
fill(100);
text("I am always here", 20, 20);
```

### Comparison Operators

To create a condition, you use comparison operators. The condition will always result in a `boolean` value (`true` or `false`).

  * `==` : Checks for equality (e.g., `x == 10`)
  * `>=` : Checks for greater than or equal to
  * `>` : Checks for greater than
  * `<=` : Checks for less than or equal to
  * `<` : Checks for less than
  * `!=` : Checks for **not** equal to

### `if-else`

You can use `else` to run a different block of code if the `if` condition is `false`.

```processing
// In setup(), set size(400, 400);

void draw() {
  // Check if the mouse is on the left side
  if (mouseX < 200) {
    // If true: draw a blue background
    background(0, 0, 255);
  } else {
    // If false (mouse is on the right): draw a red background
    background(255, 0, 0);
  }
}
```

### `else if`

You can chain multiple conditions together using `else if`. As soon as one condition is met, its code block runs and the rest of the chain is skipped.

```processing
// In draw()
background(240);

if (mouseY < 150) {
  // If mouse is in the top section, draw a circle
  fill(255, 0, 0);
  ellipse(width/2, 75, 100, 100);
} else if (mouseY < 300) {
  // Else if mouse is in the middle, draw a square
  fill(0, 255, 0);
  rect(width/2 - 50, 175, 100, 100);
} else {
  // Else (mouse must be in the bottom), draw a triangle
  fill(0, 0, 255);
  triangle(width/2, 320, width/2 - 50, 380, width/2 + 50, 380);
}
```

### Logical Operators (Chaining Conditions)

You can check multiple conditions at once using **logical operators**.

  * `&&` (AND): Both conditions must be `true`.
  * `||` (OR): At least one of the conditions must be `true`.

#### `&&` (AND) Example

```processing
// In draw()
background(240);
fill(100);
rect(100, 100, 200, 200); // A grey rectangle

// Check if mouseX is > 100 AND mouseX is < 300
// (i.e., is the mouse inside the rectangle's x-range?)
if (mouseX > 100 && mouseX < 300) {
  // If BOTH are true, draw a red ellipse
  fill(255, 0, 0);
  ellipse(width/2, height/2, 50, 50);
}
```

#### `||` (OR) Example

```processing
// In draw()
background(240);

// Check if the mouse is near the left edge OR a key is pressed
if (mouseX < 50 || keyPressed == true) {
  // If EITHER is true, draw a blue background
  background(0, 0, 255);
}
```

#### Grouping with Parentheses

Just like in math, you can use parentheses `( )` to group conditions. `&&` has priority over `||`, so grouping is important.

```processing
// In draw()
background(240);

// If (the mouse is in the top-left corner) OR (the 'm' key is pressed)
if ( (mouseX < 100 && mouseY < 100) || (key == 'm') ) {
  // Draw a big yellow circle
  fill(255, 255, 0);
  ellipse(width/2, height/2, 300, 300);
}
```

### Want Videos?
* http://learningprocessing.com/videos/5-0
* http://learningprocessing.com/videos/5-1
* http://learningprocessing.com/videos/5-2
* http://learningprocessing.com/videos/5-3
* http://learningprocessing.com/videos/5-4
