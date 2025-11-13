# Notes (Looping Structures (while and for))

A **loop** is used to complete the same, or a similar, task over and over until a particular condition is met. In Processing, we'll focus on two looping structures: `while` and `for`.

Loops are perfect for drawing repetitive patterns, like a picket fence, a grid of circles, or a staircase.

## While Loops

This looping structure will continue executing the code in its code block `{ }` **while** its condition remains `true`.

```processing
// 1. Initialize a variable
int x = 20;

// 2. Check the condition
while (x < 100) {
  // 3. Run the code
  rect(x, 50, 15, 30); // Draw a rectangle
  
  // 4. Change the variable (!!IMPORTANT!!)
  // If you forget this, you create an infinite loop!
  x = x + 20; 
}

// This code would draw 4 rectangles at x=20, x=40, x=60, and x=80.
// When x becomes 100, the condition (x < 100) is false, and the loop stops.
```

The structure of a `while` loop is very similar to an `if` statement. You can use any `boolean` expression to check whether the condition is `true` or `false`.

The `while` loop is best used when you are not sure exactly how many times you need to loop, for example, waiting for a variable to reach a certain value through a complex calculation, or running until the `mouseX` is in a certain position.

## For Loops

This looping structure is the most common and is used when you *know* how many times you want to loop (or can at least define it with a starting point, a condition, and an increment).

Instead of Python's `range()`, Processing uses a 3-part C-style `for` loop:

```processing
for (initialization; condition; increment) {
  // code to repeat...
}
```

This structure has three parts inside its parentheses, separated by semicolons:

  * **Initialization:** Runs *once* at the very beginning. Used to declare a counter variable (e.g., `int i = 0`).
  * **Condition:** Checked *before* every loop. If it's `true`, the loop runs. If it's `false`, the loop stops (e.g., `i < 10`).
  * **Increment:** Runs *after* every loop. Used to change the counter variable (e.g., `i++`, which means `i = i + 1`).

<!-- end list -->

```processing
// Count up (draw 5 circles)
// i starts at 0, runs as long as i < 5, and i increases by 1 each time
for (int i = 0; i < 5; i++) {
  float xPos = 20 + (i * 30);
  ellipse(xPos, 100, 25, 25);
  // This loop draws circles at x=20, 50, 80, 110, 140
}

// Count down (draw 5 rectangles)
// i starts at 5, runs as long as i > 0, and i decreases by 1
for (int i = 5; i > 0; i--) {
  float xPos = 20 + (i * 30);
  rect(xPos, 150, 25, 25);
  // This loop draws rectangles at x=170, 140, 110, 80, 50
}
```

## Loop Control

You can use two special keywords to control your loops:

  * `break`: Immediately exits the *current* loop and continues with the code after it.
  * `continue`: Skips the rest of the code *inside* the loop for the current iteration and jumps back to the top of the loop (to check the condition again).

<!-- end list -->

```processing
// Example of break
for (int i = 0; i < 100; i++) {
  float x = i * 10;
  
  if (x > width/2) {
    break; // Stop the loop when x gets to the middle of the screen
  }
  
  rect(x, 20, 5, 5);
}
```

-----

### Example Program 1: While Loops

```processing
/*-----------------------------------------------------------------------------
 Name:        While Loop Demo
 Purpose:     This sketch demonstrates how to use a while loop to draw 
              repetitive shapes.
 
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

  // Example 1: Drawing a row of blue rectangles
  // This loop will run as long as 'x' is less than 500.
  
  fill(0, 100, 200); // Blue
  stroke(0);
  strokeWeight(2);

  int x = 40; // 1. Initialize variable
  while (x < 550) { // 2. Check condition
    // 3. Run code
    println("Drawing rect at x: " + x);
    rect(x, 50, 20, 100);
    
    // 4. Increment variable (CRITICAL!)
    x = x + 40; 
  }


  // Example 2: Drawing a staircase of shrinking circles
  // This loop uses 'i' to control position AND size.
  
  fill(200, 0, 100); // Magenta
  noStroke();
  
  int i = 0;
  while (i < 15) {
    // 'i' controls x pos, y pos, and diameter
    float xPos = 50 + (i * 30);
    float yPos = 200 + (i * 10);
    float size = 40 - (i * 2); // Size shrinks
    
    ellipse(xPos, yPos, size, size);
    
    i = i + 1; // Increment
  }
}
```

-----

### Example Program 2: For Loops

```processing
/*-----------------------------------------------------------------------------
 Name:        For Loop Demo
 Purpose:     This sketch demonstrates using 'for' loops to draw patterns,
              including different increments and nested loops.
 
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
  
  // Example 1: Standard 'for' loop (i++)
  // Draws 10 red circles in a horizontal line.
  fill(200, 0, 0); // Red
  stroke(0);
  strokeWeight(2);
  
  // (init; condition; increment)
  for (int i = 0; i < 10; i++) {
    // 'i' will be 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    float xPos = 50 + (i * 50);
    ellipse(xPos, 70, 40, 40);
  }
  
  // Example 2: 'for' loop with custom step (i = i + 30)
  // Draws green rectangles with a gap.
  fill(0, 150, 50); // Green
  noStroke();
  
  for (int x = 20; x < width - 20; x = x + 30) {
    // 'x' will be 20, 50, 80, 110, 140...
    rect(x, 150, 20, 40);
  }
  
  // Example 3: Nested 'for' loops
  // An "outer" loop (for y) runs an "inner" loop (for x)
  // to create a 2D grid of points.
  
  stroke(0, 0, 255, 150); // Transparent blue
  strokeWeight(5);
  
  // Outer loop controls the Y position (rows)
  for (int y = 220; y < 380; y = y + 40) {
    
    // Inner loop controls the X position (columns)
    // This *entire* loop runs for *each* step of the 'y' loop
    for (int x = 40; x < 560; x = x + 40) {
      point(x, y); // Draw a point at (x, y)
    }
  }
}
```
