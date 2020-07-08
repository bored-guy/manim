from manimlib.imports import *
import math
import random
'''对于代码的说明
get_flag函数是获得美国国旗
下面的一些奇奇怪怪的动画是有关于圆的性质的
于这个视频无关（本来是做着玩的，不舍得删）
part1是第一部分
zoom是将部分放大
explain是解释
experiment是实验
最后的3个figure是实验1w，2w，5w次的
由于次数过多，最后生成的是图像（但5w还是渲染了1个多小时）
end是片尾
有意见，疑惑，欢迎加QQ号交流2232652509
祝各位好运！'''
def get_flag():
    value = 8 / 13
    dot_group1 = []
    dot_group2 = []
    for i in range(0,15):
        point1 = np.array([-7, 4-i * value, 0])
        dot_group1.append(point1)
    for i in range(0,15):
        point1 = np.array([7, 4-i * value, 0])
        dot_group2.append(point1)
    polygroup1 = VGroup()
    for i in range(0, 13):
        poly1 = Polygon(dot_group1[i], dot_group1[i + 1], dot_group2[i + 1], dot_group2[i]).set_stroke(color=WHITE)
        if i % 2 == 1:
            poly1.set_fill(color=WHITE, opacity=1)
        else:
            poly1.set_fill(color=RED, opacity=1)
        polygroup1.add(poly1)
    poly2 = Polygon(np.array([-7,4, 0]), np.array([0, 4, 0]), np.array([0, 4-value *7, 0]),
                    np.array([-7, 4-value * 7, 0])).set_color(BLUE_E).set_fill(opacity=1)
    newvalue = value * 7 / 9
    poly3 = RegularPolygon(5)
    point = poly3.get_vertices()
    star = Polygon(point[0], point[2], point[-1], point[1], point[3]).set_fill(opacity=1, color=WHITE) \
        .set_stroke(color=WHITE).move_to(np.array([-7, 4, 0])).scale(0.2).shift(
        DOWN * 0.2 + RIGHT * 0.2)
    stargroup1 = VGroup(star)
    stargroup2 = VGroup()
    for i in range(1, 6):
        newstar = star.copy().shift(RIGHT * 1.25 * i)
        stargroup1.add(newstar)
    for i in range(0, 5):
        newstar = star.copy().shift(RIGHT * 1.25* i + DOWN * newvalue + RIGHT * 0.7)
        stargroup2.add(newstar)
    stargroup = VGroup(stargroup1, stargroup2)
    for i in range(2, 9):
        if i % 2 == 0:
            stargroupi = stargroup1.copy().shift(DOWN * newvalue * i)
            stargroup.add(stargroupi)
        else:
            stargroupi = stargroup2.copy().shift(DOWN * newvalue * (i - 1))
            stargroup.add(stargroupi)
    flag = VGroup(polygroup1, poly2, stargroup)
    return flag
class DrawCircle1(Scene):
    def construct(self):
        dotA = Dot().set_color(YELLOW)
        self.play(FadeIn(dotA))
        dotB = Dot().move_to(np.array([2,0,0])).set_color(BLUE)
        value = ValueTracker(0.5*PI)
        dotB.add_updater(lambda a: a.become(
            Dot().set_color(BLUE).move_to(np.array(
                [2*math.sin(value.get_value()),2*math.cos(value.get_value()),0]
            ))
        ))
        lineA = Line(dotA,dotB).set_color(RED)
        lineA.add_updater(lambda a: a.become(
            Line(dotA,np.array(
                [2*math.sin(value.get_value()),2*math.cos(value.get_value()),0]
            )).set_color(GOLD_C)
        ))
        circle = Circle(radius=2).set_color(BLUE)
        self.add(lineA)
        self.add(dotB)
        self.play(ApplyMethod(value.set_value,-1.5*PI),ShowCreation(circle),
                  run_time=5, rate_func=linear)
        self.wait()
class DrawCircle2(Scene):
    def construct(self):
        dotA = Dot().set_color(YELLOW)
        self.play(FadeIn(dotA))

        for i in range(0,20):
            value=TAU*random.random()
            doti=Dot().move_to(np.array([2*math.sin(value),2*math.cos(value),0])).set_color(BLUE)
            self.play(FadeIn(doti),run_time=0.1)
        for i in range(0,8):
            value=random.random()
            doti=Dot().move_to(np.array([2*math.sin(value),2*math.cos(value),0])).set_color(BLUE)
            self.play(FadeIn(doti),run_time=0.1)
        for i in range(0,20):
            value=TAU*random.random()
            doti=Dot().move_to(np.array([2*math.sin(value),2*math.cos(value),0])).set_color(BLUE)
            self.play(FadeIn(doti),run_time=0.07)
        circ=Circle(radius=2,stroke_width=10).set_color(BLUE_D)
        self.play(ShowCreation(circ),run_time=2)
        self.wait()
class duichenzhou(Scene):
    def construct(self):
        textA=TextMobject('圆有无数条对称轴。').set_color(YELLOW).shift(UP*3.4)
        circ = Circle(radius=2).set_color(BLUE_D)
        self.add(circ)
        self.play(Write(textA),run_time=2)
        for i in range(0,11):
            dotA=Dot().move_to(np.array([3*math.sin(i*TAU/12),3*math.cos(i*TAU/12),0]))
            dotB = Dot().move_to(np.array([-3 * math.sin(i*TAU/12), -3 * math.cos(i*TAU/12), 0]))
            dash_line=DashedLine(dotA,dotB).set_color(GREEN)
            self.play(ShowCreation(dash_line),run_time=0.8)
        self.wait()
