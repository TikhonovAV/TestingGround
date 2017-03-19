# -*- coding: utf-8 -*-

import os
from datetime import datetime

files_path = 'c:\\share\\'
os.chdir(files_path)

for p, d, f in os.walk(files_path):
    for file_name in f:
        file_time_change = datetime.fromtimestamp(os.path.getmtime(os.path.join(p, file_name)))
        if file_name.endswith(".xml") and datetime.date(file_time_change) < datetime.today().date():
            catalog_name_full = os.path.dirname(os.path.join(p, file_name))
            print(os.path.join(p, file_name), file_time_change)
            print(os.path.dirname(os.path.join(p, file_name)))
            index_of_splash = catalog_name_full.rfind("\\") + 1
            print(catalog_name_full[index_of_splash:] + '_' + str(datetime.date(file_time_change)))
            archive_name = catalog_name_full[index_of_splash:] + '_' + str(datetime.date(file_time_change))
            archive_name_full = catalog_name_full + "\\" + archive_name + ".rar"
            print(archive_name_full)
            print(file_time_change.strftime("%d-%m-%Y"))
#            os.system(r'c:/"Program Files"/"winrar"/rar.exe a -ep1 '+ archive_name_full + ' ' + os.path.join(p, file_name))
