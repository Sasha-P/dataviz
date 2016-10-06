#DataViz

Data Visualization Web Application

The user can upload a file with data to visualize it.

App supports *.csv, *.json and *.xls file formats.

###CSV file structure
```csv
Регион,Страна,Значение
ЕС-27,Италия,5
ЕС-27,Польша,9
...
```

If the third row entry (`Значение` column) can't be converted to digits, the whole row will be ignored.

For example, row `Регион,Страна,Значение` will be ignored.

###JSON file structure
```json
{"data": [ {
    "Регион":"ЕС-27",
    "Страна":"Италия",
    "Значение":5
  },{
    "Регион":"ЕС-27",
    "Страна":"Польша",
    "Значение":9
  },
  ...
] }
```

###XLS file structure
```xls
Регион|Страна |Значение
-----------------------
ЕС-27 |Италия |5
-----------------------
ЕС-27 |Польша |9
-----------------------
...
```

One spreadsheet that contains three columns.

If the third row entry (`Значение` column) can't be converted to digits, the whole row will be ignored.

###Examples
You may find examples of files in the `examples` directory.

##Instalation
0. set up a virtual environment with `python3.5`
1. clone the repo
2. run `pip install -r /path/to/repo_clon/requirements/production`
3. provide `SECRET_KEY`
4. run `./manage.py migrate`
5. create superuser `./manage.py createsupruser` and follow the instructions
6. enjoy!

##License
Written by Sasha.

This program is licensed under the MIT License (see `LICENSE.txt`)

#DISCLAIMER

**ALL COPYRIGHTS BELONG TO THEIR RESPECTIVE OWNERS**