class gongyuandingli(Scene):
    def construct(self):
        circ=Circle(radius=2).set_color(BLUE_D)
        self.add(circ)
        group1=VGroup()
        alphalist1=['A','B','C']
        for i in range(0, 3):
            value = TAU * random.random()
            doti = Dot().move_to(np.array([2 * math.sin(value), 2 * math.cos(value), 0])).set_color(YELLOW)
            tex=TexMobject(alphalist1[i]).next_to(doti,buff=0.1).set_color(RED).scale(0.8)
            group1.add(doti)
            self.play(FadeIn(doti),FadeIn(tex),run_time=0.8)
        list1=[(0,1),(1,2),(0,2)]
        for i in range(0,3):
            line = Line(group1[list1[i][0]],group1[list1[i][1]]).set_color(GOLD_D)
            self.play(ShowCreation(line),run_time=0.8)
        group2=VGroup()
        alphalist2 = ['D', 'E', 'F']
        for i in range(0, 3):
            value = 1.4*PI * random.random()
            doti = Dot().move_to(np.array([2 * math.sin(value), 2 * math.cos(value), 0])).set_color(YELLOW)
            tex = TexMobject(alphalist2[i]).next_to(doti, buff=0.1).set_color(RED).scale(0.8)
            group2.add(doti)
            self.play(FadeIn(doti), FadeIn(tex), run_time=0.8)
        for i in range(0, 3):
            line = Line(group2[list1[i][0]], group2[list1[i][1]]).set_color(GOLD_D)
            self.play(ShowCreation(line),run_time=0.8)
        text=TexMobject(r'\frac{S\triangle ABC}{S\triangle DEF}=\frac{AB\times BC \times AC}{DE \times EF \times DF}').shift(DOWN*3.2).set_color(GREEN)
        self.play(Write(text))
        self.wait()
class MengRiDingLi(Scene):
    def construct(self):
        circ1=Circle(radius=3).set_color(BLUE)
        circ2=Circle(radius=math.sqrt(6.6)).move_to(np.array([3.97,1.58,0])).set_color(YELLOW)
        circ3 = Circle(radius=math.sqrt(3.6)).move_to(np.array([1.2, 3.37, 0])).set_color(GREEN)
        circ_group=VGroup(circ1,circ2,circ3)
        dot1=Dot().move_to(np.array([2.35,1.87,0]))
        dot2 = Dot().move_to(np.array([-0.65, 2.93, 0]))
        line1=Line(dot1,dot2)
        dot3 = Dot().move_to(np.array([1.59, 2.54, 0]))
        dot4 = Dot().move_to(np.array([2.9, -0.76, 0]))
        line2 = Line(dot3, dot4)
        dot5 = Dot().move_to(np.array([1.41, 1.49, 0]))
        dot6 = Dot().move_to(np.array([3, 3.96, 0]))
        line3 = Line(dot5, dot6)
        dot_group=VGroup(dot1,dot2,dot3,dot4,dot5,dot6).set_color(RED)
        line_group=VGroup(line1,line2,line3).set_color(RED)

        point=Dot().move_to(np.array([1.78,2.07,0])).set_color(PINK).scale(2)
        all_group = VGroup(dot_group, circ_group, line_group, point).scale(0.7).shift(DOWN + LEFT * 2)
        self.play(ShowCreation(circ_group),run_time=2,rate_func=linear)

        self.play(ShowCreation(line_group),run_time=2,rate_func=linear)
        self.play(FadeIn(point),run_time=1)
        text=TextMobject('三个不同心且相交的圆，形成三条根轴，必交于一点').set_color(GOLD).shift(DOWN*3.5)
        self.play(Write(text))
        self.wait()
class TuoLeMi(Scene):
    def construct(self):
        circ=Circle(radius=3).set_color(BLUE)
        dotA=Dot().move_to(np.array([0,3,0]))
        dotB = Dot().move_to(np.array([2.94, 0.57, 0]))
        dotC = Dot().move_to(np.array([1.48, -2.61, 0]))
        dotD = Dot().move_to(np.array([-1.78, -2.42, 0]))
        texA=TexMobject('A').next_to(dotA,buff=SMALL_BUFF)
        texB = TexMobject('B').next_to(dotB, buff=SMALL_BUFF)
        texC = TexMobject('C').next_to(dotC, buff=SMALL_BUFF)
        texD = TexMobject('D').next_to(dotD, buff=SMALL_BUFF)
        dotgroup=VGroup(dotA,dotB,dotC,dotD).set_color(YELLOW)
        texgroup=VGroup(texA,texB,texC,texD).set_color(YELLOW)
        dotlist=[(0,1),(1,2),(2,3),(0,3),(0,2),(1,3)]
        linegroup=VGroup()
        for i in dotlist:
            line=Line(dotgroup[i[0]],dotgroup[i[1]]).set_color(GOLD)
            linegroup.add(line)
        self.play(ShowCreation(circ))
        self.play(FadeIn(dotgroup),FadeIn(texgroup))
        self.play(ShowCreation(linegroup),run_time=3)
        tex=TexMobject(r'AC\times BD=AB\times CD+AD\times BC').set_color(GREEN).shift(DOWN*3.5)

        value=ValueTracker(0)
        dotA.add_updater(lambda a: a.become(
            Dot().set_color(BLUE).move_to(np.array(
                [3*math.sin(value.get_value()),3*math.cos(value.get_value()),0]
            ))
        ))
        texA.add_updater(lambda a : a.next_to(dotA,buff=SMALL_BUFF))
        linegroup[0].add_updater(lambda a : a.become(Line(dotA,dotB).set_color(GOLD)))
        linegroup[3].add_updater(lambda a: a.become(Line(dotA, dotD).set_color(GOLD)))
        linegroup[4].add_updater(lambda a: a.become(Line(dotA, dotC).set_color(GOLD)))
        self.play(Write(tex),value.set_value,-1.8,run_time=5,rate_func=linear)
        self.wait()
