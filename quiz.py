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

log.write(u'��ʾ��\r\n')
log.write(u'����������������� word ���� д��txt��\r\n')
log.write(u'��һ���������excel�ļ�һ����Ϊ�����ϴ����ҵ�����.\r\n')
log.write(u'�������ʱ�������δ�ϴ�������������ʹ��U���ύ.\r\n')

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
log.write(u'�㽶' + str(banana))
log.write(u'��' + str(dragon))
log.write(u'����' + str(monkey))
log.write(u'����' + str(orange))
'''
log.write(u'��һ��\r\n')

for i in [1,2,3,4]:
    log.write(u' ��װ����Ʒ %s �·ݵĳɱ���Ϊ %s Ԫ�����۶�Ϊ %s Ԫ.\r\n' % (i, str(banana[i]['paid']), str(banana[i]['sell']) ))

for i in [1,2,3,4]:
    log.write(u' ʳƷ����Ʒ %s �·ݵĳɱ���Ϊ %s Ԫ�����۶�Ϊ %s Ԫ.\r\n' % (i, str(dragon[i]['paid']), str(dragon[i]['sell']) ))

for i in [1,2,3,4]:
    log.write(u' �ҵ�����Ʒ %s �·ݵĳɱ���Ϊ %s Ԫ�����۶�Ϊ %s Ԫ.\r\n' % (i, str(monkey[i]['paid']), str(monkey[i]['sell']) ))

for i in [1,2,3,4]:
    log.write(u' �Ļ�����Ʒ %s �·ݵĳɱ���Ϊ %s Ԫ�����۶�Ϊ %s Ԫ.\r\n' % (i, str(orange[i]['paid']), str(orange[i]['sell']) ))


log.write(u'(1)�����������Ʒ�����۶��Լ��ɱ�����ɻ��ܱ�.\r\n')
log.write(u'(2) �ڱ������������Ʒ1��4�·ݵ��������.\r\n')
log.write(u'(3) �ڱ������������Ʒ1��4�·ݵ�ƽ������.\r\n')
log.write(u'(4) �����ó���1�·���Ʒ���۶�ı�״ͼ.\r\n')
log.write(u'(5) �����ó���2�·���Ʒ�ɱ������״ͼ.\r\n')
log.write(u'(6) �����ó���1��4�·�������������ͼ.\r\n.')

# 1th end

log.write(u'�ڶ���\r\n')

# 2nd begin

worklist = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
workorder = [' ', ' ', ' ', 'A, B', 'B, C','A, B, C','D, E, F']
workday = []


for i in worklist:
    number = random.randint(1,10)
    workday.append(number)


log.write(u'ĳ���������й�����ɣ����������������ͼ��������ؼ�·���͹����ܹ���\r\n')

for i in range(0,7):
    log.write(u' ���� %s �Ĺ����� %s ��, ��ǰ����Ϊ %s .\r\n' % (worklist[i], workday[i],workorder[i]))

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

log.write(u'������\r\n')
log.write(u' �� a= (%s,%s,%s) ,' % (shuzua[0],shuzua[1],shuzua[2]))
log.write(u'b= (%s,%s,%s) ,' % (shuzub[0],shuzub[1],shuzub[2]))
log.write(u'c= (%s,%s,%s),' % (shuzuc[0],shuzuc[1],shuzuc[2]))
log.write(u' �Լ���:\r\n')
log.write('(1)a+b-c\r\n')
log.write('(2)a*b\r\n')
log.write('(3)(a+b)*c\r\n')
log.write('(4)a-2b+3c\r\n')

# 3rd end

# 4th begin

zong = random.randint(400,500)
shou = random.randint(200,390)

log.write(u'������\r\n')
log.write(u'ĳ��ͥ���÷��ڸ����ķ�ʽ�����������������ܶ�Ϊ %s ,000Ԫ��\r\n' % zong)
log.write(u'�׸� %s ,000Ԫ�� 5�껹�����������ٷ�֮4.9��Ϣ,������Ϣ��\r\n' % shou)
log.write(u'��ÿ��Ӧ�������Ԫ������ȷ���֣���\r\n')

# 4th end


log.close

# subprocess.Popen('notepad.exe D:\\test.txt')

raw_input('Open D:\\test.txt now, press Enter\r\n')
