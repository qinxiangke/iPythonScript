#ke1.txt as input of the awk tool
#Name    Hour    salary
#Beth	4.00	0
#Dan	3.75	0
#kathy	4.00	10
#Mark	5.00	20
#Mary	5.50	22
#Susie	4.25	18

#task1:output the name and salary of the employee whose work time more than 0
awk '$3 == 0 { print $1 }' k1.txt
awk ‘$3 == 0 { print $1 }’ ke1.txt

#awk program structure
pattern {action}
pattern {action}
