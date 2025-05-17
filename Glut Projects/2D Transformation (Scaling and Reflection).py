import pyautogui
import time

# The code to be typed
code = """#include<windows.h>
#include<GL/glut.h>

void myInit(void)
{
    glClearColor(1.0, 1.0, 1.0, 0.0);
    glColor3f(0.0, 0.0, 0.0);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();

    gluOrtho2D(-320.0, 320.0, -240.0, 240.0);
    glMatrixMode(GL_MODELVIEW);
}

void Trapezium(void)
{
    glBegin(GL_LINE_LOOP);
      glVertex2i(10, 10);
      glVertex2i(150, 10);
      glVertex2i(140, 200);
      glVertex2i(10, 200);
    glEnd();
}

void myDisplay(void)
{
    glClear(GL_COLOR_BUFFER_BIT);
    glLineWidth(4.0);

    Trapezium();

    glTranslatef(80.0, 105.0, 0.0); //Move origin to center of rectangle
    glScalef(2.0, 0.5, 0.0); //Scaling (Sx = 2.0, Sy = 0.5)
    glTranslatef(-80.0, -105.0, 0.0); //Move origin back
    glColor3f(0.0, 0.0, 1.0);
    Trapezium();

    glLoadIdentity();

    glScalef(1.0, -1.0, 0.0); //Reflection about X-axis
    //glScalef(-1.0, 1.0, 0.0); //Reflection about Y-axis
    glColor3f(1.0, 0.0, 0.0);
    Trapezium();

    glFlush();
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);
    glutInitWindowSize(640, 480);
    glutInitWindowPosition(100, 100);

    glutCreateWindow("2D Transformation (Scaling and Reflection)");
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