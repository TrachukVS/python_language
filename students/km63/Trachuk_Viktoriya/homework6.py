#task1--------------------------------------------
"""
�������� ��� �������� ������ � ������� ���������
"""
s=input()
list=s.split( )
i=0
for element in list:
    print(list[i])
    i+=2 
#-------------------------------------------------
#task2--------------------------------------------
"""
�������� ��� ������ �������� ������. ��� ���� ����������� ���� for, ������������ �������� ������, � �� �� �������!
"""
s=input()
list=s.split()
i = 0
for element in list:
    q = i % 2
    if q==0:
        print(element)
    i+=1
#-------------------------------------------------
#task3--------------------------------------------
"""
��� ������ �����. �������� ��� �������� ������, ������� ������ ����������� ��������.
"""
s=input()
list=s.split( )
i=0
for element in list:
    if len(list)==1:
        list=[]
        print(list)
    elif list[i+1]>list[i]:
        print(list[i+1])
    i+=1
#-------------------------------------------------
#task4--------------------------------------------
"""
��� ������ �����. ���� � ��� ���� ��� �������� �������� ������ �����, �������� ��� �����. ���� �������� ��������� ������ ����� ��� � �� �������� ������. ���� ����� ��� ������� ��������� � �������� ������ ����.
"""
def input_data():
    data = input().split()
    return data
    
def operation_data(elements):
    data = []
    for i in range(0, len(elements)):
            if i < len(elements)-1:
                if int(elements[i]) * int(elements[i + 1]) > 0:
                    data = [elements[i]]
                    data.append(elements[i + 1])
                    break
    return data

def print_data(output_data):
    for i in output_data:
        print (i, end=' ')
print_data(operation_data(input_data()))
#-------------------------------------------------
#task5--------------------------------------------
"""
��� ������ �����. ����������, ������� � ���� ������ ���������, ������� ������ ���� ����� �������, � �������� ���������� ����� ���������. ������� �������� ������ ������� �� �����������, ��������� � ��� ������������ �������.
"""
list_new=[]
s=input()
list=s.split( )
if len(list)==1:
    print(list_new)
i=1
for element in list:
    if i!=(len(list)-1):
        if (list[i]>list[i-1]) and (list[i]>list[i+1]):
            list_new.append(list[i])
        i+=1    
        
print(list_new)   
#-------------------------------------------------
#task6--------------------------------------------
"""
��� ������ �����. �������� �������� ����������� �������� � ������, � ����� ������ ����� �������� � ������. ���� ���������� ��������� ���������, �������� ������ ������� �� ���.
"""
s=input()
list=s.split( )
i=0
g1=0
max=list[0]
for element in list:
    if i!=(len(list)-1):
        if list[i+1]>max:
            max=list[i+1]
            g1=i+1
        i+=1
    else: 
        if list[i]>max:
            max=list[i]
            g1=i
print(max)
print(g1)
#-------------------------------------------------
#task7--------------------------------------------
"""
���� ������� � ������ �����. �� ����� ����������� ��� ������������ ���������� ��� ����� � �����. �������� ��� ��� �������.
��������� �������� �� ���� �������������� ������������������ ����������� �����, ���������� ���� ������� �������� � �����. ����� ����� �������� ����� X � ���� ����. ��� ����� �� ������� ������ ����������� � �� ��������� 200. �������� �����, ��� ������� ���� ������ ������ � �����. ���� � ����� ���� ���� � ���������� ������, ����� ��, ��� � ����, �� �� ������ ������ ����� ���.
"""
s=input()
list=s.split( )
x=input()
list_new=[]
i=0
j=0
for element in list:
    if list[i]==x:
        if i!=(len(list)-1):
            j=i+1
        else:
            j=len(list)
    else:
        while list[i]>x:
            if i!=(len(list)-1):
                i+=1
                j=i
            else:
                j=len(list)