class YuanZhouJiao(Scene):
    def construct(self):
        circ=Circle(radius=3).set_color(BLUE)
        dotA = Dot().move_to(np.array([1.22, 2.74, 0])).set_color(GREEN)
        texA=TexMobject('A').set_color(GREEN).next_to(dotA)
        dotB = Dot().move_to(np.array([1.48, -2.61, 0])).set_color(GREEN)
        texB = TexMobject('B').set_color(GREEN).next_to(dotB)
        dotC = Dot().move_to(np.array([-1.78, -2.42, 0])).set_color(GREEN)
        texC = TexMobject('C').set_color(GREEN).next_to(dotC)
        self.play(ShowCreation(circ))
        self.play(FadeIn(dotA),FadeIn(dotB),FadeIn(dotC),FadeIn(texA),FadeIn(texB),FadeIn(texC))
        Line1=Line(dotA,dotB).set_color(YELLOW)
        Line2 = Line(dotA, dotC).set_color(YELLOW)
        self.play(ShowCreation(Line1))
        self.play(ShowCreation(Line2))
        value=ValueTracker(0)
        dotD=Dot().move_to(np.array([0,3,0]))
        texD=TexMobject('D').set_color(GREEN).next_to(dotC)
        texD.add_updater(lambda a: a.next_to(dotD))
        dotD.add_updater(lambda a: a.become(
            Dot().set_color(GREEN).move_to(np.array(
                [3*math.sin(value.get_value()),3*math.cos(value.get_value()),0]
            ))
        ))
        Line3=Line(dotD,dotB).set_color(YELLOW)
        Line4=Line(dotD,dotC).set_color(YELLOW)
        Line3.add_updater(lambda a: a.become(Line(dotD,dotB)).set_color(YELLOW))
        Line4.add_updater(lambda a: a.become(Line(dotD, dotC)).set_color(YELLOW))
        tex=TexMobject(r'\angle CAB=\angle CDB').set_color(GOLD).to_edge(DOWN)
        self.play(FadeIn((VGroup(dotD,Line3,Line4,texD))))
        self.play(Write(tex))
        self.play(value.set_value,-2,run_time=4)
        self.wait()
class part1(ThreeDScene):
    def construct(self):
        texlist=[r'$\pi$这个神奇的常数藏在数学中的各个角落',
                 '许多与圆毫不相干的问题中也常有$\pi$的身影',
                 '比如布丰投针问题',
                 '向条格纸(美国国旗)上随机扔细针','二倍的针长除以条格间距','再除以$\pi$就是针与条格相交概率']
        text1=TextMobject(texlist[0]).set_color(YELLOW).to_edge(UL)
        self.play(Write(text1))
        text2=TextMobject(texlist[1]).set_color(YELLOW).to_edge(UL).shift(DOWN)
        self.play(Write(text2))
        image1=ImageMobject(r'C:\Users\22326\Pictures\image\pi.png').to_corner(UR)
        self.play(FadeIn(image1))
        arrow1=Arrow().rotate(PI/2).scale(0.8).next_to(image1,DOWN,buff=0.1).set_color(ORANGE)
        text1_5=TextMobject('哪里都有它').scale(0.8).next_to(arrow1,DOWN).set_color(ORANGE)
        self.play(FadeIn(VGroup(arrow1,text1_5),FadeIn(image1)))
        self.wait(0.8)
        self.play(FadeOut(VGroup(arrow1,text1_5)),FadeOut(image1),run_time=0.8)
        text3=TextMobject(texlist[2]).set_color(BLUE).to_edge(UL)
        text4 = TextMobject(texlist[3]).set_color(BLUE).to_edge(UL).shift(DOWN)
        self.play(Uncreate(text1),Uncreate(text2),run_time=1.2)
        self.play(Write(text3))
        self.play(Write(text4))
        flag=get_flag().scale(0.6).to_edge(DOWN)
        self.play(FadeIn(flag))
        self.move_camera(phi=60*DEGREES)
        self.play(FadeOut(text3),FadeOut(text4))
        text5=TextMobject(texlist[4]).to_edge(UL).set_color(BLUE)
        text6=TextMobject(texlist[5]).to_edge(UL).shift(DOWN).set_color(BLUE)
        self.pin(5)
        self.add_fixed_in_frame_mobjects(text5)
        self.wait(2)
        self.add_fixed_in_frame_mobjects(text6)
        self.wait(2)
        self.move_camera(phi=0)
        self.play(FadeOut(VGroup(text5,text6)))
        self.wait(2)
    def pin(self,time):
        values = 7 / 13
        n = time
        linegroup = VGroup()
        while n > 0:
            value = ValueTracker()
            x = random.uniform(-1,3)
            y = random.uniform(-3, 1)
            z = random.uniform(-PI / 2, PI / 2)
            a = 15
            x_1 = x + 0.5 * math.cos(z)
            y_1 = y + 0.5 * math.sin(z)
            line = Line(np.array([x, y, 3]), np.array([x_1, y_1, 3])).set_color(BLUE)
            line.add_updater(lambda thing: thing.become(
                Line(np.array([x, y, 3 - ((value.get_value()) ** 2) * 0.5 * a]),
                     np.array([x_1, y_1, 3 - ((value.get_value()) ** 2) * 0.5 * a])
                     ).set_color(BLUE)))
            self.play(FadeIn(line), run_time=0.3)
            self.play(value.set_value, math.sqrt(6 / a), rate_func=linear, run_time=1.2)
            n -= 1
            line.clear_updaters(recursive=True)
            linegroup.add(line)


