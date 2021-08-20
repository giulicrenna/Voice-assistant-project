void setup()
{
  Serial.begin(9600);

  for (int thisPin = 2; thisPin < 9; thisPin++)
  {
    pinMode(thisPin, OUTPUT);
  }
}

void loop()
{
  if (Serial.available() > 0)
  {
    int inByte = Serial.read();
    switch (inByte)
    {
    case 'a':
      digitalWrite(2, HIGH);
      break;
    case 'b':
      digitalWrite(3, HIGH);
      break;
    case 'c':
      digitalWrite(4, HIGH);
      break;
    case 'd':
      digitalWrite(5, HIGH);
      break;
    case 'e':
      digitalWrite(6, HIGH);
      break;
    case 'f':
      digitalWrite(7, HIGH);
      break;
    case 'g':
      digitalWrite(8, HIGH);
      break;
    case 'h':
      digitalWrite(9, HIGH);
      break;


    case 'i':
      digitalWrite(2, LOW);
      break;
    case 'j':
      digitalWrite(3, LOW);
      break;
    case 'k':
      digitalWrite(4, LOW);
      break;
    case 'l':
      digitalWrite(5, LOW);
      break;
    case 'm':
      digitalWrite(6, LOW);
      break;
    case 'n':
      digitalWrite(7, LOW);
      break;
    case 'o':
      digitalWrite(8, LOW);
      break;
    case 'p':
      digitalWrite(9, LOW);
      break;
     
    default:
      for (int thisPin = 2; thisPin < 9; thisPin++)
      {
        digitalWrite(thisPin, LOW);
      }
    }
  }
}
