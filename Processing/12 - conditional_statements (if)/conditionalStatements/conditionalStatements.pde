/*-----------------------------------------------------------------------------
 Name:        Conditional Shapes
 Purpose:     Demonstrates if, else if, else, and logical operators (&&, ||) 
              to draw different shapes based on mouse position and input.
 
 Author:      C. Brooks-Prenger
 Created:     02-Nov-2025
 Updated:     02-Nov-2025
-----------------------------------------------------------------------------*/

// setup() runs once at the start.
void setup() {
  size(600, 600);
  
  // Set up text properties for labels
  textSize(16);
  textAlign(CENTER, CENTER);
}

// draw() runs 60 times per second.
void draw() {
  // Redraw the background each frame
  background(240);

  // 1. Basic if-else
  // Checks if the mouse is on the left or right side of the screen.
  if (mouseX < width/2) {
    // If true: draw a red circle in the left half
    fill(255, 50, 50);
    noStroke();
    ellipse(width/4, 150, 100, 100);
    fill(0);
    text("if (mouseX < width/2)", width/4, 50);
  } else {
    // If false: draw a blue square in the right half
    fill(50, 50, 255);
    noStroke();
    rect(width * 0.75 - 50, 100, 100, 100);
    fill(0);
    text("else", width * 0.75, 50);
  }

  // 2. if-else if-else
  // Checks the vertical position of the mouse.
  fill(0);
  text("if-else if-else chain (vertical)", width/2, 280);
  
  if (mouseY < 350) {
    // If in the top section, draw a green line
    stroke(0, 200, 0);
    strokeWeight(10);
    line(0, 320, width, 320);
  } else if (mouseY < 450) {
    // If in the middle section, draw a magenta line
    stroke(200, 0, 200);
    strokeWeight(10);
    line(0, 400, width, 400);
  } else {
    // If in the bottom section, draw an orange line
    stroke(255, 150, 0);
    strokeWeight(10);
    line(0, 500, width, 500);
  }

  // 3. Logical && (AND)
  // This shape only appears if *both* conditions are true.
  fill(0);
  noStroke();
  text("&& (AND): Hold mouse AND any key", width/2, 550);
  
  if (mousePressed == true && keyPressed == true) {
    // Draw a large, transparent black circle
    fill(0, 0, 0, 100); // 100 is transparency
    ellipse(width/2, height/2, 400, 400);
  }
  
  // 4. Logical || (OR)
  // This shape appears if *either* condition is true.
  fill(0);
  noStroke();
  text("Triangle: || (OR): Go to left OR bottom", 150, 10);
  
  if (mouseX < 100 || mouseY > 500) {
    // Draw a yellow triangle at the top
    fill(255, 255, 0);
    stroke(0);
    strokeWeight(2);
    triangle(20, 20, 80, 20, 50, 80);
  }
}
