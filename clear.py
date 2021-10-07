import os

pasta = r'file:///C:/AutomationEdge/WorkSpace/AE/UserConference'.replace('file:///','')

log_message=''
delete=[]

files_list =os.listdir(pasta)
print(files_list)


for file in files_list:
    if '.csv' in file:
        delete.append(os.remove(file))
log_message='True'