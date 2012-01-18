#!/usr/bin/python
# -*- coding: gbk -*-

import random
import codecs


yourname = raw_input('Please input yourname by pinyin\r\n')
yourclass = raw_input('Please input yourclass by pinyin\r\n')

print yourname
print yourclass

# y = yourname.decode('latin-1')

log = codecs.open(r'D:\test.txt','w','gbk')

log.write(yourclass)
log.write(' \r\n')
log.write(yourname)
log.write(' ')
log.write('Welcome to Matrix!\r\n')

log.write(u'提示：\r\n')
log.write(u'将三、四两题答案输入 word 或者 写入txt，\r\n')
log.write(u'与一、二两题的excel文件一并作为附件上传至我的邮箱.\r\n')
log.write(u'如果考试时间结束还未上传，请向我申请使用U盘提交.\r\n')

# 1th begin

def item():
    product = {1:{'sell':2000, 'paid':1600},
                     2:{'sell':2000, 'paid':1600},
                     3:{'sell':2000, 'paid':1600},
                     4:{'sell':2000, 'paid':1600}}

    for i in [1,2,3,4]:
        number1 = random.randint(100,1000)
        number2 = random.randint(100,1400)
        product[i]['sell'] += number1
        product[i]['paid'] += number2
                        
    return product


        
# give product to value


banana = item()
dragon = item()
monkey = item()
orange = item()

'''
log.write(u'香蕉' + str(banana))
log.write(u'龙' + str(dragon))
log.write(u'猴子' + str(monkey))
log.write(u'桔子' + str(orange))
'''
log.write(u'第一题\r\n')

for i in [1,2,3,4]:
    log.write(u' 服装类商品 %s 月份的成本额为 %s 元，销售额为 %s 元.\r\n' % (i, str(banana[i]['paid']), str(banana[i]['sell']) ))

for i in [1,2,3,4]:
    log.write(u' 食品类商品 %s 月份的成本额为 %s 元，销售额为 %s 元.\r\n' % (i, str(dragon[i]['paid']), str(dragon[i]['sell']) ))

for i in [1,2,3,4]:
    log.write(u' 家电类商品 %s 月份的成本额为 %s 元，销售额为 %s 元.\r\n' % (i, str(monkey[i]['paid']), str(monkey[i]['sell']) ))

for i in [1,2,3,4]:
    log.write(u' 文化类商品 %s 月份的成本额为 %s 元，销售额为 %s 元.\r\n' % (i, str(orange[i]['paid']), str(orange[i]['sell']) ))


log.write(u'(1)请把这四类商品的销售额以及成本额组成汇总表.\r\n')
log.write(u'(2) 于表中求出各类商品1到4月份的总利润额.\r\n')
log.write(u'(3) 于表中求出各类商品1到4月份的平均利润.\r\n')
log.write(u'(4) 制作该超市1月份商品销售额的饼状图.\r\n')
log.write(u'(5) 制作该超市2月份商品成本额的柱状图.\r\n')
log.write(u'(6) 制作该超市1到4月份总利润额的折线图.\r\n.')

# 1th end

log.write(u'第二题\r\n')

# 2nd begin

worklist = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
workorder = [' ', ' ', ' ', 'A, B', 'B, C','A, B, C','D, E, F']
workday = []


for i in worklist:
    number = random.randint(1,10)
    workday.append(number)


log.write(u'某工程由下列工序组成，试着求出工序流程图，并求出关键路径和工程总工期\r\n')

for i in range(0,7):
    log.write(u' 工序 %s 的工期是 %s 天, 紧前工序为 %s .\r\n' % (worklist[i], workday[i],workorder[i]))

#log.write

# 2nd end

# 3rd begin

shuzua = []

for i in range(0,3):
    ex = random.randint(1,10)
    shuzua.append(ex)

shuzub = []

for i in range(0,3):
    ex = random.randint(1,10)
    shuzub.append(ex)
        
shuzuc = []

for i in range(0,3):
    ex = random.randint(1,10)
    shuzuc.append(ex)

log.write(u'第三题\r\n')
log.write(u' 设 a= (%s,%s,%s) ,' % (shuzua[0],shuzua[1],shuzua[2]))
log.write(u'b= (%s,%s,%s) ,' % (shuzub[0],shuzub[1],shuzub[2]))
log.write(u'c= (%s,%s,%s),' % (shuzuc[0],shuzuc[1],shuzuc[2]))
log.write(u' 试计算:\r\n')
log.write('(1)a+b-c\r\n')
log.write('(2)a*b\r\n')
log.write('(3)(a+b)*c\r\n')
log.write('(4)a-2b+3c\r\n')

# 3rd end

# 4th begin

zong = random.randint(400,500)
shou = random.randint(200,390)

log.write(u'第四题\r\n')
log.write(u'某家庭采用分期付贷的方式购买汽车，购汽车总额为 %s ,000元，\r\n' % zong)
log.write(u'首付 %s ,000元， 5年还清贷款，按年利百分之4.9计息,复利计息，\r\n' % shou)
log.write(u'问每月应还款多少元？（精确到分）？\r\n')

# 4th end


log.close

# subprocess.Popen('notepad.exe D:\\test.txt')

raw_input('Open D:\\test.txt now, press Enter\r\n')