class zoom(ZoomedScene):
    CONFIG = {
        "zoomed_display_height": 9,
        "zoomed_display_width": 15,
        "zoomed_display_center":ORIGIN,
        "zoom_factor": 0.23,
        "zoom_activated": False,
        "zoomed_camera_frame_starting_position": ORIGIN+DOWN*2,
    }
    def construct(self):
        flag=get_flag().scale(0.7).to_edge(DOWN)
        self.add(flag)
        self.activate_zooming(animate=True)
        self.wait()
class explain(Scene):

    def construct(self):
        background=ImageMobject(r'C:\Users\22326\STEM\myprogramme\PycharmProject\newmanim\manim-master\media\videos\pi\images\zoom.png').scale(4)
        self.add(background)
        text1=TextMobject('那么让我们看看这里为什么会出现$\pi$').set_color(BLUE).to_edge(DOWN)
        arrow = Arrow().rotate(PI * 13.5/ 8).scale(0.5).next_to(text1, UL).set_color(PINK)
        text1_5=TextMobject('看这儿').next_to(arrow, UL,buff=0.2).set_color(PINK)
        group1=VGroup(text1_5,arrow)
        self.play(FadeIn(group1),run_time=0.5)
        self.play(Indicate(group1))
        self.play(FadeOut(group1,run_time=0.5))
        self.play(Write(text1))
        self.wait(1)
        pin=Line().rotate(PI/2).set_color(PINK)
        text2=TextMobject('这是一根针').set_color(BLUE).to_edge(DOWN)
        self.play(ReplacementTransform(text1,text2),FadeIn(pin))
        text3=TextMobject('无论他的长度是多少').set_color(BLUE).to_edge(DOWN)
        self.wait(1)
        self.play(ReplacementTransform(text2,text3),pin.set_height,4)
        self.play(pin.set_height,2)
        text4=TextMobject('他与这些平行线的交点都可以理解为','随机变量').to_edge(DOWN).set_color(BLUE)
        text4[1].scale(1.1).shift(RIGHT*0.1).set_color(YELLOW)
        self.play(ReplacementTransform(text3,text4))
        text4_5 = TextMobject('不妨叫他','$X_1$').to_edge(UL).set_color(YELLOW)
        self.play(Write(text4_5))
        text4_7=TextMobject('不要害怕，他很简单').to_edge(UR).set_color(YELLOW)
        text4_8 = TextMobject('不会唤起你被统计支配的恐惧').to_edge(UR).set_color(YELLOW).shift(DOWN)
        self.add(text4_7,text4_8)
        self.wait(3)
        self.remove(text4_7,text4_8)
        text5=TextMobject('比如这一根针，他与平行线的交点可能是一个两个或没有').to_edge(DOWN).set_color(BLUE).scale(0.8)
        self.wait(2)
        self.play(Transform(text4,text5),FadeOut(text4_5[0]))
        self.play(text4_5[1].to_edge,UL)
        dot1=Dot().set_color(BLUE)
        tex6 = TexMobject(r'X_{1}=1').to_edge(UL).set_color(YELLOW)
        self.play(FadeIn(dot1),ReplacementTransform(text4_5[1],tex6),FadeOut(text4))
        self.play(FadeOut(dot1))
        self.play(pin.shift,UP*0.8)
        dot2=Dot().set_color(BLUE)
        dot3=Dot().shift(UP*1.6).set_color(BLUE)
        tex7=TexMobject(r'X_{1}=2').to_edge(UL).set_color(YELLOW)
        self.play(FadeIn(VGroup(dot2,dot3)),ReplacementTransform(tex6,tex7))
        self.play(FadeOut(VGroup(dot2,dot3)))
        self.play(pin.rotate,PI/2)
        tex8=TexMobject(r'X_{1}','=0').to_edge(UL).set_color(YELLOW)
        self.play(ReplacementTransform(tex7,tex8))
        self.wait(2)
        text9=TextMobject('我们考虑这个随机变量的期望值').set_color(BLUE).to_edge(DOWN)
        tex10=TexMobject('E(X_1)').to_edge(UL).set_color(YELLOW)
        self.play(Write(text9),FadeOut(tex8[1]))
        self.play(ReplacementTransform(tex8[0],tex10))
        text11=TextMobject('不妨设针与平行线有n个交点的概率是$p_{n}$').set_color(BLUE).to_edge(DOWN)
        self.play(ReplacementTransform(text9,text11))
        text12=TextMobject('那么我们就可以得到期望值的公式').set_color(BLUE).to_edge(DOWN)
        self.wait(1.5)
        tex13=TexMobject(r'E(X_1)=',r'p_0 \times 0+',r'p_1 ',r'\times 1+','p_2',r'\times 2 ',r'\cdots').to_edge(UL).set_color(YELLOW)
        self.play(ReplacementTransform(text11,text12),ReplacementTransform(tex10,tex13))
        self.wait(2)
        text13_5=TextMobject('显然，期望值与针的长度有关').set_color(BLUE).to_edge(DOWN)
        text14=TextMobject('而布丰投针问题要求针长小于平行线间距').set_color(BLUE).to_edge(DOWN)
        self.play(Transform(text12,text13_5))
        self.wait(2)
        self.play(ReplacementTransform(text12,text14))
        self.play(pin.rotate,PI/2,pin.set_height,1)
        self.wait(1.2)
        text15=TextMobject('即针只可能与直线有一个或两个交点').set_color(BLUE).to_edge(DOWN)
        self.play(ReplacementTransform(text14,text15))
        self.wait(0.8)
        self.play(Transform(tex13[4],TexMobject('0').to_edge(UL).set_color(YELLOW).shift(RIGHT*6.4)))
        self.wait(0.8)
        self.play(FadeOut(VGroup(tex13[1],tex13[3],tex13[4:])))
        self.wait(0.8)
        self.play(tex13[2].shift,LEFT*2.1)
        text16=TextMobject('而我们要求的概率$p_1$也就是$E(x_1)$').set_color(BLUE).to_edge(DOWN)
        self.play(ReplacementTransform(text15,text16))
        self.wait(2)
        text17=TextMobject('现在，我再拿出一根一模一样的针').set_color(BLUE).to_edge(DOWN)
        pin2=Line().shift(RIGHT*2).set_color(BLUE).rotate(PI/4).set_height(1)
        self.play(ReplacementTransform(text16,text17),FadeIn(pin2))
        self.wait(1.8)
        text18=TextMobject('他与平行线的交点也是随机变量').set_color(BLUE).to_edge(DOWN)
        text19=TextMobject('不妨叫他','$X_2$').to_edge(UL).set_color(YELLOW).shift(DOWN)
        self.play(ReplacementTransform(text17,text18),Write(text19))
        text20=TextMobject('因为完全相同，所以$X_2$的期望值和$X_1$相同').set_color(BLUE).to_edge(DOWN)
        tex21=TexMobject('=E(X_2)').set_color(YELLOW).next_to(tex13[2],buff=SMALL_BUFF)
        self.wait(2)
        self.play(ReplacementTransform(text18,text20),FadeOut(text19[0]),ReplacementTransform(text19[1],tex21))
        self.wait(2)
        text22=TextMobject('现在我们将这两个针焊在一起').set_color(BLUE).to_edge(DOWN)
        self.play(ReplacementTransform(text20,text22),pin2.shift,UP*0.75+LEFT*1.5)
        dot4=Dot().shift(UP*0.2)
        self.play(FadeIn(dot4))
        self.play(Flash(dot4),FadeOut(dot4))
        text23=TextMobject('这一个整体与平行线的交点，应该等于$X_1+X_2$').set_color(BLUE).to_edge(DOWN)
        self.play(ReplacementTransform(text22,text23))
        tex24=TexMobject('X_{1,2}=X_1+X_2').to_edge(UL).set_color(YELLOW).shift(DOWN)
        self.play(Write(tex24))
        self.wait(0.8)
        text25=TextMobject('这样我们就可以求得这一整体与平行线相交的期望值').set_color(BLUE).to_edge(DOWN)
        tex26 = TexMobject('E(X_{1,2})=','E(X_1)','+','E(X_2)').to_edge(UL).set_color(YELLOW).shift(DOWN)
        tex27=TexMobject('E(X_1)').to_edge(UL).set_color(YELLOW).shift(DOWN).shift(RIGHT*4.8)
        self.play(ReplacementTransform(text23,text25),ReplacementTransform(tex24,tex26))
        self.wait(0.8)
        self.play(Transform(tex26[3],tex27))
        self.wait(1)
        tex28=TexMobject('2E(X_1)').set_color(YELLOW).next_to(tex26[0],RIGHT,buff=SMALL_BUFF)
        self.play(Transform(tex26[1:],tex28))
        text29=TextMobject('我们知道这个期望值是与针的长度有关的').set_color(BLUE).to_edge(DOWN)
        self.play(ReplacementTransform(text25,text29))
        text30 = TextMobject('而当长度增加二倍时，期望值也增加二倍').set_color(BLUE).to_edge(DOWN)
        self.wait(2)
        tex30=TexMobject('L_{1,2}=2L_1').to_edge(UL).set_color(YELLOW).shift(DOWN*2)
        self.play(ReplacementTransform(text29,text30),Write(tex30))
        text31=TextMobject('这也就意味着，针与平行线交点个数的期望值与针长成正比').set_color(BLUE).to_edge(DOWN)
        self.wait(2)
        self.play(ReplacementTransform(text30,text31))
        self.wait(0.8)
        ULGROUP=VGroup(tex13[0],tex13[2],tex21,tex26,tex30)
        tex32=TexMobject('E(X)','=','n','L').to_edge(UL).set_color(YELLOW)
        self.play(ReplacementTransform(ULGROUP,tex32))
        self.play(FadeOut(VGroup(pin,pin2)))
        text33=TextMobject('目前为止我们讨论的还是直线或折线').set_color(BLUE).to_edge(DOWN)
        self.wait(1.5)
        self.play(ReplacementTransform(text31,text33))
        text34=TextMobject('而曲线可以将它理解为一段段折线拼接起来形成的').set_color(BLUE).to_edge(DOWN)
        self.wait(2.2)
        arc=Arc(start_angle=PI*9/10,angle=PI*12/10,radius=2.5).set_color(BLUE)
        self.play(ReplacementTransform(text33,text34),ShowCreation(arc))
        dotlist=[]
        for i in range(0,7):
            dot=np.array([2.5*math.cos(PI*9/10+PI*i*2/10),2.5*math.sin(PI*9/10+PI*2*i/10),0])
            dotlist.append(dot)
        linegroup=VGroup()
        for i in range(0,6):
            line=Line(dotlist[i],dotlist[i+1]).set_color(YELLOW)
            linegroup.add(line)
        self.play(ShowCreation(linegroup))
        dotlist2 = []
        for i in range(0, 13):
            dot = np.array(
                [2.5 * math.cos(PI * 9 / 10 + PI * i / 10), 2.5 * math.sin(PI * 9 / 10 + PI * i / 10), 0])
            dotlist2.append(dot)
        linegroup2 = VGroup()
        for i in range(0, 12):
            line = Line(dotlist2[i], dotlist2[i + 1]).set_color(YELLOW)
            linegroup2.add(line)
        self.wait(1.2)
        self.play(ReplacementTransform(linegroup,linegroup2))
        text35=TextMobject('只要分割的足够多，曲线的长度就会和折线相等').set_color(BLUE).to_edge(DOWN)
        self.play(ReplacementTransform(text34,text35))
        self.wait(2)
        text36=TextMobject('这样对于任意曲线都有期望值与长度成正比').set_color(BLUE).to_edge(DOWN)
        self.play(ReplacementTransform(text35,text36))
        self.wait(2)
        text37=TextMobject('现在我们求出这个比值n就ok了').set_color(BLUE).to_edge(DOWN)
        self.play(ReplacementTransform(text36,text37))
        self.wait(2)
        text38=TextMobject('我们需要找到一个曲线，无论怎么扔他与平行线的交点都是固定值').set_color(BLUE).to_edge(DOWN).scale(0.8)
        self.play(ReplacementTransform(text37,text38))
        self.wait(2.5)
        text39=TextMobject('这样他的期望值就是这个定值').set_color(BLUE).to_edge(DOWN)
        self.play(ReplacementTransform(text38, text39))
        self.wait(1.5)
        text40 = TextMobject('首先他不能是特别扁的长方形').set_color(BLUE).to_edge(DOWN)
        self.wait(2)
        rect=Rectangle(height=4,width=1).set_color(BLUE)
        self.play(ReplacementTransform(text39, text40),ReplacementTransform(VGroup(arc,linegroup2),rect))
        self.wait(1.8)
        text41=TextMobject('否则，旋转一圈后，交点数就会改变').set_color(BLUE).to_edge(DOWN)
        self.play(rect.rotate, PI / 2,ReplacementTransform(text40, text41))
        self.wait(2)
        text42=TextMobject('这说明该曲线应该更接近于正方形').set_color(BLUE).to_edge(DOWN)
        square=RegularPolygon(4).scale(0.86).shift(DOWN*0.72)
        self.play(ReplacementTransform(rect,square),ReplacementTransform(text41, text42))
        self.wait(1)
        self.play(square.shift,DOWN*0.8)
        text43=TextMobject('正方形上下移动时，交点数仍为两个').set_color(BLUE).to_edge(DOWN)
        self.play(ReplacementTransform(text42,text43),square.shift,UP*0.8)
        self.wait(2)
        text44=TextMobject('但是他旋转一点交点数，就会改变').set_color(BLUE).to_edge(DOWN)
        self.play(ReplacementTransform(text43, text44), square.rotate, PI/4)
        self.wait(2)
        text45=TextMobject('那么，什么图形旋转不会改变呢').set_color(BLUE).to_edge(DOWN)
        circ=Circle(radius=0.85).set_color(BLUE).shift(DOWN*0.6)
        self.wait(2)
        self.play(ReplacementTransform(text44, text45),ReplacementTransform(square, circ))
        text46=TextMobject('这个圆无论平移旋转与平行线的交点都是2个').set_color(BLUE).to_edge(DOWN)
        self.play(ReplacementTransform(text45, text46),  circ.shift,DOWN*1)
        self.play(circ.shift,UP*1.2,run_time=1.5)
        text47=TextMobject('虽然你看不出来，但他确实在转圈').scale(0.7).next_to(circ,LEFT,buff=SMALL_BUFF).set_color(BLUE)
        self.add(text47)
        self.play(circ.rotate,PI*2)
        self.remove(text47)
        text48=TextMobject('那么这个圆就是我们所要的图形').set_color(BLUE).to_edge(DOWN)
        self.play(ReplacementTransform(text46, text48))
        self.wait(2)
        self.play(circ.shift,DOWN*0.34)
        text49=TexMobject('d').set_color(BLUE)
        arrow2=Arrow().rotate(PI/2).scale(0.5).next_to(text49,UP,buff=0).set_color(BLUE)
        arrow3 = Arrow().rotate(PI*3/2).scale(0.5).next_to(arrow2,DOWN,buff=0).set_color(BLUE)
        lgroup=VGroup(text49,arrow2,arrow3).shift(DOWN*0.94+RIGHT*2).scale(1.1)
        text49.shift(RIGHT*0.2)

        self.wait(1)
        text50=TextMobject('那么这个圆与平行线交点的期望值就是2').set_color(BLUE).to_edge(DOWN)
        self.play(ReplacementTransform(text48,text50))
        tex51=TexMobject('E(X)=2').to_edge(UL).set_color(YELLOW).shift(DOWN)
        self.play(Write(tex51))
        self.wait(1.8)
        self.play(FadeIn(lgroup))
        text52 = TextMobject(r'这个圆的周长是$\pi \times d$').set_color(BLUE).to_edge(DOWN)
        self.play(ReplacementTransform(text50, text52))
        tex53=TexMobject(r'L=\pi d').to_edge(UL).set_color(YELLOW).shift(DOWN*2)
        self.play(Write(tex53))
        self.wait(1)
        tex54=TexMobject('2').to_edge(UL).set_color(YELLOW)
        tex55=TexMobject(r'\pi d').next_to(tex32[2]).set_color(YELLOW)
        self.play(Transform(tex32[0],tex54),FadeOut(tex51))
        self.wait(0.5)
        self.play(Transform(tex32[3],tex55),FadeOut(tex53))
        self.wait(1)
        tex56=TexMobject('2=n \pi d').to_edge(UL).set_color(YELLOW)
        self.play(ReplacementTransform(tex32,tex56))
        self.wait(1)
        tex57=TexMobject(r'n=\frac{2}{\pi d}').to_edge(UL).set_color(YELLOW)
        self.play(ReplacementTransform(tex56, tex57))
        self.wait(1)
        text58=TextMobject('求出了n我们就快完事了').set_color(BLUE).to_edge(DOWN)
        self.play(ReplacementTransform(text52,text58))
        self.wait(1.5)
        text59=TextMobject('翻出那个我们一开始就推出的公式').set_color(BLUE).to_edge(DOWN)
        self.play(ReplacementTransform(text58, text59))
        tex60=TexMobject('E(X)=p_1').set_color(YELLOW)
        self.wait(2)
        text61=TextMobject('对于短针，他与平行线相交的概率等于他的期望值').scale(0.8).set_color(BLUE).to_edge(DOWN)
        self.play(ReplacementTransform(text59, text61),ReplacementTransform(VGroup(circ,lgroup), tex60))
        self.wait(1)
        self.play(tex57.next_to,tex60,DOWN)
        tex62=TexMobject('E(X)','=','n','L').next_to(tex57,DOWN).set_color(YELLOW)
        self.play(Write(tex62),run_time=1)
        self.wait(2)
        tex63=TexMobject(r'p_1=E(x)=nL=\frac{2L}{\pi d}').set_color(YELLOW)
        self.play(ReplacementTransform(VGroup(tex60,tex62,tex57),tex63))
        self.wait(0.8)
        self.play(FocusOn(tex63))
        self.play(Indicate(tex63))
        tex64=TexMobject('Bingo!').set_color(BLUE).to_edge(DOWN)
        self.play(ReplacementTransform(text61, tex64))
        self.wait(2)





