# Notes (Framework & 2D Shapes)

### The Processing Framework (`setup()` & `draw()`)

Every standard Processing sketch is built around two main functions: `setup()` and `draw()`.

1.  **`void setup() { ... }`**

      * This function runs **once** at the very beginning when your program starts.
      * It's used for initialization tasks, like setting the window size, loading images, setting a background color that won't change, or setting global properties like text alignment.
      * The most important function to call here is `size(width, height)` to create your sketch window.

2.  **`void draw() { ... }`**

      * This function runs **continuously** in a loop (by default, 60 times per second).
      * This is where all the active drawing, animation, and interaction logic goes.
      * The `draw()` loop is what creates the illusion of motion. Each time `draw()` runs, it draws a new "frame."

<!-- end list -->

```processing
void setup() {
  // Runs once: Set the window size to 600x400
  size(600, 400);
}

void draw() {
  // Runs 60 times per second:
  
  // 1. Redraw the background to clear the previous frame
  background(220); // Light grey
  
  // 2. Draw an ellipse at the mouse's current (x, y) position
  ellipse(mouseX, mouseY, 50, 50);
}
```

-----

### Drawing Properties (Color & Style)

Before you draw a shape, you can set its properties, like its fill color, outline color, and outline thickness. These properties will apply to all shapes drawn *after* them, until you change them again.

  * `background(r, g, b)`: Sets the background color of the sketch. `(0, 0, 0)` is black, `(255, 255, 255)` is white. You can also use a single value for grayscale: `background(100)`.
  * `fill(r, g, b)`: Sets the **fill** (interior) color for shapes.
  * `noFill()`: Disables the fill for shapes (makes them transparent).
  * `stroke(r, g, b)`: Sets the **stroke** (outline) color for shapes.
  * `noStroke()`: Disables the outline for shapes.
  * `strokeWeight(pixels)`: Sets the thickness of the stroke in pixels.

<!-- end list -->

```processing
void setup() {
  size(400, 400);
}

void draw() {
  background(255); // White background

  // Example 1: Red circle with a thick black outline
  stroke(0, 0, 0);   // Black stroke
  strokeWeight(5); // 5 pixel thick outline
  fill(255, 0, 0);   // Red fill
  ellipse(100, 100, 80, 80);

  // Example 2: Blue square with no outline
  noStroke();        // Turn off the outline
  fill(0, 0, 255);   // Blue fill
  rect(200, 60, 80, 80); // rect(x, y, width, height)
  
  // Example 3: Green line (lines don't have a fill)
  stroke(0, 255, 0); // Green stroke
  strokeWeight(10);
  line(50, 200, 350, 300); // line(x1, y1, x2, y2)
}
```

-----

### 2D Primitive Shapes

Processing gives you simple functions to draw basic geometric shapes. The coordinates `(0, 0)` are at the **top-left** corner of the window.

  * `point(x, y)`: Draws a single pixel.
  * `line(x1, y1, x2, y2)`: Draws a line from point `(x1, y1)` to `(x2, y2)`.
  * `rect(x, y, w, h)`: Draws a rectangle. By default, `(x, y)` is the top-left corner, and `w` and `h` are its width and height.
  * `ellipse(x, y, w, h)`: Draws an ellipse (or circle). By default, `(x, y)` is the **center** of the ellipse, and `w` and `h` are its width and height.
  * `triangle(x1, y1, x2, y2, x3, y3)`: Draws a triangle by connecting the three coordinate points.
  * `quad(x1, y1, x2, y2, x3, y3, x4, y4)`: Draws any four-sided shape by connecting the four coordinate points.

<!-- end list -->

```processing
void setup() {
  size(500, 500);
  noLoop(); // Stop draw() from looping, just run it once
}

void draw() {
  background(240);
  strokeWeight(2);
  
  // A point (can be hard to see!)
  strokeWeight(5);
  stroke(0);
  point(50, 50);
  strokeWeight(2); // Reset

  // A line
  stroke(255, 0, 0); // Red
  line(20, 80, 180, 100);

  // A rectangle
  fill(0, 255, 0); // Green
  stroke(0);
  rect(40, 150, 100, 60); // (x, y, width, height)

  // An ellipse (circle)
  fill(0, 0, 255); // Blue
  ellipse(300, 200, 100, 100); // (x, y, width, height)

  // A triangle
  noFill(); // No fill, just outline
  stroke(255, 0, 255); // Magenta
  triangle(300, 300, 450, 320, 350, 450);
}
```

### 📖 Shape Reference

This is just a small sample of the available shapes. For a complete list, including `arc`, `curve`, and 3D shapes, always check the official Processing reference.

**[https://processing.org/reference/\#shape](https://processing.org/reference/#shape)**
