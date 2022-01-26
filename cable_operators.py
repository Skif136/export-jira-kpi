from vars import *
from atlassian import Jira

# 1
Low_One = (  one_month + priority + ' Low' + zone + ' CableOperators')
Low_One1 = ( one_month + in_time + priority + ' Low' + zone + ' CableOperators')
Medium_One = ( one_month + priority + ' Medium' + zone + ' CableOperators')
Medium_One1 = ( one_month + in_time + priority + ' Medium' + zone + ' CableOperators')
High_One = ( one_month + priority + ' High' + zone + ' CableOperators')
High_One1 = ( one_month + in_time + priority + ' High' + zone + ' CableOperators')
Critical_One = ( one_month + priority + ' Critical' + zone + ' CableOperators')
Critical_One1 = ( one_month + in_time + priority + ' Critical' + zone + ' CableOperators')
Blocker_One = ( one_month + priority + ' Blocker' + zone + ' CableOperators')
Blocker_One1 = ( one_month + in_time + priority + ' Blocker' + zone + ' CableOperators')
# 2
Low_Two = (  two_months + priority + ' Low' + zone + ' CableOperators')
Low_Two1 = ( two_months + in_time + priority + ' Low' + zone + ' CableOperators')
Medium_Two = ( two_months + priority + ' Medium' + zone + ' CableOperators')
Medium_Two1 = ( two_months + in_time + priority + ' Medium' + zone + ' CableOperators')
High_Two = ( two_months + priority + ' High' + zone + ' CableOperators')
High_Two1 = ( two_months + in_time + priority + ' High' + zone + ' CableOperators')
Critical_Two = ( two_months + priority + ' Critical' + zone + ' CableOperators')
Critical_Two1 = ( two_months + in_time + priority + ' Critical' + zone + ' CableOperators')
Blocker_Two = (  two_months + priority + ' Blocker' + zone + ' CableOperators')
Blocker_Two1 = ( two_months + in_time + priority + ' Blocker' + zone + ' CableOperators')
# 3
Low_Three = (  three_months + priority + ' Low' + zone + ' CableOperators')
Low_Three1 = ( three_months + in_time + priority + ' Low' + zone + ' CableOperators')
Medium_Three = ( three_months + priority + ' Medium' + zone + ' CableOperators')
Medium_Three1 = ( three_months + in_time + priority + ' Medium' + zone + ' CableOperators')
High_Three = ( three_months + priority + ' High' + zone + ' CableOperators')
High_Three1 = ( three_months + in_time + priority + ' High' + zone + ' CableOperators')
Critical_Three = ( three_months + priority + ' Critical' + zone + ' CableOperators')
Critical_Three1 = ( three_months + in_time + priority + ' Critical' + zone + ' CableOperators')
Blocker_Three = ( three_months + priority + ' Blocker' + zone + ' CableOperators')
Blocker_Three1 = ( three_months + in_time + priority + ' Blocker' + zone + ' CableOperators')
# 4
Low_Four = (  four_months + priority + ' Low' + zone + ' CableOperators')
Low_Four1 = ( four_months + in_time + priority + ' Low' + zone + ' CableOperators')
Medium_Four = ( four_months + priority + ' Medium' + zone + ' CableOperators')
Medium_Four1 = ( four_months + in_time + priority + ' Medium' + zone + ' CableOperators')
High_Four = ( four_months + priority + ' High' + zone + ' CableOperators')
High_Four1 = ( four_months + in_time + priority + ' High' + zone + ' CableOperators')
Critical_Four = ( four_months + priority + ' Critical' + zone + ' CableOperators')
Critical_Four1 = ( four_months + in_time + priority + ' Critical' + zone + ' CableOperators')
Blocker_Four = ( four_months + priority + ' Blocker' + zone + ' CableOperators')
Blocker_Four1 = ( four_months + in_time + priority + ' Blocker' + zone + ' CableOperators')
# 5
Low_Five = (  five_months + priority + ' Low' + zone + ' CableOperators')
Low_Five1 = ( five_months + in_time + priority + ' Low' + zone + ' CableOperators')
Medium_Five = ( five_months + priority + ' Medium' + zone + ' CableOperators')
Medium_Five1 = ( five_months + in_time + priority + ' Medium' + zone + ' CableOperators')
High_Five = ( five_months + priority + ' High' + zone + ' CableOperators')
High_Five1 = ( five_months + in_time + priority + ' High' + zone + ' CableOperators')
Critical_Five = ( five_months + priority + ' Critical' + zone + ' CableOperators')
Critical_Five1 = ( five_months + in_time + priority + ' Critical' + zone + ' CableOperators')
Blocker_Five = ( five_months + priority + ' Blocker' + zone + ' CableOperators')
Blocker_Five1 = ( five_months + in_time + priority + ' Blocker' + zone + ' CableOperators')
# 6
Low_Six = ( six_months + priority + ' Low' + zone + ' CableOperators')
Low_Six1 = ( six_months + in_time + priority + ' Low' + zone + ' CableOperators')
Medium_Six = ( six_months + priority + ' Medium' + zone + ' CableOperators')
Medium_Six1 = ( six_months + in_time + priority + ' Medium' + zone + ' CableOperators')
High_Six = ( six_months + priority + ' High' + zone + ' CableOperators')
High_Six1 = ( six_months + in_time + priority + ' High' + zone + ' CableOperators')
Critical_Six = ( six_months + priority + ' Critical' + zone + ' CableOperators')
Critical_Six1 = ( six_months + in_time + priority + ' Critical' + zone + ' CableOperators')
Blocker_Six = ( six_months + priority + ' Blocker' + zone + ' CableOperators')
Blocker_Six1 = ( six_months + in_time + priority + ' Blocker' + zone + ' CableOperators')
# Sum
Sum_one = ( one_month +  zone + ' CableOperators')
Sum_one1 = ( one_month + in_time  + zone + ' CableOperators')
Sum_two = (  two_months  + zone + ' CableOperators')
Sum_two1 = ( two_months + in_time  + zone + ' CableOperators')
Sum_three = (  three_months  + zone + ' CableOperators')
Sum_three1 = ( three_months + in_time + zone + ' CableOperators')
Sum_four = ( four_months +  zone + ' CableOperators')
Sum_four1 = ( four_months + in_time  + zone + ' CableOperators')
Sum_five = (  five_months  + zone + ' CableOperators')
Sum_five1 = ( five_months + in_time  + zone + ' CableOperators')
Sum_six = (  six_months  + zone + ' CableOperators')
Sum_six1 = ( six_months + in_time + zone + ' CableOperators')