class experiment(ThreeDScene):
    def construct(self):
        text=TextMobject('在视频的最后，让我们用实验证明一下他').set_color(PINK)
        self.play(Write(text))
        text2=TextMobject('这是一面美国国旗').set_color(PINK).shift(DOWN)
        self.wait(0.8)
        self.play(Write(text2))
        self.wait(0.8)
        flag=get_flag().scale(0.8).to_edge(UP)
        self.play(ReplacementTransform(VGroup(text,text2),flag))
        self.move_camera(phi=50 * DEGREES)
        self.wait(1)
        text3=TextMobject('扔到星星区域的假装没有星星,就当条格隐藏了起来').set_color(YELLOW).to_edge(UL)
        text4 = TextMobject('与条的边界相交的会变成黄色').set_color(YELLOW).to_edge(UL).shift(DOWN)
        text5 = TextMobject('没有相交的会变为蓝色').set_color(YELLOW).to_edge(UL).shift(DOWN*2)
        self.add_fixed_in_frame_mobjects(VGroup(text3,text4,text5))
        self.wait(5)
        self.play(FadeOut(VGroup(text3,text4,text5)))
        self.wait(1)
        n=30
        all_times=30
        times=0
        texpigroup=VGroup()
        linegroup=VGroup()
        pilist=[]
        texpi = TexMobject(r'\pi=')
        texpi.to_corner(UL)
        self.add_fixed_in_frame_mobjects(texpi)
        while n >0:
            value=ValueTracker()
            x=random.uniform(-6,6)
            y=random.uniform(-2,2)
            z=random.uniform(-PI/2,PI/2)
            a=9.8
            x_1=x+7/13*math.cos(z)
            y_1=y+7/13*math.sin(z)
            height=3
            line=Line(np.array([x,y,height]),np.array([x_1,y_1 ,height])).set_color(BLUE)
            line.add_updater(lambda thing: thing.become(
                Line(np.array([x, y, height-((value.get_value())**2)*0.5*a]),
                     np.array([x_1, y_1, height-((value.get_value())**2)*0.5*a])
                     ).set_color(BLUE)))
            self.play(FadeIn(line),run_time=0.1)
            self.play(value.set_value,math.sqrt(6/a),rate_func=linear,run_time=0.6)
            n-=1
            line.clear_updaters(recursive=True)
            y_max=max(y_1,y)
            y_min=min(y,y_1)
            for i in range(1,14):
                if y_min<4-i*8/13*0.8:
                    if y_max>4-i*8/13*0.8:
                        self.play(line.set_color,YELLOW,run_time=0.3)
                        times+=1
                    else:
                        pass
                else:
                    pass
            p = times / (all_times-n)
            if p==0:
                pass
            else:
                pi = (2 * (7/13)) / ((8/13)* p)
                self.play(FadeOut(texpi),run_time=0.2)
                pilist.append(pi)
                texpi=TexMobject('\pi=%.5f'%pi).to_corner(UL)
                texpigroup.add(texpi)
                self.add_fixed_in_frame_mobjects(texpi)
            linegroup.add(line)
        self.wait(2)
