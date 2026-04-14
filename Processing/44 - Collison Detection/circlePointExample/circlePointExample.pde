color circleColor;
int circleX =200;
int circleY =200;
int circleSize= 50;

/**
 * This function calculates the distance between two points given by (x1, y1) and (x2, y2)
 *
 * @param x1 The x-coordinate of the first point
 * @param y1 The y-coordinate of the first point
 * @param x2 The x-coordinate of the second point
 * @param y2 The y-coordinate of the second point
 * @return The distance between the two points
 */
float distFromPoints(float x1, float y1, float x2, float y2) {
  float distance = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2));
  return distance;
}

void setup() {
  size(400, 400);
}

void draw() {

  if (distFromPoints(circleX, circleY, mouseX, mouseY) < circleSize/2) {
    // A collision happens!
    circleColor = color(100, 0, 0);
  } else {
    // no collision happened
    circleColor = color(255, 0, 0);
  }
  
  fill(circleColor);
  ellipse(circleX, circleY, circleSize, circleSize);
}
