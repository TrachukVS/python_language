#task1--------------------------------------------
"""
���� ������ �������������� �����: x1, y1, x2, y2.
 �������� ������� distance(x1, y1, x2, y2),
 ����������� ���������� ����� ������ (x1,y1) � (x2,y2).
 �������� ������ �������������� ����� � �������� ��������� ������ ���� �������.
"""
import math
def distance(x1,x2,y1,y2):
	result=0
	result=math.sqrt((x2-x1)**2+(y2-y1)**2))
	return result
x1=float(input())
x2=float(input())
y1=float(input())
y2=float(input())
res=distance(x1,x2,y1,y2)
print(res)
#-------------------------------------------------
#task2--------------------------------------------
"""
���� �������������� ������������� ����� a � ����e ����� n.

��������� an. ������� �������� � ���� ������� power(a, n).

����������� �������� ���������� � ������� ������������ ������.
"""
def power(a,n):
	if n==1:
		result=a
	else:
		k=2
		while k<=n:
			result*=a
			k+=1
	return result
a=float(input())
n=int(input())
res=power(a,n)
print(res)
#-------------------------------------------------

#task3--------------------------------------------
"""
���� �������������� ������������� ����� a � ����� ��������������� ����� n.
 ��������� an �� ��������� �����, ���������� � ������� ����� ** � ������� math.pow(),
 � ��������� ������������ ����������� an=a*an-1.
"""
def power(a, n):

    if n == 0:

        return 1

    else:

        return a*power(a, n - 1)



a = float(input())

n = int(input())

res=power(a,n)
print(res)
#---------------------------------------------------

#task4----------------------------------------------
"""
�������� ������� fib(n),
 ������� �� ������� ������ ����������������
 n ���������� n-e ����� ���������.
"""

def fib(n):

    if n == 1 or n == 2:

        return 1
    else:

        return fib(n - 1) + fib(n - 2)



n = int(input())
res=fib(n)

print(res)
#-----------------------------------------------------