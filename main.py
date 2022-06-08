import time
import pymata4H.pymata4 as pymat


my_board = pymat.Pymata4()
my_board.set_pin_mode_digital_output(7)
my_board.set_pin_mode_digital_output(4)
my_board.set_pin_mode_pwm_output(9)
my_board.set_pin_mode_pwm_output(10)
my_board.set_pin_mode_pwm_output(11)

def red_color():
    my_board.pwm_write(9, 200)
    my_board.pwm_write(10, 0)
    my_board.pwm_write(11, 0)
def white_color():
    my_board.pwm_write(9, 200)
    my_board.pwm_write(10, 200)
    my_board.pwm_write(11, 200)
def green_color():
    my_board.pwm_write(9, 0)
    my_board.pwm_write(10, 200)
    my_board.pwm_write(11, 0)
def blue_color():
    my_board.pwm_write(9, 0)
    my_board.pwm_write(10, 0)
    my_board.pwm_write(11, 200)

def police():
    red_color()
    time.sleep(0.05)
    red_color()
    off_color()
    blue_color()
    time.sleep(0.05)
    blue_color()
    time.sleep(0.05)
    red_color()
    time.sleep(0.05)
    red_color()
    time.sleep(0.05)

def off_color():
    my_board.pwm_write(9, 0)
    my_board.pwm_write(10, 0)
    my_board.pwm_write(11, 0)



def dim():
    for i in range(0,255):
        my_board.pwm_write(9, i)
        my_board.pwm_write(10, i)
        my_board.pwm_write(11, i)
        time.sleep(0.05)
    for j in range(255,0,-1):
        my_board.pwm_write(9, j)
        my_board.pwm_write(10, j)
        my_board.pwm_write(11, j)
        time.sleep(0.05)



try:

    while True:
        colors_list = ['red','green','blue','white','off','police','dim']
        color_in = input('type ur color\n')
        if color_in in colors_list:
            if color_in.lower() == 'red':
                red_color()
            elif color_in.lower() == 'green':
                green_color()
            elif color_in.lower() == 'blue':
                blue_color()
            elif color_in.lower() == 'off':
                off_color()
            elif color_in.lower() == 'white':
                white_color()
            elif color_in.lower() == 'police':
                t = time.time()
                while time.time() - t <= 15:
                    police()
            elif color_in.lower() =='dim':
                dim()

        else:
            r_value = input('enter red value?')
            g_value = input('enter green value?')
            b_value = input('enter blue value?')
            r_value = int(r_value)
            g_value = int(g_value)
            b_value = int(b_value)
            my_board.pwm_write(9, r_value)
            my_board.pwm_write(10, g_value)
            my_board.pwm_write(11, b_value)



except:
    off_color()


