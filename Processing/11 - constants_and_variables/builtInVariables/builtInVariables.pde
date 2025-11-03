/*-----------------------------------------------------------------------------
 Name:        Built-in Variables and Text
 Purpose:     Demonstrates built-in variables (width, height, mouseX, 
              mouseY, pmouseX, pmouseY, frameCount, mousePressed, 
              keyPressed, key) and displays text on the screen.
 
 Author:      C. Brooks-Prenger
 Created:     02-Nov-2025
 Updated:     02-Nov-2025
-----------------------------------------------------------------------------*/

// setup() runs once at the start.
void setup() {
  // Use size() to set the window dimensions.
  // This also sets the built-in 'width' and 'height' variables.
  size(600, 400);
}

// draw() runs 60 times per second.
void draw() {
  // 1. Use 'width' and 'height'
  // We'll draw two rectangles using the window's dimensions.
  noStroke();
  fill(230, 230, 250); // Light purple
  rect(0, 0, width/2, height/2); // Top-left quadrant
  rect(width/2, height/2, width/2, height/2); // Bottom-right quadrant
  
  // 2. Use 'mouseX' and 'mouseY'
  // Draw an ellipse directly at the mouse's current (x, y) coordinates.
  fill(0, 150, 200); // Blue
  stroke(0);
  strokeWeight(2);
  ellipse(mouseX, mouseY, 40, 40);

  // 3. Use 'pmouseX' and 'pmouseY'
  // Draw a small rectangle at the mouse's *previous* (x, y) coordinates.
  fill(200, 0, 0); // Red
  noStroke();
  rect(pmouseX, pmouseY, 10, 10);
  
  // 4. Use 'frameCount'
  // Draw a line that moves down the screen.
  // We use modulo (%) to make 'frameCount' wrap around the 'height'.
  float yPos = frameCount % height;
  stroke(0, 180, 0); // Green
  strokeWeight(4);
  line(0, yPos, width, yPos);
  
  // 5. Use 'mousePressed' (a boolean)
  // We can cast 'true' to 1 and 'false' to 0.
  // When not pressed, size = 20 + (0 * 80) = 20
  // When pressed,    size = 20 + (1 * 80) = 100
  float circleSize = 20 + (int(mousePressed) * 80);
  fill(255, 150, 0); // Orange
  noStroke();
  ellipse(width/2, height/2, circleSize, circleSize);
  
  // 6. Use 'keyPressed' (boolean) and 'key' (char)
  // 'keyPressed' (0 or 1) will control the red channel.
  // 'key' (ASCII value) will control the green channel.
  float redColor = 255 * int(keyPressed);
  float greenColor = int(key); // 'a' is 97, 'b' is 98, etc.
  fill(redColor, greenColor, 100);
  stroke(0);
  strokeWeight(3);
  rect(50, 50, 80, 80);

  // 7. Use 'frameCount' with text()
  // This section displays the frame count at the top-left.
  // It's drawn last to appear on top of all other shapes.
  
  // Draw a white rectangle to clear the area behind the text
  fill(255); // White
  noStroke();
  rect(5, 5, 150, 30);
  
  // Draw the text
  fill(0); // Black text
  textSize(16);
  // text(data, x, y)
  // Concatenate the string "Frame: " with the frameCount variable
  text("Frame: " + frameCount, 10, 25);
}