class figure1(ThreeDScene):
    def construct(self):
        flag=get_flag()
        self.add(flag)
        n = 10000
        all_times = 10000
        times = 0
        pilist = []
        while n > 0:
            x = random.uniform(-6, 6)
            y = random.uniform(-3, 3)
            z = random.uniform(-PI / 2, PI / 2)
            x_1 = x + 7 / 13 * math.cos(z)
            y_1 = y + 7 / 13 * math.sin(z)
            line = Line(np.array([x, y,0]), np.array([x_1, y_1, 0])).set_color(BLUE)

            n -= 1
            line.clear_updaters(recursive=True)
            y_max = max(y_1, y)
            y_min = min(y, y_1)
            for i in range(1, 14):
                if y_min < 4 - i * 8 / 13 * 0.8:
                    if y_max > 4 - i * 8 / 13 * 0.8:
                        line.set_color(YELLOW)
                        times += 1
                    else:
                        pass
                else:
                    pass
            p = times / (all_times - n)
            if p == 0:
                pass
            else:
                pi = (2 * (7 / 13)) / ((8 / 13) * p)
                pilist.append(pi)
            self.add(line)
            if n%100==0:
                print(n/100)
        newlist = sorted(pilist, key=lambda a: abs(a - PI))
        text=TextMobject(r'$\pi=$'+str(newlist[0])).set_color(PINK).to_edge(DOWN)
        self.add(text)
