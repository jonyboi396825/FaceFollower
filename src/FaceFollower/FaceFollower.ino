/**
 * The code to be uploaded to the Arduino.
*/

// motor pins
#define RIGHT1 3
#define RIGHT2 4
#define RIGHTEN 5
#define LEFTEN 6
#define LEFT1 7
#define LEFT2 8

short speedL = 0; // -255 to 255, 255 indicating one direction, -255 indicating the other
short speedR = 0; // -255 to 255, 255 indicating one direction, -255 indicating the other

void setup(){
    Serial.begin(115200);

    // motor pins
    pinMode(RIGHT1, OUTPUT);
    pinMode(RIGHT2, OUTPUT);
    pinMode(RIGHTEN, OUTPUT);
    pinMode(LEFTEN, OUTPUT);
    pinMode(LEFT1, OUTPUT);
    pinMode(LEFT2, OUTPUT);
}

void loop(){
    // read from serial port if available
    if (Serial.available()){
        parseInput(Serial.readStringUntil('\n'));

        // Serial.print(speedL);
        // Serial.print(" ");
        // Serial.print(speedR);
        // Serial.println();
    }

    driveL();
    driveR();
}

/**
 * Drives left motor given speeds of speedL 
*/
void driveL(){
    if (speedL == 0){
        digitalWrite(LEFT1, LOW);
        digitalWrite(LEFT2, LOW);
        analogWrite(LEFTEN, 0);
    }

    // drive different directions given if value is positive or negative
    if (speedL > 0){
        digitalWrite(LEFT1, HIGH);
        digitalWrite(LEFT2, LOW);
        analogWrite(LEFTEN, speedL);
    } else{
        digitalWrite(LEFT1, LOW);
        digitalWrite(LEFT2, HIGH);
        analogWrite(LEFTEN, -speedL);
    }
}

/**
 * Drives right motor given speeds of speedR 
*/
void driveR(){
    if (speedR == 0){
        digitalWrite(RIGHT1, LOW);
        digitalWrite(RIGHT2, LOW);
        analogWrite(RIGHTEN, 0);
    }

    // drive different directions given if value is positive or negative
    if (speedR > 0){
        digitalWrite(RIGHT1, HIGH);
        digitalWrite(RIGHT2, LOW);
        analogWrite(RIGHTEN, speedR);
    } else{
        digitalWrite(RIGHT1, LOW);
        digitalWrite(RIGHT2, HIGH);
        analogWrite(RIGHTEN, -speedR);
    }
}

/**
 * Gets input from serial port and recursively parses it into lspeed and rspeed.
 * 
 * @param str: the string to be parsed
*/
void parseInput(String str){
    // example test cases:
    // "l:25;r:54"
    // "r:43"
    // "l:66"
    // "r:25;l:22"
    // handle string until first semicolon, then recursively handle rest of string
    // terminating condition = no semicolon

    // find semicolon
    int ind_semicolon = -1;

    for (int i = 0; i < str.length(); i++){
        if (str[i] == ';'){
            ind_semicolon = i;
            break;
        }        
    }

    if (ind_semicolon == -1) ind_semicolon = str.length();

    // find colon
    int ind_colon = -1;
    for (int i = 0; i < ind_semicolon; i++){
        if (str[i] == ':'){
            ind_colon = i;
            break;
        }
    }

    // if no colon found, then return because invalid
    if (ind_colon == -1) return;

    if (str.substring(0, ind_colon) == "l"){
        // left
        speedL = str.substring(ind_colon+1, ind_semicolon).toInt();
        if (speedL > 255) speedL = 255;
        if (speedL < -255) speedL = -255;
    }
    else if (str.substring(0, ind_colon) == "r"){
        // right
        speedR = str.substring(ind_colon+1, ind_semicolon).toInt();
        if (speedR > 255) speedR = 255;
        if (speedR < -255) speedR = -255;
    }

    // recurse if there is a semicolon remaining
    if (ind_semicolon != str.length()){
        parseInput(str.substring(ind_semicolon+1, str.length()));
    }
}