print(j)
#-------------------------------------------------
#task8--------------------------------------------
"""
��� ������, ������������� �� ���������� ��������� � ���. ����������, ������� � ��� ��������� ���������.
"""
s=input()
list=s.split( )
i=0
j=len(list)
for element in list:
    if i!=(len(list)-1):
        if list[i]==list[i+1]:
            j-=1
        i+=1
print(j)
#-------------------------------------------------
#task9--------------------------------------------
"""
����������� �������� �������� ������ (A[0] c A[1], A[2] c A[3] � �. �.). ���� ��������� �������� �����, �� ��������� ������� �������� �� ����� �����.
"""
s=input()
list=s.split( )
i=0
if len(list)%2 == 1:
    for element in list:
        if i!=(len(list)-1):
            k=list[i]
            list[i]=list[i+1]
            list[i+1]=k
            i+=2
    print(list)
else:
    for element in list:
        if i!=(len(list)):
            k=list[i]
            list[i]=list[i+1]
            list[i+1]=k
            i+=2
    print(list)
#-------------------------------------------------
#task10--------------------------------------------
"""
� ������ ��� �������� ��������. ��������� ������� ����������� � ������������ ������� ����� ������.
"""
def input_data():
    data = input().split()
    return data

def operation_data(elements):
    max = elements[0]
    min = elements[0]
    ind_min = 0
    ind_max = 0
    for i in range(0, len(elements)):
        if  int(min) > int(elements[i]):
            min = elements[i]
            ind_min = i
        if  int(max) < int(elements[i]):
            max = elements[i]
            ind_max = i
    elements[ind_min], elements[ind_max] = elements[ind_max], elements[ind_min]    
    return elements

def print_data(output_data):
    for i in output_data:
        print (i, end=' ')

print_data(operation_data(input_data()))
#-------------------------------------------------
#task11--------------------------------------------
"""
��� ������ �� ����� � ������ �������� � ������ k. ������� �� ������ ������� � �������� k, ������� ����� ��� ��������, ������� ������ �������� � �������� k.
��������� �������� �� ���� ������, ����� ����� k. ��������� �������� ��� ��������, � ����� ����� ������� ��������� ������� ������ ��� ������ ������ pop() ��� ����������.
��������� ������ ������������ ����� ��������������� � ������, � �� ������ ��� ��� ������ ���������. ����� ������ ������������ �������������� ������. ����� �� ������� ������������ �����pop(k) � ����������.
"""
s=input()
list=s.split( )
k=int(input())
len=len(list)
while k<len-1:
    list[k]=list[k+1]
    k+=1
list.pop()
print(list)
#-------------------------------------------------
#task12--------------------------------------------
"""
��� ������ ����� �����, ����� k � �������� C. ���������� �������� � ������ �� ������� � �������� k �������, ������ C, ������� ��� ��������, ������� ������ �� ����� k, ������.
��������� ��� ���� ���������� ��������� � ������ �������������, ����� ���������� ������ � ��� ����� ����� ����� �������� ����� �������, ��������� ����� append.
������� ���������� ������������ ��� � ��������� ������, �� ����� ����� ��� ������ � �� �������� ��������������� ������.
"""
def input_data():

    data = input().split()

    return data

def operation_data(elements):

    data = input().split()

    elements.append(data[1])

    for i in range(len(elements) - 1, int(data[0]), -1):

        elements[i] = elements[i - 1]

    elements[int(data[0])] = int(data[1])

    return elements

def print_data(output_data):
   for i in output_data:

        print (i, end=' ')
  
print_data(operation_data(input_data()))
#-------------------------------------------------
#task13--------------------------------------------
"""
��� ������ �����. ����������, ������� � ��� ��� ���������, ������ ���� �����. ���������, ��� ����� ��� ��������, ������ ���� ����� �������� ���� ����, ������� ���������� ���������.
"""
s=input()
list=s.split( )
len=len(list)
amount=0
i=0
while i<len:
    j=0
    while j<i:
        if list[i]==list[j]:
            amount+=1
        j+=1
    i+=1
