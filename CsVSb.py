import math

pi = 3.141592654
A = 10475.764126557
h = 6.62607004 * 10 ** -34
e = 1.60217733 * 10 ** -19
me = 9.10938356 * 10 ** -30

print(h / (2 * pi * 2 * pi * e))


def run(a, b):
    """k坐标乘过2pi"""
    r = (a - b) / 2
    print(r * r * pi * A)


def runa(a, b):
    """k坐标未乘2pi"""
    a = a * 2 * pi
    # print(a)
    b = b * 2 * pi
    # print(b)
    r = (a - b) / 2
    print(r * r * pi * A)


def runb(a, b, c):
    """k坐标未乘2pi,椭圆"""
    a = a * 2 * pi
    # print(a)
    b = b * 2 * pi
    # print(b)
    c = c * 2 * pi
    print((c - a) * (b - c) * pi * A)


def rund(a, c):
    """k点未乘2pi，圆形，c-a为半径"""
    r = (c - a) * 2 * pi
    print(r * r * pi * A)


def runc(a):
    """反解界面大小，或对应的倒空间长度"""
    b = math.sqrt(a / (A * pi))
    print(a / A)
    print(b / (2 * pi) * 2)


runa(0.18821, 0.19719)
runa(0.19719, 0.20714)
runa(0.20714, 0.25494)
runb(0.20714, 0.25494, 0.2331)
runa(0.37938, 0.43277)
runa(0.37938, 0.4334)
runb(0.4334, 0.46291, 0.445)
runa(0.46291, 0.47868)
runa(0.44117, 0.44823)
runa(0.47868, 0.52928)
runb(0.47868, 0.52928, 0.50552)
runa(0.03131, -0.03131)
print(-0.01446)

runa(0.19768, 0.20666)
runa(0.20666, 0.25543)
runb(0.20666, 0.25543, 0.23213)
# runa(0.37938,0.43277)
# runa(0.37938,0.4334)
# runb(0.4334,0.46291,0.445)
# runa(0.44117, 0.44823)
runb(0.46194, 0.47941, 0.47177)
runa(0.47941, 0.52855)
runb(0.47941, 0.52855, 0.50552)
runa(0.53364, 0.55015)
print("反解")
runc(27)
runc(73)
runc(727)
runc(786)
runc(33.5)
print(-0.076)
runb(0.43928, 0.45418, 0.445)
runa(0.20059, 0.20447)


def area(a):
    a=1/(a*math.sqrt(3)/2)#倒空间轴长
    """六方的面积，a为轴长"""
    a = a * 2 * pi
    # print(a)
    s = a ** 2 * math.sqrt(3) / 2
    # print(V)
    return s

def calpre(a):
    return a/area(5.50552)

print("area")
print(0.00258 / area(5.50552))
print(0.00697 / area(5.50552))
print(0.06940 / area(5.50552))
print(0.07503 / area(5.50552))
print(calpre(0.00258))
area(1)
print(100 ** 2)


def vf(Af, m):
    """费米速度"""
    vf = h / (2 * pi) * math.sqrt(Af / pi) * (10 ** 10) / (me * m)
    return vf


print(vf(0.00258, 0.13003), vf(0.00697, 0.12829), vf(0.06940, 0.54010), vf(0.07503, 0.60574))
rund(0.02795, 0)
runa(0.09478, 0.10277)
runa(0.09478, 0.10003)
runb(0.09478, 0.10003, 0.09646)
runb(0.09478, 0.10277, 0.09709)
runb(0.13156, 0.18288, 0.16541)
runa(0.20108, 0.2035)
runb(0.43991, 0.45272, 0.445)
runb(0.48536, 0.5237, .50552)
runa(0.53801, 0.54748)

runb(0.13593, 0.18263, 0.16541)
runa(0.09457, 0.104)

print((0.45 / 0.51 * 0.85440055) ** 2 * pi * A)
import math

print(math.sqrt(0.09611757 ** 2 + 0.05549351 ** 2))
