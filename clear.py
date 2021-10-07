import os
pasta = 'file:///C:/AutomationEdge/WorkSpace/AE/UserConference'.replace('file:///','')
delete=[]
files_list =os.listdir(pasta)
for file in files_list:
    if '.csv' in file:
        delete.append(os.remove(file))

