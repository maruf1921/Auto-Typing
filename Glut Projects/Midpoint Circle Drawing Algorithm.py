import pyautogui
import time

# The code to be typed
code = """
#include<windows.h>
#include<GL/glut.h>

void myInit(void)
{
    glClearColor(1.0, 1.0, 1.0, 0.0);
    glColor3f(0.0, 0.0, 0.0);

    gluOrtho2D(0.0, 640.0, 0.0, 480);
}

void myDisplay(void)
{
    glClear(GL_COLOR_BUFFER_BIT);
    glPointSize(4.0);

    int x = 0, r = 100, y = r, h = 320, k = 240;
    int d = 1 - r;

    while(x<=y)
    {
        glBegin(GL_POINTS);
          glVertex2i(x+h, y+k);
          glVertex2i(-x+h, y+k);
          glVertex2i(x+h, -y+k);
          glVertex2i(-x+h, -y+k);

          glVertex2i(y+h, x+k);
          glVertex2i(-y+h, x+k);
          glVertex2i(y+h, -x+k);
          glVertex2i(-y+h, -x+k);
        glEnd();

        if(d<0) //Top Pixel T is Chosen
        {
            d = d + 2*x + 3;
        }
        else if(d>=0) //Bottom Pixel S is Chosen
        {
            d = d + 2*(x - y) + 5;
            y = y - 1;
        }
        x = x + 1;
    }

    glFlush();
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);
    glutInitWindowSize(640, 480);
    glutInitWindowPosition(100, 100);

    glutCreateWindow("Midpoint Circle Drawing Algorithm");
    glutDisplayFunc(myDisplay);

    myInit();
    glutMainLoop();

    return 0;
}"""

# Give time to switch to text editor
print("Switch to your text editor within 5 seconds...")
time.sleep(5)

# Type the code with proper delays
pyautogui.write(code, interval=0.08)  # 0.08 second delay between characters