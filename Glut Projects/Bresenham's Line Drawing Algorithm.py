import pyautogui
import time

# The code to be typed (with proper formatting)
code_lines = [
    "#include<windows.h>",
    "#include<GL/glut.h>",
    "",
    "void myInit(void)",
    "{",
    "    glClearColor(1.0, 1.0, 1.0, 0.0);",
    "    glColor3f(0.0, 0.0, 0.0);",
    "",
    "    gluOrtho2D(0.0, 640.0, 0.0, 480.0);",
    "}",
    "",
    "void myDisplay(void)",
    "{",
    "    glClear(GL_COLOR_BUFFER_BIT);",
    "    glPointSize(4.0);",
    "",
    "    int x1 = 20, y1 = 20, xn = 400, yn = 250; // 0<m<1",
    "    int x = x1, y = y1;",
    "    int dx = xn - x1, dy = yn - y1;",
    "",
    "    int dS = 2*dy;",
    "    int dT = 2*(dy - dx);",
    "",
    "    int d = 2*dy - dx;",
    "",
    "    glBegin(GL_POINTS);",
    "        glVertex2i(x, y);",
    "    glEnd();",
    "",
    "    while(x < xn)",
    "    {",
    "        x++;",
    "        if(d < 0) // Bottom Pixel S is Chosen",
    "        {",
    "            d = d + dS;",
    "        }",
    "        else if(d >= 0) // Top Pixel T is Chosen",
    "        {",
    "            y = y + 1;",
    "            d = d + dT;",
    "        }",
    "",
    "        glBegin(GL_POINTS);",
    "            glVertex2i(x, y);",
    "        glEnd();",
    "    }",
    "",
    "    glFlush();",
    "}",
    "",
    "int main(int argc, char** argv)",
    "{",
    "    glutInit(&argc, argv);",
    "    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);",
    "    glutInitWindowSize(640, 480);",
    "    glutInitWindowPosition(100, 100);",
    "",
    "    glutCreateWindow(\"Bresenham's Line Drawing Algorithm\");",
    "    glutDisplayFunc(myDisplay);",
    "",
    "    myInit();",
    "    glutMainLoop();",
    "",
    "    return 0;",
    "}"
]

# Give some time to switch to the text editor
print("Switch to your text editor within 5 seconds...")
time.sleep(5)

# Type each line carefully with delays
for line in code_lines:
    pyautogui.write(line, interval=0.1)  # Slower typing speed (0.1s per char)
    pyautogui.press('enter')
    time.sleep(0.2)  # Extra delay after each line