class figure2(ThreeDScene):
    def construct(self):
        flag=get_flag()
        self.add(flag)
        n = 20000
        all_times = 20000
        times = 0
        pilist = []
        while n > 0:
            x = random.uniform(-6, 6)
            y = random.uniform(-3, 3)
            z = random.uniform(-PI / 2, PI / 2)
            x_1 = x + 7 / 13 * math.cos(z)
            y_1 = y + 7 / 13 * math.sin(z)
            line = Line(np.array([x, y,0]), np.array([x_1, y_1, 0])).set_color(BLUE)

            n -= 1
            line.clear_updaters(recursive=True)
            y_max = max(y_1, y)
            y_min = min(y, y_1)
            for i in range(1, 14):
                if y_min < 4 - i * 8 / 13 * 0.8:
                    if y_max > 4 - i * 8 / 13 * 0.8:
                        line.set_color(YELLOW)
                        times += 1
                    else:
                        pass
                else:
                    pass
            p = times / (all_times - n)
            if p == 0:
                pass
            else:
                pi = (2 * (7 / 13)) / ((8 / 13) * p)
                pilist.append(pi)
            self.add(line)
            if n%100==0:
                print(n/100)
        newlist = sorted(pilist, key=lambda a: abs(a - PI))
        text=TextMobject(r'$\pi=$'+str(newlist[0])).set_color(PINK).to_edge(DOWN)
        self.add(text)
