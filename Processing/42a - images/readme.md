# Loading an Image in Processing

## Prerequisites: The `data` Folder

In Processing, external assets like images, fonts, and sounds must be placed in a specific folder so the sketch can locate them.

1. Create a new Processing sketch and save it (e.g., `ImageLoaderExample`).
2. Press **Ctrl+K** (Windows/Linux) or **Cmd+K** (Mac) to open the sketch folder.
3. Inside that folder, create a new folder and name it exactly **`data`** (all lowercase).
4. Place your image file inside the `data` folder. For this example, rename your image to `sample_image.jpg`.

---

## 💻 The Processing Code

Copy and paste the following code into your main sketch file:

```java
/*
 * Loading and Displaying an Image
 * This sketch demonstrates how to declare an image variable,
 * load a file from the disk into memory, and render it to the screen.
 */

// 1. Declare a variable of type PImage to hold our image data
PImage myImage; 

void setup() {
  // Set the size of the display window (width, height)
  size(800, 600); 
  
  // 2. Load the image file into memory. 
  // Processing looks for this file in the sketch's "data" folder.
  myImage = loadImage("sample_image.jpg"); 
  
  // Optional: Check if the image loaded successfully to prevent crashes
  if (myImage == null) {
    println("Error: Image could not be loaded. Check the filename and data folder.");
  }
}

void draw() {
  // Set the background to a dark gray
  background(50); 
  
  // 3. Display the image
  // Only attempt to draw the image if it successfully loaded into memory
  if (myImage != null) {
    // Syntax: image(PImage variable, x-coordinate, y-coordinate)
    // (0, 0) is the top-left corner of the window
    image(myImage, 0, 0);
    
    // Example: You can also specify width and height to scale the image
    // Uncomment the line below to draw a smaller version following your mouse
    // image(myImage, mouseX, mouseY, myImage.width / 4, myImage.height / 4);
  }
}
```