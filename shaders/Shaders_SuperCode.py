import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

program = 0

VERTEX_SHADER_CODE = """
    #version 120
    
    void main(){
        gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
    }
"""
FRAGMENT_SHADER_CODE = """
    #version 120
    
    const float height = 720, width = 1280;
    const int max_iteration = 1000;
    uniform float theta;
    
    void main(){
        // FRACTAL CODE
        
        float x0 = 3.5 * gl_FragCoord.x/width - 2.5, y0 = 2*gl_FragCoord.y/height - 1;
        int iteration = 0;
        /*
        //MANDELBROT FRACTAL
        float x = 0.0, y = 0.0;
        while (x*x + y*y < 4  && iteration < max_iteration) {
            float xtemp = x*x - y*y;
            y = 2*x*y + y0;
            x = xtemp + x0;
            iteration++;
        }
        
        //JULIA FRACTAL
        float x = x0, y = y0, s = sin(theta), c = cos(theta);
        while (x*x + y*y < 4  &&  iteration < max_iteration) {
            float xtemp = x*x - y*y;
            y = 2*x*y + 0.7885 * c;
            x = xtemp + 0.7885 * s;
            iteration++; 
        }
        
        int i = max_iteration/4, j = max_iteration/2;
        gl_FragColor = 20*vec4(float(mod(iteration, i))/i , float(mod(iteration, j))/j, float(iteration)/max_iteration, 1);
        */
        
        //FUNCTIONS
        /*
        float x = gl_FragCoord.x / width, y = gl_FragCoord.y / height;
        float color;
        //color = step(0.5, x); //STEP
        //color = x; //LINEAR
        //color = x * x; //QUADRATIC
        //color = 1 - pow(x * x + y * y, 0.5); //RADIAL
        //color = pow(x, 5); //EXPONENTIAL
        //color = 9 * x * exp(1 - 9 * x); //IMPULSE
        
        gl_FragColor = vec4(color, color, color, 1);
        */
        //LENS FLARE
        /*
        float t = theta;
        vec2 r = vec2(width, height);

        vec3 c;
        float l,z = t;
        for(int i = 0; i < 3 ; i++) {
            vec2 uv, p = gl_FragCoord.xy/r - 0.5;
            //uv = p;
            p.x *= r.x/r.y;
            z += .07;
            l = length(p);
            uv += p/l * (sin(z) + 1) * abs(sin(9*l - 2*z));
            c[i] = 0.01/length( abs( mod(uv, 1) - 0.5));
        }
        gl_FragColor = vec4(c/l,1);
        
        */
        
        float x = 2 * gl_FragCoord.x / width - 1, y = 2 * gl_FragCoord.y / height - 1;
        
        vec3 color = vec3(0.2, 1, 0);
        vec3 color2 = vec3(1, 0.2, 0);
        vec3 color3 = vec3(0, 0.2, 1);
        vec3 color4 = vec3(0.7, 0.1, 1);
        
        color  *= abs(0.0025 / sin(x*2 + 0.5  +    sin(y + 2*theta)));
        color2 *= abs(0.005 / sin(x  +            sin(y + 4*theta)));
        color3 *= abs(0.01 / sin(x + 0.66 +    0.3*sin(y + 5*theta)));
        color4 *= abs(0.01 / sin(2*x - 0.66 +    0.5*sin(y + 7*theta)));
        
        gl_FragColor = vec4(color + color2 + color3 + color4, 1);
    }
"""

def render():
    glColor3fv((1, 1, 1))
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_QUADS)
    glVertex3fv(( 1, -1, 0))
    glVertex3fv(( 1,  1, 0))
    glVertex3fv((-1,  1, 0))
    glVertex3fv((-1, -1, 0))
    glEnd()
    
def shade(const, program, code):
    shader = glCreateShader(const)
    glShaderSource(shader, code)
    glCompileShader(shader)
    print(glGetShaderInfoLog(shader))
    glAttachShader(program, shader)

def main():
    display = (1280, 720)
    pygame.init()
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    program = glCreateProgram()
    shade(GL_VERTEX_SHADER, program, VERTEX_SHADER_CODE)
    shade(GL_FRAGMENT_SHADER, program, FRAGMENT_SHADER_CODE)
    glLinkProgram(program)
    glUseProgram(program)
    
    theta = 4.3;
        
    print("Done")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        theta += 0.01;
        glUniform1f(glGetUniformLocation(program, "theta"), theta);
        render()
        pygame.display.flip()
        pygame.time.wait(13)
    
main()