class figure3(ThreeDScene):
    def construct(self):
        flag=get_flag()
        self.add(flag)
        n = 50000
        all_times = 50000
        times = 0
        pilist = []
        while n > 0:
            x = random.uniform(-6, 6)
            y = random.uniform(-3, 3)
            z = random.uniform(-PI / 2, PI / 2)
            x_1 = x + 7 / 13 * math.cos(z)
            y_1 = y + 7 / 13 * math.sin(z)
            line = Line(np.array([x, y,0]), np.array([x_1, y_1, 0])).set_color(BLUE)

            n -= 1
            line.clear_updaters(recursive=True)
            y_max = max(y_1, y)
            y_min = min(y, y_1)
            for i in range(1, 14):
                if y_min < 4 - i * 8 / 13 * 0.8:
                    if y_max > 4 - i * 8 / 13 * 0.8:
                        line.set_color(YELLOW)
                        times += 1
                    else:
                        pass
                else:
                    pass
            p = times / (all_times - n)
            if p == 0:
                pass
            else:
                pi = (2 * (7 / 13)) / ((8 / 13) * p)
                pilist.append(pi)
            self.add(line)
            if n%100==0:
                print(n/100)
        newlist = sorted(pilist, key=lambda a: abs(a - PI))
        text=TextMobject(r'$\pi=$'+str(newlist[0])).set_color(PINK).to_edge(DOWN)
        self.add(text)

class end(Scene):
    def construct(self):
        text1=TextMobject('随着投掷次数的逐渐增加，所计算的$\pi$值也更加准确').set_color(YELLOW)
        self.play(Write(text1))
        self.wait(1)
        text2=TextMobject('这就是神奇的布丰投针问题').set_color(YELLOW)
        self.play(text1.shift,UP)
        self.play(Write(text2))
        self.wait(1)
        text3=TextMobject('感谢大家能够坚持看到这里').set_color(YELLOW)
        textgroup=VGroup(text1,text2)
        self.play(textgroup.shift, UP)
        self.play(Write(text3))
        self.wait(1)
        text4=TextMobject('你看到的这个视频是靠788行python代码写出的').set_color(YELLOW)
        textgroup.add(text3)
        self.play(textgroup.shift, UP)
        self.play(Write(text4))
        self.wait(1)
        text5 = TextMobject('视频制作属实不易，感谢大家的三连关注和支持').set_color(YELLOW)
        textgroup.add(text4)
        self.play(textgroup.shift, UP)
        self.play(Write(text5))
        self.wait(1)
        textgroup.add(text5)
        good=SVGMobject(r'C:\Users\22326\Documents\Tencent Files\2232652509\FileRecv\一笔画的svg素材\svg_icon\good.svg').set_color(GREY).shift(LEFT*2+DOWN*5).scale(0.5)
        coin=SVGMobject(r'C:\Users\22326\Documents\Tencent Files\2232652509\FileRecv\一笔画的svg素材\svg_icon\coin.svg').set_color(GREY).shift(DOWN*5).scale(0.5)
        favo = SVGMobject(
            r'C:\Users\22326\Documents\Tencent Files\2232652509\FileRecv\一笔画的svg素材\svg_icon\favo.svg').set_color(
            GREY).shift(RIGHT*2+DOWN * 5).scale(0.5)
        sanliangroup=VGroup(good,favo,coin)
        self.play(VGroup(textgroup,sanliangroup).shift,UP*5)
        self.play(WiggleOutThenIn(good))
        self.play(WiggleOutThenIn(good))
        self.play(WiggleOutThenIn(good))
        self.play(sanliangroup.set_color,BLUE)
        self.play(Flash(good,flash_radius=1),Flash(coin,flash_radius=1),Flash(favo,flash_radius=1))
        self.wait(2)


