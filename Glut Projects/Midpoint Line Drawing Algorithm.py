import pyautogui
import time

# The code to be typed
code = """#include<windows.h>
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

    int x1 = 20, y1 = 20, xn = 400, yn = 250; // 0<=m<=1
    int x = x1, y = y1;

    int dx = xn - x1, dy = yn - y1;
    int d = 2*dy - dx;
    int dNE = 2*(dy - dx);
    int dE = 2*dy;

    glBegin(GL_POINTS);
      glVertex2i(x, y);
    glEnd();

    while(x<xn)
    {
        if(d>0) //Upper Pixel of Midpoint is Chosen
        {
            d = d + dNE;
            x = x + 1;
            y = y + 1;
        }
        else if(d<=0) //Lower Pixel of Midpoint is Chosen
        {
            d = d + dE;
            x = x + 1;
        }
        glBegin(GL_POINTS);
          glVertex2i(x, y);
        glEnd();
    }

    glFlush();
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);
    glutInitWindowSize(640, 480);
    glutInitWindowPosition(100, 100);

    glutCreateWindow("Midpoint Line Drawing Algorithm");
    glutDisplayFunc(myDisplay);

    myInit();
    glutMainLoop();

    return 0;
}
"""

# Give time to switch to text editor
print("Switch to your text editor within 5 seconds...")
time.sleep(5)

# Type the code with proper delays
pyautogui.write(code, interval=0.08)  # 0.08 second delay between characters