jira = Jira(
    url= addr,
    token=token_user)

#1
data_Low_One = jira.jql(Low_One)
data_Low_One1 = jira.jql(Low_One1)
data_Medium_One = jira.jql(Medium_One)
data_Medium_One1 = jira.jql(Medium_One1)
data_High_One = jira.jql(High_One)
data_High_One1 = jira.jql(High_One1)
data_Critical_One = jira.jql(Critical_One)
data_Critical_One1 = jira.jql(Critical_One1)
data_Blocker_One = jira.jql(Blocker_One)
data_Blocker_One1 = jira.jql(Blocker_One1)
#2
data_Low_Two = jira.jql(Low_Two)
data_Low_Two1 = jira.jql(Low_Two1)
data_Medium_Two = jira.jql(Medium_Two)
data_Medium_Two1 = jira.jql(Medium_Two1)
data_High_Two = jira.jql(High_Two)
data_High_Two1 = jira.jql(High_Two1)
data_Critical_Two = jira.jql(Critical_Two)
data_Critical_Two1 = jira.jql(Critical_Two1)
data_Blocker_Two = jira.jql(Blocker_Two)
data_Blocker_Two1 = jira.jql(Blocker_Two1)
#3
data_Low_Three = jira.jql(Low_Three)
data_Low_Three1 = jira.jql(Low_Three1)
data_Medium_Three = jira.jql(Medium_Three)
data_Medium_Three1 = jira.jql(Medium_Three1)
data_High_Three = jira.jql(High_Three)
data_High_Three1 = jira.jql(High_Three1)
data_Critical_Three = jira.jql(Critical_Three)
data_Critical_Three1 = jira.jql(Critical_Three1)
data_Blocker_Three = jira.jql(Blocker_Three)
data_Blocker_Three1 = jira.jql(Blocker_Three1)
#4
data_Low_Four = jira.jql(Low_Four)
data_Low_Four1 = jira.jql(Low_Four1)
data_Medium_Four = jira.jql(Medium_Four)
data_Medium_Four1 = jira.jql(Medium_Four1)
data_High_Four = jira.jql(High_Four)
data_High_Four1 = jira.jql(High_Four1)
data_Critical_Four = jira.jql(Critical_Four)
data_Critical_Four1 = jira.jql(Critical_Four1)
data_Blocker_Four = jira.jql(Blocker_Four)
data_Blocker_Four1 = jira.jql(Blocker_Four1)
#5
data_Low_Five = jira.jql(Low_Five )
data_Low_Five1 = jira.jql(Low_Five1 )
data_Medium_Five = jira.jql(Medium_Five )
data_Medium_Five1 = jira.jql(Medium_Five1)
data_High_Five = jira.jql(High_Five )
data_High_Five1 = jira.jql(High_Five1 )
data_Critical_Five = jira.jql(Critical_Five )
data_Critical_Five1 = jira.jql(Critical_Five1 )
data_Blocker_Five = jira.jql(Blocker_Five )
data_Blocker_Five1 = jira.jql(Blocker_Five1)
#6
data_Low_Six = jira.jql(Low_Six )
data_Low_Six1 = jira.jql(Low_Six1 )
data_Medium_Six = jira.jql(Medium_Six )
data_Medium_Six1 = jira.jql(Medium_Six1)
data_High_Six = jira.jql(High_Six )
data_High_Six1 = jira.jql(High_Six1 )
data_Critical_Six = jira.jql(Critical_Six )
data_Critical_Six1 = jira.jql(Critical_Six1 )
data_Blocker_Six = jira.jql(Blocker_Six )
data_Blocker_Six1 = jira.jql(Blocker_Six1)
#Sum
data_Sum_One = jira.jql(Sum_one)
data_Sum_One1 = jira.jql(Sum_one1)
data_Sum_Two = jira.jql(Sum_two)
data_Sum_Two1 = jira.jql(Sum_two1)
data_Sum_Three = jira.jql(Sum_three)
data_Sum_Three1 = jira.jql(Sum_three1)
data_Sum_Four = jira.jql(Sum_four)
data_Sum_Four1 = jira.jql(Sum_four1)
data_Sum_Five = jira.jql(Sum_five)
data_Sum_Five1 = jira.jql(Sum_five1)
data_Sum_Six = jira.jql(Sum_six)
data_Sum_Six1 = jira.jql(Sum_six1)

