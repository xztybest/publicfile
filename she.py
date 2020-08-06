import turtle
#单独定义一个画社的函数
def drawSnake(rad,angle,len,neckrad):
#定义颜色列表cyan蓝绿色
  colors = ["black","green","cyan","red","yellow","orange","blue","black"]
  for i in range(len):
#设置颜色
    turtle.color(colors[i])
#画蛇
    turtle.circle(rad,angle)
#换一个方向
    turtle.circle(-rad,angle)
#循环结束，画蛇头为紫色
  turtle.color("purple")
  turtle.circle(rad,angle/2)
#沿着海龟的前方画2倍半径
  turtle.fd(rad*2)
#掉头画蛇
  turtle.circle(neckrad+1,180)
#继续沿当前海龟方向前进2/3半径
  turtle.fd(rad*2/3)

#定义调用函数
def main():
#设置画布大小为1200x500像素
  turtle.setup(1200,500,0,0)
#海龟画笔抬起
  turtle.penup()
#定位到距离左边边上200px并垂直居中
  turtle.goto(-400,0)
#放下海龟画笔准备开始画图
  turtle.pendown()
#设置画笔大小为50宽
  pythonsize = 50
  turtle.pensize(pythonsize)
#设置画蛇的起始方向
  turtle.seth(-40)
#调用画蟒蛇的函数，设置参数半径，40，角度80，节数(长度)，调头半径
  drawSnake(40,80,8,pythonsize/2)

#调用运行程序
main()
