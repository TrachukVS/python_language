		#task1------------------------------------------------------------
""" 
		���� �������� ����� n. �������� ��������� ������ �� n?n ���������, �������� ��� ��������� "." (������ ������� ������� �������� ������� �� ������ �������). 
		����� ��������� ��������� "*" ������� ������ �������, ������� ������� �������, ������� ��������� � �������� ���������. 
		� ���������� ������� � ������� ������ ������������ ����������� ���������. 
		�������� ���������� ������ �� �����, �������� �������� ������� ���������. 
		""" 
		number = int(input()) 
		 
		list_=[['.'] * number for i in range(number)] 
		for i in range(number): 
		    for j in range(number): 
		        if i == ( number // 2 ) : 
		            list_[i][j]='*' 
		        if j == ( number // 2 ) : 
		            list_[i][j]='*' 
		        if i==j: 
		            list_[i][j]='*' 
		        if (ij)==number-1: 
		            list_[i][j]='*' 
		             
		for i in range(number): 
		    print() 
		    for j in range(number): 
		        print(list_[i][j],end=' ') 
		 
		#----------------------------------------------------------------- 
		#task2------------------------------------------------------------ 
		""" 
		���� ����� n. �������� ������ �������� n?n � ��������� ��� �� ���������� �������. 
		�� ������� ��������� ������ ���� �������� ����� 0. �� ���� ����������, ����������� � �������, ����� 1. 
		�� ��������� ���� ���������� ����� 2, � �.�.  
		""" 
		def print_array(array): 
		    for str in array: 
		        print() 
		        for elem in str: 
		            print(elem,end=' ') 
		n=int(input()) 
		 
		array=[[0] * n for i in range(n)] 
		for k in range(n): 
		    for i in range(n): 
		        for j in range(n): 
		            if i<j: 
		                array[i][j]=array[i1][j]1 
		            if j<i: 
		                array[i][j]=array[i][j1]1 
		print_array(array) 
		 
		#----------------------------------------------------------------- 
		#task3------------------------------------------------------------ 
		""" 
		���� ����� n. �������� ������ �������� n?n � ��������� ��� �� ���������� �������: 
		 
		����� �� ���������, ������ �� ������� �������� � ����� ������ ���� ����� 1. 
		 
		�����, ������� ���� ���� ���������, ����� 0. 
		 
		�����, ������� ���� ���� ���������, ����� 2. 
		 
		���������� ������ �������� �� �����. ����� � ������ ���������� ����� ��������. 
		""" 
		def create_list(n,list_): 
		    for i in range(n): 
		        list_.append(('0 '*n).split()) 
		    return(list_) 
		#default 
		list_=[] 
		#input 
		n=int(input()) 
		#main 
		list_=create_list(n,list_) 
		 
		for i in range(n): 
		    for j in range(n): 
		        if ij==n-1: 
		            list_[i][j]=1 
		        if ij>n-1: 
		            list_[i][j]=2 
		#print           
		for i in range(n): 
		    if i!=0: 
		        print() 
		    for j in range(n): 
		        print(list_[i][j], end=' ') 
		 
		#-----------------------------------------------------------------

