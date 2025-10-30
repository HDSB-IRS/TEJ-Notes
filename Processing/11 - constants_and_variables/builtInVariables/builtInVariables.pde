/*-----------------------------------------------------------------------------
 Name:        Some Basics
 Purpose:     This sketch demonstrates common built-in variables like width, height, mouseX, mouseY, pmouseX, pmouseY, mousePressed, key, keyPressed, and frameCount.

 Author:      C. Brooks-Prenger
 Created:     30-Oct-2025
 Updated:     30-Oct-2025
-----------------------------------------------------------------------------*/

/*
 * Example: Built-in Variables
 *
 * This sketch demonstrates common built-in variables
 * like width, height, mouseX, mouseY, pmouseX, pmouseY,
 * mousePressed, key, keyPressed, and frameCount.
 */

// setup() runs once at the start.
void setup() {
  // 1. Set the window size.
  // This action also sets the built-in 'width' and 'height' variables.
  size(600, 400);
  
  // We can print the width and height to the console.
  println("Sketch width: " + width); // Prints 600
  println("Sketch height: " + height); // Prints 400
  
  background(230); // Set a light grey background
  println("Click and drag to draw. Hold a key to change the color.");
}

// draw() runs continuously, creating an animation.
void draw() {
  
  // 2. Use 'width' and 'height' to draw a line down the middle.
  stroke(150); // Grey line
  strokeWeight(1);
  line(width/2, 0, width/2, height);

  // 3. Use 'mousePressed' to check if the mouse is held down.
  if (mousePressed == true) {
    
    // 4. Check 'keyPressed' to see if a key is also held down.
    if (keyPressed == true) {
      stroke(200, 50, 50); // Draw in Red
    } else {
      stroke(50, 50, 200); // Draw in Blue
    }
    
    // 5. Use mouseX, mouseY, pmouseX, and pmouseY to draw a line
    // from the mouse's last position to its current position.
    strokeWeight(5);
    line(pmouseX, pmouseY, mouseX, mouseY);
  }
  
  // 6. Use 'frameCount' to display the elapsed frames
  // This will write text on top of the drawing.
  fill(0); // Black text
  noStroke();
  textSize(16);
  // We clear a small rectangle at the top-left to make the text readable
  fill(230);
  rect(0, 0, 200, 30);
  fill(0);
  text("Frame: " + frameCount, 10, 20);
}

// 7. This is an "event function" that uses the 'key' variable.
// It runs once every time a key is pressed.
void keyPressed() {
  // Print the specific key that was pressed to the console.
  println("Key pressed: " + key);
}
