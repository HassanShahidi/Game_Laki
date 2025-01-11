import turtle
from time import time , sleep
from random import randint
import txt

# تنظیمات اولیه
time_game = 60
page_number = 1
address_record = 'record.txt'
# رنگ لاک پشت
color_index = 0
AllColorLaki = ['DarkGreen','MediumBlue','DarkSlateGray', 'Indigo', 'Maroon', 'Lime', 'Magenta', 'Red', 'Aqua', 'Orange']


def setup_screen():
    global game_screen
    game_screen = turtle.Screen()
    game_screen.setup(700, 700)
    game_screen.title('Game Laki')
    game_screen.bgpic('PNG/back.gif')

# صفحه شروع بازی
def draw_first_page():
    food.st()
    Laki.shapesize(2)
    game_screen.onkey(lambda: None, 'a')
    game_screen.onkey(lambda: None, 'd')
    game_screen.onkey(setup_game_start, 's')
    hide_button() # مخفی کردن دکمه ها
    print_cadr_button(-50)
    cadr.goto(-40, -135)
    cadr.color('red')
    cadr.write('(s)شروع', font = ('b koodak', 20, 'bold'))
    write_time.write(f'زمان = {str(time_game)}', font = ('b koodak', 12, 'bold'))
    write_score.write(f'امتياز = {0}', font = ('b koodak', 12, 'bold'))

# صفحه تغییر رنگ 
def draw_second_page():
    # رسم عناصر برای صفحه دوم
    food.ht()
    new_record.ht()
    cadr.clear()
    food.clear()
    write_score.clear()
    write_time.clear()
    Laki.shapesize(4)
    game_screen.onkey(previous_color, 'a')
    game_screen.onkey(next_color, 'd')
    game_screen.onkey(lambda: None, 's')
    show_button() # نمایش دکمه ها

#### تابع سازنده لاک پشت ####
def create_turtle(x=0, y=0, shape='classic', color_pen='Navy', color_turtle='Navy', shapesize=1 , show=False, photo=False, speed=0):
    if photo :
        game_screen.register_shape(shape)
    tr = turtle.Turtle(shape)
    if not show:
        tr.ht()
    tr.up()
    tr.speed(speed)
    tr.shapesize(shapesize)
    tr.goto(x, y)
    tr.color(color_pen, color_turtle)
    return tr
# ویژگی هر لاک پشت
def create_turtles():
    # ساختن لاکی
    global Laki
    Laki = create_turtle(shape='turtle', show=True, shapesize=2,
                         color_pen='DarkGreen', color_turtle='DarkGreen',
                         speed=6
                         )
    # ساختن غذا
    global food
    food = create_turtle(50, 0, 'PNG/ball.gif', show=True, photo=True)
    # عکس رکورد جدید
    global new_record
    new_record = create_turtle(200, 200, 'PNG/new record.gif', photo=True)
    # ساختن دکمه تغییر رنگ 
    global button_rt
    global button_left
    button_rt = create_turtle(0, 0, 'arrow', 'Black', 'DarkRed', 2)
    button_left = button_rt.clone()
    button_left.left(180)
    # چاپ زمان بازی
    global write_time
    write_time = create_turtle(275, 326)
    global write_time_321
    write_time_321 = create_turtle(-15, 10)
    global write_time_60
    write_time_60 = create_turtle(-130, 70)
    # چاپ امتیاز
    global write_score
    write_score = create_turtle(-325, 326)
    # چاپ کادر
    global cadr
    cadr = create_turtle()

# ساختن کادر صفحه
def create_cadr_screen():
    boundary_turtle = turtle.Turtle()
    boundary_turtle.ht()  # مخفی کردن تورتل
    boundary_turtle.width(4)
    boundary_turtle.speed('fastest')
    boundary_turtle.up()
    boundary_turtle.goto(325, 325)
    boundary_turtle.down()
            # کشیدن مرز
    for _ in range(4):
        boundary_turtle.rt(90)
        boundary_turtle.fd(650)
# توابع کشیدن کادر پایان بازی
def print_cadr():
    cadr.width(7)
    cadr.color('DarkGreen', 'MediumSpringGreen')
    cadr.goto(-150, -150)
    cadr.down()
    cadr.begin_fill()
    for x in (300, 220, 300, 220):
        cadr.fd(x)
        cadr.left(90)
    cadr.end_fill()
    cadr.up()
def print_cadr_button(x = -80):
    cadr.width(4)
    cadr.color('DarkBlue', 'DeepSkyBlue')
    cadr.goto(x, -135)
    cadr.down()
    cadr.begin_fill()
    tool = (x*-2) + 5
    for _ in (tool, 45, tool, 45):
        cadr.fd(_)
        cadr.left(90)
    cadr.end_fill()
    cadr.up()

# نمایش دکمه ها 
def show_button():
    # نمایش دکمه راست
    button_rt.goto(150, -40)
    button_rt.write('(d)', font=('Arial', 14, 'bold'))
    button_rt.goto(150, 0)
    button_rt.st()
    # نمایش دکمه چپ
    button_left.goto(-170, -40)
    button_left.write('(a)', font=('Arial', 14, 'bold'))
    button_left.goto(-150, 0)
    button_left.st()
# پنهان کردن دکمه ها
def hide_button():
    button_rt.ht()
    button_rt.clear()
    button_left.ht()
    button_left.clear()

# توابع تغییر رنگ لاک پشت با کیبرد
def next_color():
    global color_index
    color_index += 1
    if color_index == 10:
        color_index = 0
    Laki.color(AllColorLaki[color_index])
