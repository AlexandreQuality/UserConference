import os

pasta = r'file:///C:/AutomationEdge/WorkSpace/AE/UserConference'.replace('file:///','')

log_message=''
delete=[]

files_list =os.listdir(pasta)
if 'brio_totals - Sheet1.csv' in files_list:
    for file in files_list:
        if 'brio_totals - Sheet1.csv' in file:
            destino= fr'{pasta}/{file}'
            os.remove(destino)
            log_message=f'Removido:  {file}'
    
    
else: log_message = 'Arquivo Não Encontrado'

print(log_message)