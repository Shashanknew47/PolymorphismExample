
# len() being used for a string 
print(len("Data Science")) 
  
# len() being used for a list 
print(len([1, 2, 3, 4])) 

class CSVColumnOne: 
    def col_count(self): 
        print("Column One - count function is called.") 
   
    def col_mean(self): 
        print("Column One - mean function is called.") 
   
    def col_std(self): 
        print("Column One - std function is called.") 
   
class CSVColumnTwo:
    def col_count(self): 
        print("Column Two - count function is called.") 
   
    def col_mean(self): 
        print("Column Two - mean function is called.") 
   
    def col_std(self): 
        print("Column Two - std function is called.") 

def func(obj): 
    obj.col_count() 
    obj.col_mean() 
    obj.col_std() 
   
obj_col_one = CSVColumnOne()
obj_col_two = CSVColumnTwo() 
   
func(obj_col_one) 
func(obj_col_two)


class CSVColumn: 
    def col_count(self): 
        print("Count function is called for all columns.") 
   
    def col_mean(self): 
        print("Mean function is called for all columns.")  
   
class CSVColumnSub(CSVColumn):
    def col_mean(self): 
        print("Mean function is called for only sub-columns.") 
   
obj_col_all = CSVColumn()
obj_col_sub = CSVColumnSub()

obj_col_all.col_count()
obj_col_all.col_mean()

obj_col_sub.col_count()
obj_col_sub.col_mean()




