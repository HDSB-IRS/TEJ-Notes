/*-----------------------------------------------------------------------------
 Name:        Framework and 2D Shapes
 Purpose:     This sketch demonstrates the setup() and draw() framework, drawing properties (fill, stroke), and 2D primitive shapes.

 Author:      C. Brooks-Prenger
 Created:     30-Oct-2025
 Updated:     30-Oct-2025 
-----------------------------------------------------------------------------*/


/*
 * Example: Framework and 2D Shapes
 *
 * This sketch demonstrates the setup() and draw() framework,
 * drawing properties (fill, stroke), and 2D primitive shapes.
 */

// setup() runs one time at the very start.
void setup() {
  // Set the window size to 600 pixels wide by 400 pixels tall
  size(600, 400);
  
  // Set the background color once
  background(240); // Light grey
  
  // Print a message to the console
  println("Drawing 2D primitive shapes.");
  
  // By default, draw() loops. We'll add noLoop() 
  // so it only runs once, making a static image.
  // Remove the line below to see shapes drawn at the mouse position!
  noLoop(); 
}

// draw() runs in a loop (unless noLoop() is used).
void draw() {
  
  // --- Style 1: Red ellipse with black outline ---
  fill(200, 0, 0);    // Set fill color to Red
  stroke(0);        // Set stroke color to Black
  strokeWeight(4);  // Set outline thickness to 4 pixels
  
  // ellipse(x, y, width, height)
  // (x, y) is the CENTER of the ellipse
  ellipse(100, 100, 150, 100);

  // --- Style 2: Blue rectangle with no outline ---
  noStroke();         // Disable the outline
  fill(0, 100, 200);  // Set fill color to Blue
  
  // rect(x, y, width, height)
  // (x, y) is the TOP-LEFT corner of the rectangle
  rect(250, 50, 120, 100);

  // --- Style 3: Green triangle with thick outline, no fill ---
  noFill();           // Disable the fill
  stroke(0, 150, 50); // Set stroke color to Green
  strokeWeight(8);
  
  // triangle(x1, y1, x2, y2, x3, y3)
  // Connects the three (x, y) points
  triangle(450, 150, 550, 80, 500, 200);

  // --- Style 4: A thick orange line ---
  // (Lines don't use fill)
  stroke(255, 150, 0); // Orange
  strokeWeight(10);
  
  // line(x1, y1, x2, y2)
  line(50, 250, 250, 350);

  // --- Style 5: A magenta quadrilateral (quad) ---
  fill(200, 0, 200); // Magenta
  noStroke();
  
  // quad(x1, y1, x2, y2, x3, y3, x4, y4)
  // Connects four (x, y) points
  quad(300, 220, 500, 250, 450, 380, 320, 300);
  
  // --- Style 6: Several large black points ---
  stroke(0);
  strokeWeight(15); // Make the "points" large and easy to see
  
  point(50, 350);
  point(70, 370);
  point(90, 350);
}
