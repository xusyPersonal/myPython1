import math ;
import calendar ;

#print(math.pi) ;
appconst=5*2 ;
grapecost=15*3 ;

# print("苹果的花费：{}，葡萄的花费：{}".format(appconst,grapecost)) ;
# print(math.degrees(math.pi/2))

cal = calendar.month(2017, 2)
# print ("以下输出2017年1月份的日历:")
# print (cal) ;
discount = 1.0 ;
total_cost=20 ;
if total_cost<30 :
 discount=0.9;
 print("实际花费：{}".format(discount*total_cost)) ;
elif total_cost>50:
 discount= 0.8 ;

 print("实际花费：{}".format(discount*total_cost)) ;

var1 = 100
if var1:
    print("1 - if 表达式条件为 true")
    print(var1)

var2 = 0
if var2:
    print("2 - if 表达式条件为 true")
    print(var2)
print("Good bye!")







