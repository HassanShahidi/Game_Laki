import time
import turtle
import random
import txt
time_game = 60
#طراحي صفحه بازي                            align('right')
s = turtle.Screen()
s.setup(700, 700)
s.title('Game Laki')
s.bgpic('PNG/back.gif')
t = turtle.Turtle()
t.ht()
t.width(4)
t.speed('fastest')
t.up()
t.goto(325, 325)
t.down()
for _ in range(4):
    t.rt(90)
    t.fd(650)
#طراحي شخصيت بازي
Laki = turtle.Turtle('turtle')
Laki.shapesize(2)
Laki.color('DarkGreen')
Laki.up()
#شخصيت رنگارنگ
'''ColorLakiDark=['Black','DarkGreen','MediumBlue','DarkSlateGray', 'Indigo', 'Maroon']

ColorLakiLight=['Lime', 'Magenta', 'Red', 'Aqua', 'Orange']        #Laki.gif
s.register_shape('Laki.gif')'''

#طراحي غذا و چاپ مقدار امتيازوزمان و شما برديدوباختيد
s.register_shape('PNG/ball.gif')
food = turtle.Turtle('PNG/ball.gif')
food.speed('fastest')
food.up()
food.color('Blue')
#چاپ شروع و شروع مجدد 3و2و1
timer = turtle.Turtle()
timer.ht()
timer.up()
timer.goto(-40, -135)
timer.color('Navy')
#چاپ (شما 60 ثانيه فرصت داريد)
tm = turtle.Turtle()
tm.ht()
tm.up()
tm.goto(-130, 70)
tm.color('Navy')
#چاپ زمان
tr = turtle.Turtle()
tr.ht()
tr.up()
tr.goto(275, 326)
tr.write('زمان ='+str(time_game), font = ('b koodak', 12, 'bold'))
#چاپ امتياز
wr = turtle.Turtle()
wr.ht()
wr.up()
wr.goto(-325, 326)
wr.color('Navy')
wr.write('امتياز =0', font = ('b koodak', 12, 'bold'))
#new_record
s.register_shape('PNG/new record.gif')
new_record = turtle.Turtle('PNG/new record.gif')
new_record.ht()
new_record.speed('fastest')
new_record.up()
new_record.goto(200, 200)
#توابع کادر
cadr = turtle.Turtle()
cadr.ht()
cadr.up()
cadr.speed('fastest')
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
#توابع حرکتي با کيبرد
def move_rt():
    Laki.rt(30)
def move_left():
    Laki.left(30)
def move_fd():
    Laki.fd(10)
def move_bd():
    Laki.rt(180)
s.listen()
#طراحي بازي
print_cadr_button(-50)
timer.color('red')
timer.write('(s)شروع', font = ('b koodak', 20, 'bold'))
def start_game_laki():
    #متغيرها
    score = 0
    address_record = 'record.txt'
    #پاک کردن نوشته ها
    new_record.ht()
    timer.clear()
    cadr.clear()
    food.clear()
    #چاپ امتياز
    wr.clear()
    wr.write('امتياز ='+str(score), font = ('b koodak', 12, 'bold'))
    #رفتن غذا به يک مکان تصادفي
    food.goto(random.randint(-290, 290),random.randint(-290, 290))
    #شروع بازي
    tm.write('شما 60 ثانيه فرصت داريد', font = ('b koodak', 24, 'bold'))
    timer.color('navy')
    timer.goto(-15, 10)
    timer.write('3', font = ('b koodak', 36, 'bold'))
    time.sleep(1)
    timer.clear()
    
    timer.write('2', font = ('b koodak', 36, 'bold'))
    time.sleep(1)
    timer.clear()
    
    timer.write('1', font = ('b koodak', 36, 'bold'))
    time.sleep(1)
    timer.clear()
    tm.clear()
    #توابع حرکتي با کيبرد 
    s.onkey(move_rt, 'Right')
    s.onkey(move_left, 'Left')
    s.onkey(move_fd, 'Up')
    s.onkey(move_bd, 'Down')
    start = time.time()
    time_game2 = time.time() + 1
    while True:
        Laki.fd(1)
        #برخورد با ديوار
        if Laki.xcor() > 310 or Laki.xcor() < -310 or Laki.ycor() > 310 or Laki.ycor() < -310 :
            Laki.rt(180)
            Laki.fd(10)
            score += -5
            wr.clear()
            wr.write('امتياز ='+str(score), font = ('b koodak', 12, 'bold'))
        #امتياز گرفتن
        if Laki.distance(food) < 20:
            food.goto(random.randint(-290, 290),random.randint(-290, 290))
            score += 10
            wr.clear()
            wr.write('امتياز ='+str(score), font = ('b koodak', 12, 'bold'))
            #برنده شدن 
            if score >= 100:                                                                                #100
                print_cadr()
                h = time.time()
                food.goto(-125, -10)
                food.write('شما برنده شديد', font = ('b koodak', 36, 'bold'))
                
                Laki.seth(0)
                Laki.goto(0,-5)
            
                new_time = round(60 -(h - start), 2)
                record = float (txt.print_txt(address_record))
                #ثبت رکورد 
                food.goto(-130, -90)
                if record < new_time :
                    txt.w(address_record, new_time)
                    new_record.st()
                
                    food.write('رکورد ='+str(new_time), font = ('b koodak', 16, 'bold'))
                else :
                    food.write('رکورد ='+str(record), font = ('b koodak', 16, 'bold'))
                #چاپ زمان باقي مانده 
                food.goto(-130, -60)
                food.write('زمان باقي مانده ='+str(new_time), font = ('b koodak', 16, 'bold'))
                #چاپ امتياز 
                food.goto(-130, -30)
                food.write('امتياز ='+str(score), font = ('b koodak', 16, 'bold'))
                #شروع مجدد
                print_cadr_button()
                timer.color('red')
                timer.goto(-70, -135)
                timer.write('(s)شروع مجدد', font = ('b koodak', 20, 'bold'))
                break
        #باختن 
        if start + 60 < time.time():                                           #60
            print_cadr()
            record = open (address_record, 'r')
            food.goto(-100, -10)
            food.write('شما باختيد', font=('b koodak', 36, 'bold'))
            #چاپ رکورد
            food.goto(-130, -90)
            food.write('رکورد ='+record.read(), font = ('b koodak', 16, 'bold'))
            #چاپ زمان باقي مانده 
            food.goto(-130, -60)
            food.write('زمان باقي مانده ='+'0', font = ('b koodak', 16, 'bold'))
            #چاپ امتياز 
            food.goto(-130, -30)
            food.write('امتياز ='+str(score), font = ('b koodak', 16, 'bold'))
            
            Laki.seth(0)
            Laki.goto(0,-5)
            #شروع مجدد
            print_cadr_button()
            timer.color('red')
            timer.goto(-70, -135)
            timer.write('(s)شروع مجدد', font = ('b koodak', 20, 'bold'))
            break
        if time.time() >= time_game2 :#چاپ زمان
            time_game2 = time_game2 + 1
            tr.clear()
            tr.write('زمان ='+str(round(60 -(time.time() - start))), font = ('b koodak', 12, 'bold'))

s.onkey(start_game_laki, 's')
s.onkey(s.bye, 'b')
turtle.done()