def previous_color():
    global color_index
    color_index -= 1
    if color_index == -1:
        color_index = 9
    Laki.color(AllColorLaki[color_index])
# توابع حرکتی با کیبرد
def move_rt():
    Laki.rt(30)
def move_left():
    Laki.left(30)
def move_fd():
    Laki.fd(10)
def move_bd():
    Laki.rt(180)

# تغییر صفحه بازی
def reset_game():
    global page_number
    if page_number == 1:
        draw_second_page()
        page_number = 2
    else:
        draw_first_page()
        page_number = 1

# شروع بازی
def setup_game_start():
    score = 0
    new_record.ht()
    cadr.clear()
    food.clear()
    game_screen.onkey(lambda: None, 'w')
    game_screen.onkey(lambda: None, 's')
    # چاپ زمان
    write_time.clear()
    write_time.write(f'زمان = {str(time_game)}', font = ('b koodak', 12, 'bold'))
    # چاپ امتياز
    write_score.clear()
    write_score.write(f'امتياز = {str(score)}', font = ('b koodak', 12, 'bold'))
    # رفتن غذا به يک مکان تصادفي
    food.goto(randint(-290, 290), randint(-290, 290))
    # چاپ (شما 60 ثانيه فرصت داريد)
    write_time_60.write('شما 60 ثانيه فرصت داريد', font = ('b koodak', 24, 'bold'))
    for _ in range(3, 0, -1):
        write_time_321.write(str(_), font = ('b koodak', 36, 'bold'))
        sleep(1)
        write_time_321.clear()
    write_time_60.clear()
    #توابع حرکتي با کيبرد 
    game_screen.onkey(move_rt, 'Right')
    game_screen.onkey(move_left, 'Left')
    game_screen.onkey(move_fd, 'Up')
    game_screen.onkey(move_bd, 'Down')
    game_laki()# شروع بازی
# تابع بازی
def game_laki():
    score = 0
    start = time()
    time_game2 = time() + 1
    while True:
        Laki.fd(1)
        # برخورد با ديوار
        if Laki.xcor() > 310 or Laki.xcor() < -310 or Laki.ycor() > 310 or Laki.ycor() < -310 :
            Laki.rt(180)
            Laki.fd(10)
            score += -5
            write_score.clear()
            write_score.write(f'امتياز = {str(score)}', font = ('b koodak', 12, 'bold'))
        # امتياز گرفتن
        if Laki.distance(food) < 20.0:
            time_now = time()
            food.goto(randint(-290, 290),randint(-290, 290))
            score += 10
            write_score.clear()
            write_score.write(f'امتياز = {str(score)}', font = ('b koodak', 12, 'bold'))
            # برنده شدن
            if score >= 100 :
                end_game(score, time_now, start)
                break
        # باختن
        if start + 60 < time():
            end_game(score, start+60, start, False)
            break
        # چاپ زمان
        if time() >= time_game2 :
            time_game2 += 1
            write_time.clear()
            write_time.write(f'زمان = {str(int(60 + start - time()))}', font = ('b koodak', 12, 'bold'))

# کادر پایان بازی
def end_game(score, time_now, start_game, game_result=True):
    # غیر فعال کردن توابع حرکتی
    for _ in ('Right', 'Left', 'Up', 'Down'):
        game_screen.onkey(lambda: None, _)
    
    print_cadr()
    Laki.seth(0)
    Laki.goto(0, -5)
    new_time = round(60 - time_now + start_game, 2)
    record = float (txt.read_from_file(address_record))
    # برد
    if game_result:
        # چاپ (شما برنده شدید) 
        food.goto(-125, -10)
        food.write('شما برنده شديد', font = ('b koodak', 36, 'bold'))
        # چاپ رکورد
        food.goto(-130, -90)
        if new_time > record :
            txt.write_to_file(address_record, new_time)
            new_record.st()
            food.write(f'رکورد = {str(new_time)}', font = ('b koodak', 16, 'bold'))
        else :
            food.write(f'رکورد = {str(record)}', font = ('b koodak', 16, 'bold'))
    # باخت
    else:
        # چاپ (شما باختید)
        food.goto(-100, -10)
        food.write('شما باختيد', font=('b koodak', 36, 'bold'))
        # چاپ رکورد
        food.goto(-130, -90)
        food.write(f'رکورد = {str(record)}', font = ('b koodak', 16, 'bold'))
    # چاپ زمان باقی مانده
    food.goto(-130, -60)
    food.write(f'زمان باقي مانده = {str(new_time)}', font = ('b koodak', 16, 'bold'))            # احتمال خطا
    # چاپ امتياز 
    food.goto(-130, -30)
    food.write(f'امتياز = {str(score)}', font = ('b koodak', 16, 'bold'))
    # چاپ دکمه (شروع مجدد)
    print_cadr_button()
    cadr.color('red')
    cadr.goto(-70, -135)
    cadr.write('(s)شروع مجدد', font = ('b koodak', 20, 'bold'))
    # فعال کردن دکمه ها
    game_screen.onkey(setup_game_start, 's')
    game_screen.onkey(reset_game, 'w')

def main():
    setup_screen()
    # ساختن لاک پشت ها
    create_turtles()
    create_cadr_screen()
    # کشیدن صفحه اول
    draw_first_page()
    # فعال سازی دکمه ها
    game_screen.listen()
    game_screen.onkey(reset_game, 'w')
    game_screen.onkey(game_screen.bye, 'b')
    turtle.done()

if __name__ == "__main__":
    main()