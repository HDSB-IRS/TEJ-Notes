//Declare a variable of type PImage to hold our image data
PImage spriteSheet; 
//Declare a variable for a single frame
PImage frame;

//Declare variables for the frame size
int frameWidth=16;  
int frameHeight=28;
int numFrames = 1;


// setup() runs one time at the very start.
void setup() {
  // Set the window size to 600 pixels wide by 400 pixels tall
  size(600, 400);
  
  // Set the background color once
  background(240); // Light grey
  
  // Load the image file into memory. 
  // Processing looks for this file in the sketch's "data" folder.
  spriteSheet = loadImage("0x72_DungeonTilesetII_v1.3.png"); 
  
  // Optional: Check if the image loaded successfully to prevent crashes
  if (spriteSheet == null) {
    println("Error: Image could not be loaded. Check the filename and data folder.");
  }
  
  //How to Calculate the width and height of a single frame is the spritesheet only has one image row
  //If the sheet has 6 frames in a row, one frame's width is the total width divided by 6
  //frameWidth = spriteSheet.width / numFrames;
  //frameHeight = spriteSheet.height;
  
  //Grab a single frame of data from the sprite sheet
  frame = spriteSheet.get(127,236, frameWidth, frameHeight);

  // By default, draw() loops. We'll add noLoop() 
  // so it only runs once, making a static image.
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
  
  //Display the image
  // Only attempt to draw the image if it successfully loaded into memory
  if (spriteSheet != null) {
    // Syntax: image(PImage variable, x-coordinate, y-coordinate)
    // (0, 0) is the top-left corner of the window
    image(spriteSheet, 50, 50);
    

    //Draw the new image
    image(frame, 0, 0);
    
  
  }
}