print(amount)
#-------------------------------------------------
#task14--------------------------------------------
"""
��� ������. �������� �� ��� ��������, ������� ����������� � ������ ������ ���� ���. �������� ����� �������� � ��� �������, � ������� ��� ����������� � ������.
"""
s=input()
list=s.split( )
len=len(list)
i=0
while i<len:
    j=0
    while j<len:
        if list[i]==list[j] and j!=i:
            break
        elif j==len-1:
            print(list[i])
        j+=1
    i+=1
#-------------------------------------------------
#task15--------------------------------------------
"""
N ������ ��������� � ���� ���, ����������� �� ����� ������� ������� �� 1 �� N. ����� �� ����� ���� ������� K �����, ��� ���� i-� ��� ���� ��� ����� � �������� �� li �� ri ������������. ����������, ����� ����� �������� ������ �� �����.
��������� �������� �� ���� ���������� ������ N � ���������� ������� K. ����� ���� K ��� ����� li, ri, ��� ���� 1? li? ri? N.
��������� ������ ������� ������������������ �� N ��������, ��� j-� ������ ���� �I�, ���� j-� ����� �������� ������, ��� �.�, ���� j-� ����� ���� �����.
"""
Def form_of_list(number):
	List=[]
	List=[�I� for I in range(number)]
	Return(list)
Number,count_of_shots=input().split()
List=form_of_list(int(number))
For I in range (int(count_of_shots)):
	Start_pos,final_pos=input().splint()
	For j in range(int(start_pos)-1, int(final_pos)):
		List_[j]=�.�
For element in list:
	Print(element, end=� �)
#-------------------------------------------------
#task16--------------------------------------------
"""
��������, ��� �� ����� 8?8 ����� ���������� 8 ������ ���, ����� ��� �� ���� ���� �����. ��� ���� ����������� 8 ������ �� �����, ����������, ���� �� ����� ��� ���� ������ ���� �����.
��������� �������� �� ���� ������ ��� �����, ������ ����� �� 1 �� 8 � ���������� 8 ������. ���� ����� �� ���� ���� �����, �������� ����� NO, ����� �������� YES.

"""
def form_list_(size):#this function create a new 2-D list sizeXsize (this function created by me)
     list_ = (size * '0 ').split()
     for i in range(len(list_)):
         list_[i] = []
         list_[i] = (size * '0 ').split()
     return list_
 
def horizontal_vertical_test(list_):#this function make a test. If ion horizontal and vertical we have only 1 queen function retur 1, else 0.(created by me)
    for i in range(len(list_)):
        sum_of_horizontal = 0
        sum_of_vertical = 0
        for j in range(len(list_)):
            sum_of_horizontal += int(list_[i][j])
            sum_of_vertical += int(list_[j][i])
        if sum_of_horizontal > 1 or sum_of_vertical > 1:
             return 0
     return 1
 
 
 def diagonal_test(list):#this function for horizontal test(created by Anton Pidgayniy)
     for i in range(len(list)):
         sum1, sum2, sum3, sum4 = 0, 0, 0, 0
         for j in range(len(list)):
             if -1 < j - i < len(list):
                 sum1 += int(list[j - i][j])
                 sum2 += int(list[j][j - i])
                 sum3 += int(list[j - i][len(list) - j - 1])
                 sum4 += int(list[len(list) - j - 1][j - i])
         if sum1 > 1 or sum2 > 1 or sum3 > 1 or sum4 > 1:
             return 0
     return 1
 
 
 list_ = form_list_(8)
 
 for i in range(8):# This is part of code where we read a coordinat's of Queen on the chess board(created by me)
     i, j = input().split()
     list_[int(i) - 1][int(j) - 1] = 1
 
 if diagonal_test(list_) == 1 and horizontal_vertical_test(list_) == 1:
	 print("NO")
 else:
     print("YES")
#-------------------------------------------------
