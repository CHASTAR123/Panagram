
students = {
'name': 'Jack' ,
'age': 12,    
'sport':'Football',
'marks' : [40,50,75,60]  ,
'subject' : 'Math'  ,
}   
data = {

}
for i in range(2):
    name = input('Please enter your name')
    age = int(input('Please enter your age'))
    grade = input('PLease enter your grade')
    data[name] = {'name': name,'age' : age ,'grade' : grade}
print(data)