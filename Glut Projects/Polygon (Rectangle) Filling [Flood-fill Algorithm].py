import pyautogui
import time

# The code to be typed
code = """#include<windows.h>
#include<GL/glut.h>

float fill_color[3] = {1.0, 0.0, 0.0};
float original_color[3] = {0.0, 0.0, 0.0};

void myInit(void)
{
    glClearColor(1.0, 1.0, 1.0, 0.0);
    glColor3f(0.0, 0.0, 0.0);

    gluOrtho2D(0.0, 640.0, 0.0, 480);
}

void setPixel(int x, int y, float fill_color[3])
{
    glBegin(GL_POINTS);
      glColor3fv(fill_color);
      glVertex2i(x, y);
    glEnd();
    glFlush();
}

void getPixel(int x, int y, float color[3])
{
    glReadPixels(x, y, 1, 1, GL_RGB, GL_FLOAT, color);
}

void FloodFill (int x, int y, float fill_color[3], float original_color[3])
{
    float color[3];
    getPixel(x, y, color);
    if(color[0]==original_color[0] && color[1]==original_color[1] && color[2]==original_color[2])
    {
        setPixel(x, y, fill_color);
        FloodFill(x+1, y, fill_color, original_color);
        FloodFill(x, y+1, fill_color, original_color);
        FloodFill(x-1, y, fill_color, original_color);
        FloodFill(x, y-1, fill_color, original_color);
    }
}

void myMouse(int button, int state, int x, int y)
{
    y = 480 - y;
    if(button == GLUT_LEFT_BUTTON && state == GLUT_DOWN)
    {
        FloodFill(x, y, fill_color, original_color);
    }
}

void myDisplay(void)
{
    glClear(GL_COLOR_BUFFER_BIT);

    glBegin(GL_POLYGON);
      glVertex2i(100, 100);
      glVertex2i(300, 100);
      glVertex2i(300, 200);
      glVertex2i(100, 200);
    glEnd();

    glFlush();
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);
    glutInitWindowSize(640, 480);
    glutInitWindowPosition(100, 100);

    glutCreateWindow("Polygon (Rectangle) Filling [Flood-fill Algorithm]");
    glutDisplayFunc(myDisplay);
    glutMouseFunc(myMouse);

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