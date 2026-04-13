# **Simple Animations in Processing**

Processing makes animation incredibly straightforward by using two main functions: `setup()` and `draw()`.

* `setup()`: Runs exactly once when the program starts. This is where you define the screen size, initialize variables, and load assets.  
* `draw()`: Runs continuously in a loop (usually 60 times per second). By drawing a shape, clearing the background, and drawing the shape in a slightly different position, you create the illusion of movement.

Here is a step-by-step guide to building animations, starting from the absolute basics and elaborating into more complex systems.

## **1\. The Absolute Basics: Moving on One Axis**

Before we tackle full 2D movement, let's start with something simpler: a ball that only moves left and right along the horizontal axis (the X-axis). To do this, we need to track its x position and its horizontal speed (xSpeed).
```java
// Variable for horizontal position
float x = 200;
// We'll keep the vertical position constant for now
float y = 200; 

// Variable for speed
float xSpeed = 5;

// Radius of the ball
float radius = 20;

void setup() {
  size(400, 400); // Set window size
  noStroke();     // Remove outlines from shapes
  fill(0, 150, 255); // Set the ball color to blue
}

void draw() {
  background(220); // Clear the screen every frame
  
  // 1. Update the position
  x = x + xSpeed;
  
  // 2. Check boundaries and bounce
  // If the ball hits the right edge OR the left edge
  if (x > width - radius || x < radius) {
    xSpeed = xSpeed * -1; // Reverse horizontal direction
  }
  
  // 3. Draw the ball
  circle(x, y, radius * 2);
}
```
## **2\. Expanding to Two Dimensions**

Now that we have horizontal movement working, let's add the vertical axis (the Y-axis). We just need to apply the exact same logic we used for x to our y variable.
```java
float x = 200;
float y = 200;

float xSpeed = 5;
float ySpeed = 3; // Add vertical speed

float radius = 20;

void setup() {
  size(400, 400);
  noStroke();
  fill(0, 150, 255);
}

void draw() {
  background(220);
  
  // 1. Update BOTH positions
  x = x + xSpeed;
  y = y + ySpeed;
  
  // 2. Check boundaries and bounce
  // Check left and right edges
  if (x > width - radius || x < radius) {
    xSpeed = xSpeed * -1;
  }
  
  // Check top and bottom edges
  if (y > height - radius || y < radius) {
    ySpeed = ySpeed * -1; // Reverse vertical direction
  }
  
  // 3. Draw the ball
  circle(x, y, radius * 2);
}
```

<!--
## **3\. Elaborating: Adding Gravity and Physics**

Straight-line bouncing is cool, but adding "gravity" makes it feel real. Gravity is simply a constant downward force added to the vertical speed every frame. We also add "dampening" so the ball loses a bit of energy with each bounce.
```java
float x = 50;
float y = 50;
float xSpeed = 3;
float ySpeed = 0; // Starts with no vertical speed

float gravity = 0.5;   // Pulls the ball down every frame
float dampening = 0.8; // Energy kept after a bounce (80%)

float radius = 20;

void setup() {
  size(400, 400);
  noStroke();
  fill(255, 100, 100);
}

void draw() {
  background(30); 
  
  // Apply gravity to vertical speed
  ySpeed = ySpeed + gravity;
  
  // Update position
  x = x + xSpeed;
  y = y + ySpeed;
  
  // Bounce off walls (left/right)
  if (x > width - radius || x < radius) {
    xSpeed = xSpeed * -1;
    // Keep ball strictly inside bounds to prevent getting stuck
    x = constrain(x, radius, width - radius); 
  }
  
  // Bounce off the floor
  if (y > height - radius) {
    // Reverse direction AND lose energy (dampening)
    ySpeed = ySpeed * -dampening; 
    y = height - radius; // Prevent ball from sinking into the floor
  }
  
  circle(x, y, radius * 2);
}
```
## **4\. Elaborating Further: Object-Oriented Programming (OOP)**

What if we want 100 bouncing balls? Creating 100 sets of x, y, xSpeed, and ySpeed variables is impossible. This is where Object-Oriented Programming comes in. We create a Ball **class** (a blueprint), and then we can create as many Ball **objects** as we want.
```
// Create a list to hold our balls
ArrayList<Ball> balls = new ArrayList<Ball>();

void setup() {
  size(600, 400);
  noStroke();
  
  // Create 50 balls with random properties and add them to the list
  for (int i = 0; i < 50; i++) {
    balls.add(new Ball(random(width), random(height/2)));
  }
}

void draw() {
  background(20);
  
  // Loop through every ball in our list
  for (Ball b : balls) {
    b.update();  // Calculate new position
    b.display(); // Draw it on screen
  }
}

// --- The Ball Blueprint (Class) ---
class Ball {
  float x, y;
  float vx, vy;
  float gravity = 0.2;
  float radius;
  color c;
  
  // Constructor: Sets up the initial state of the ball when created
  Ball(float startX, float startY) {
    x = startX;
    y = startY;
    vx = random(-3, 3);
    vy = random(-2, 2);
    radius = random(10, 25);
    c = color(random(100, 255), random(100, 255), random(100, 255));
  }
  
  // Method to update physics
  void update() {
    vy += gravity;
    x += vx;
    y += vy;
    
    // Floor bounce
    if (y > height - radius) {
      vy *= -0.8; // Dampening
      y = height - radius;
    }
    // Wall bounces
    if (x > width - radius || x < radius) {
      vx *= -0.9;
      x = constrain(x, radius, width - radius);
    }
  }
  
  // Method to draw the ball
  void display() {
    fill(c);
    circle(x, y, radius * 2);
  }
}
```
## **5\. The Final Polish: Adding Interactivity**

To make animations engaging, you should allow the user to affect the system. Using our OOP setup, it is incredibly easy to add a feature where clicking the mouse spawns a new ball exactly where the mouse is.

We just need to add the built-in mousePressed() function to the bottom of the sketch from Step 4:

// ... (Include setup, draw, and the Ball class from Step 4) ...

// This built-in function runs automatically whenever the mouse is clicked
void mousePressed() {
  // Add a new Ball object at the mouse's current X and Y coordinates
  balls.add(new Ball(mouseX, mouseY));
}

// Optional: Add a subtle trail effect in draw() instead of clearing completely!
// Replace background(20); in draw() with:
// fill(20, 50); // Almost transparent black
// rect(0, 0, width, height);

### **Summary of Core Animation Concepts:**

1. **The Loop:** draw() is your engine.  
2. **The Wipe:** Always draw a background() first to clear the old frame, otherwise, you'll just paint a solid streak.  
3. **State:** Variables (x, y) represent the current state of an object.  
4. **Rate of Change:** Velocity (xSpeed) changes Position. Acceleration (gravity) changes Velocity.  
5. **Boundaries:** "If" statements keep things on the screen.  
6. **Scalability:** Classes and Arrays/Lists let you manage hundreds of moving parts cleanly.
-->