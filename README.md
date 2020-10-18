# Typing-Speed-Test-OCR-Bot
A python bot that uses Optical Character Recognition to beat typing speed tests.


NOTE:
  To run this program you will need to add the following packages to your python interpreter:
  
  - PyTesseract
  - PyAutoGui
  - Pynput
  - Keyboard
  
  You will also need to install TesseractOCR from:
  
  - https://github.com/UB-Mannheim/tesseract/wiki
  
  The program works by taking a screenshot of the region that includes the text, analyses the image and picks out the text as a string. It then converts this string into a list
  of all the characters and then simply simulates a key press of every character.
  
  For this to work:
  
  - Split your screen such that your browser showing the typing test is on the left half of the screen. (drag the top bar to the left hand side of your screen and it should do this
    automatically on windows)
  - After you run the program it delays 4 seconds before it begins to simulate key presses. In this time click in the box where you are expected to type.
  - To cancel the program, hold down the ENTER key for at least 1 second. If you dont cancel it when the typing test is done or when the test runs out of characters it could get messy...

Finally, Enjoy! This program uses the named packages above and I had no part in creating them. All credit of said packages go to their creators.