cab = [(' '),
('# CableOperators-KPI-Jira'),
('# One-months'),
('tasks_completed_on_time (Month= "1 month ago", Priority= "Low", Zone= "CableOperators") {}' .format(data_Low_One1.get('total'))),
('tasks_completed_on_time (Month= "1 month ago", Priority= "Medium", Zone= "CableOperators") {}'.format(data_Medium_One1.get('total'))),
('tasks_completed_on_time (Month= "1 month ago", Priority= "High", Zone= "CableOperators") {}'.format(data_High_One1.get('total'))),
('tasks_completed_on_time (Month= "1 month ago", Priority= "Critical", Zone= "CableOperators") {}'.format(data_Critical_One1.get('total'))),
('tasks_completed_on_time (Month= "1 month ago", Priority= "Blocker", Zone= "CableOperators") {}'.format(data_Blocker_One1.get('total'))),
('tasks_completed_on_time (Month= "1 month ago", Priority= "All", Zone= "CableOperators") {}'.format(data_Sum_One1.get('total'))),
('tasks_total (Month= "1 month ago", Priority= "Low", Zone= "CableOperators") {}'.format(data_Low_One.get('total'))),
('tasks_total (Month= "1 month ago", Priority= "Medium", Zone= "CableOperators") {}'.format(data_Medium_One.get('total'))),
('tasks_total (Month= "1 month ago", Priority= "High", Zone= "CableOperators") {}'.format(data_High_One.get('total'))),
('tasks_total (Month= "1 month ago", Priority= "Critical", Zone= "CableOperators") {}'.format(data_Critical_One.get('total'))),
('tasks_total (Month= "1 month ago", Priority= "Blocker", Zone= "CableOperators") {}'.format(data_Blocker_One.get('total'))),
('tasks_total (Month= "1 month ago", Priority= "All", Zone= "CableOperators") {}'.format(data_Sum_One.get('total'))),
('# Two-months'),
('tasks_completed_on_time (Month= "2 month ago", Priority= "Low", Zone= "CableOperators") {}'.format(data_Low_Two1.get('total'))),
('tasks_completed_on_time (Month= "2 month ago", Priority= "Medium", Zone= "CableOperators") {}'.format(data_Medium_Two1.get('total'))),
('tasks_completed_on_time (Month= "2 month ago", Priority= "High", Zone= "CableOperators") {}'.format(data_High_Two1.get('total'))),
('tasks_completed_on_time (Month= "2 month ago", Priority= "Critical", Zone= "CableOperators") {}'.format(data_Critical_Two1.get('total'))),
('tasks_completed_on_time (Month= "2 month ago", Priority= "Blocker", Zone= "CableOperators") {}'.format(data_Blocker_Two1.get('total'))),
('tasks_completed_on_time (Month= "2 month ago", Priority= "All", Zone= "CableOperators") {}'.format(data_Sum_Two1.get('total'))),
('tasks_total (Month= "2 month ago", Priority= "Low", Zone= "CableOperators") {}'.format(data_Low_Two.get('total'))),
('tasks_total (Month= "2 month ago", Priority= "Medium", Zone= "CableOperators") {}'.format(data_Medium_Two.get('total'))),
('tasks_total (Month= "2 month ago", Priority= "High", Zone= "CableOperators") {}'.format(data_High_Two.get('total'))),
('tasks_total (Month= "2 month ago", Priority= "Critical", Zone= "CableOperators") {}'.format(data_Critical_Two.get('total'))),
('tasks_total (Month= "2 month ago", Priority= "Blocker", Zone= "CableOperators") {}'.format(data_Blocker_Two.get('total'))),
('tasks_total (Month= "2 month ago", Priority= "All", Zone= "CableOperators") {}'.format(data_Sum_Two.get('total'))),
('# Three-months'),
('tasks_completed_on_time (Month= "3 month ago", Priority= "Low", Zone= "CableOperators") {}'.format(data_Low_Three1.get('total'))),
('tasks_completed_on_time (Month= "3 month ago", Priority= "Medium", Zone= "CableOperators") {}'.format(data_Medium_Three1.get('total'))),
('tasks_completed_on_time (Month= "3 month ago", Priority= "High", Zone= "CableOperators") {}'.format(data_High_Three1.get('total'))),
('tasks_completed_on_time (Month= "3 month ago", Priority= "Critical", Zone= "CableOperators") {}'.format(data_Critical_Three1.get('total'))),
('tasks_completed_on_time (Month= "3 month ago", Priority= "Blocker", Zone= "CableOperators") {}'.format(data_Blocker_Three1.get('total'))),
('tasks_completed_on_time (Month= "3 month ago", Priority= "All", Zone= "CableOperators") {}'.format(data_Sum_Three1.get('total'))),
('tasks_total (Month= "3 month ago", Priority= "Low", Zone= "CableOperators") {}'.format(data_Low_Three.get('total'))),
('tasks_total (Month= "3 month ago", Priority= "Medium", Zone= "CableOperators") {}'.format(data_Medium_Three.get('total'))),
('tasks_total (Month= "3 month ago", Priority= "High", Zone= "CableOperators") {}'.format(data_High_Three.get('total'))),
('tasks_total (Month= "3 month ago", Priority= "Critical", Zone= "CableOperators") {}'.format(data_Critical_Three.get('total'))),
('tasks_total (Month= "3 month ago", Priority= "Blocker", Zone= "CableOperators") {}'.format(data_Blocker_Three.get('total'))),
('tasks_total (Month= "3 month ago", Priority= "All", Zone= "CableOperators") {}'.format(data_Sum_Three.get('total'))),
('# Four-months'),
('tasks_completed_on_time (Month= "4 month ago", Priority= "Low", Zone= "CableOperators") {}'.format(data_Low_Four1.get('total'))),
('tasks_completed_on_time (Month= "4 month ago", Priority= "Medium", Zone= "CableOperators") {}'.format(data_Medium_Four1.get('total'))),
('tasks_completed_on_time (Month= "4 month ago", Priority= "High", Zone= "CableOperators") {}'.format(data_High_Four1.get('total'))),
('tasks_completed_on_time (Month= "4 month ago", Priority= "Critical", Zone= "CableOperators") {}'.format(data_Critical_Four1.get('total'))),
('tasks_completed_on_time (Month= "4 month ago", Priority= "Blocker", Zone= "CableOperators") {}'.format(data_Blocker_Four1.get('total'))),
('tasks_completed_on_time (Month= "4 month ago", Priority= "All", Zone= "CableOperators") {}'.format(data_Sum_Four1.get('total'))),
('tasks_total (Month= "4 month ago", Priority= "Low", Zone= "CableOperators") {}'.format(data_Low_Four.get('total'))),
('tasks_total (Month= "4 month ago", Priority= "Medium", Zone= "CableOperators") {}'.format(data_Medium_Four.get('total'))),
('tasks_total (Month= "4 month ago", Priority= "High", Zone= "CableOperators") {}'.format(data_High_Four.get('total'))),
('tasks_total (Month= "4 month ago", Priority= "Critical", Zone= "CableOperators") {}'.format(data_Critical_Four.get('total'))),
('tasks_total (Month= "4 month ago", Priority= "Blocker", Zone= "CableOperators") {}'.format(data_Blocker_Four.get('total'))),
('tasks_total (Month= "4 month ago", Priority= "All", Zone= "CableOperators") {}'.format(data_Sum_Four.get('total'))),
('# Five-months'),
('tasks_completed_on_time (Month= "5 month ago", Priority= "Low", Zone= "CableOperators") {}'.format(data_Low_Five1.get('total'))),
('tasks_completed_on_time (Month= "5 month ago", Priority= "Medium", Zone= "CableOperators") {}'.format(data_Medium_Five1.get('total'))),
('tasks_completed_on_time (Month= "5 month ago", Priority= "High", Zone= "CableOperators") {}'.format(data_High_Five1.get('total'))),
('tasks_completed_on_time (Month= "5 month ago", Priority= "Critical", Zone= "CableOperators") {}'.format(data_Critical_Five1.get('total'))),
('tasks_completed_on_time (Month= "5 month ago", Priority= "Blocker", Zone= "CableOperators") {}'.format(data_Blocker_Five1.get('total'))),
('tasks_completed_on_time (Month= "5 month ago", Priority= "All", Zone= "CableOperators") {}'.format(data_Sum_Five1.get('total'))),
('tasks_total (Month= "5 month ago", Priority= "Low", Zone= "CableOperators") {}'.format(data_Low_Five.get('total'))),
('tasks_total (Month= "5 month ago", Priority= "Medium", Zone= "CableOperators") {}'.format(data_Medium_Five.get('total'))),
('tasks_total (Month= "5 month ago", Priority= "High", Zone= "CableOperators") {}'.format(data_High_Five.get('total'))),
('tasks_total (Month= "5 month ago", Priority= "Critical", Zone= "CableOperators") {}'.format(data_Critical_Five.get('total'))),
('tasks_total (Month= "5 month ago", Priority= "Blocker", Zone= "CableOperators") {}'.format(data_Blocker_Five.get('total'))),
('tasks_total (Month= "5 month ago", Priority= "All", Zone= "CableOperators") {}'.format(data_Sum_Five.get('total'))),
('# Six-months'),
('tasks_completed_on_time (Month= "6 month ago", Priority= "Low", Zone= "CableOperators") {}'.format(data_Low_Six1.get('total'))),
('tasks_completed_on_time (Month= "6 month ago", Priority= "Medium", Zone= "CableOperators") {}'.format(data_Medium_Six1.get('total'))),
('tasks_completed_on_time (Month= "6 month ago", Priority= "High", Zone= "CableOperators") {}'.format(data_High_Six1.get('total'))),
('tasks_completed_on_time (Month= "6 month ago", Priority= "Critical", Zone= "CableOperators") {}'.format(data_Critical_Six1.get('total'))),
('tasks_completed_on_time (Month= "6 month ago", Priority= "Blocker", Zone= "CableOperators") {}'.format(data_Blocker_Six1.get('total'))),
('tasks_completed_on_time (Month= "6 month ago", Priority= "All", Zone= "CableOperators") {}'.format(data_Sum_Six1.get('total'))),
('tasks_total (Month= "6 month ago", Priority= "Low", Zone= "CableOperators") {}'.format(data_Low_Six.get('total'))),
('tasks_total (Month= "6 month ago", Priority= "Medium", Zone= "CableOperators") {}'.format(data_Medium_Six.get('total'))),
('tasks_total (Month= "6 month ago", Priority= "High", Zone= "CableOperators") {}'.format(data_High_Six.get('total'))),
('tasks_total (Month= "6 month ago", Priority= "Critical", Zone= "CableOperators") {}'.format(data_Critical_Six.get('total'))),
('tasks_total (Month= "6 month ago", Priority= "Blocker", Zone= "CableOperators") {}'.format(data_Blocker_Six.get('total'))),
('tasks_total (Month= "6 month ago", Priority= "All", Zone= "CableOperators") {}'.format(data_Sum_Six.get('total')))]