//Declare a variable of type PImage to hold our image data
PImage myImage; 



// setup() runs one time at the very start.
void setup() {
  // Set the window size to 600 pixels wide by 400 pixels tall
  size(600, 400);
  
  // Set the background color once
  background(240); // Light grey
  
  // Load the image file into memory. 
  // Processing looks for this file in the sketch's "data" folder.
  myImage = loadImage("IRHS_logo.png"); 
  
  // Optional: Check if the image loaded successfully to prevent crashes
  if (myImage == null) {
    println("Error: Image could not be loaded. Check the filename and data folder.");
  }
  
  // By default, draw() loops. We'll add noLoop() 
  // so it only runs once, making a static image.
  // Remove the line below to see shapes drawn at the mouse position!
  noLoop(); 
}

/*
 * Loading and Displaying an Image
 * This sketch demonstrates how to declare an image variable,
 * load a file from the disk into memory, and render it to the screen.
 */


void draw() {
  // Set the background to a dark gray
  background(50); 
  
  // Display the image
  // Only attempt to draw the image if it successfully loaded into memory
  if (myImage != null) {
    // Syntax: image(PImage variable, x-coordinate, y-coordinate)
    // (0, 0) is the top-left corner of the window
    image(myImage, 50, 50);
    
    // Example: You can also specify width and height to scale the image
    // Uncomment the line below to draw a smaller version following your mouse
    // image(myImage, mouseX, mouseY, myImage.width / 4, myImage.height / 4);
  }
}
