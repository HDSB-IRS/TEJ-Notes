String programState;
int counter;

void setup() {
  size(400, 400);
  textSize(40);
  programState = "reset";
}

void draw() {
  if (programState == "start") {
    background(255, 0, 0); //Red
    text("Start Screen\r\nClick to Continue",50,200);
    if (mousePressed) {
      programState = "play";
    }
  } else if (programState == "reset") {
    programState = "start";
    counter = 0;
    delay(500);
  } else if (programState == "play") {
    background(0, 0, 255); //Blue
    counter+= 1;
    println(counter);
    if (counter > 200) {
      programState = "gameOver";
    }
  } else if (programState == "gameOver") {
    background(0, 255, 0); //Green
    if (mousePressed) {
      programState ="reset";
    }
  } else {
    print("Error, no program state recognized");
  }
}
