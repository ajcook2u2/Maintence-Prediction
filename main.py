import pandas as pd
# import Pyarrow

train_FD001 = pd.read_csv('CMAPSSData/train_FD001.txt', sep='\s+')
train_FD002 = pd.read_csv('CMAPSSData/train_FD002.txt', sep='\s+')
train_FD003 = pd.read_csv('CMAPSSData/train_FD003.txt', sep='\s+')
train_FD004 = pd.read_csv('CMAPSSData/train_FD004.txt', sep='\s+')

test_FD001 = pd.read_csv('CMAPSSData/test_FD001.txt', sep='\s+')
test_FD002 = pd.read_csv('CMAPSSData/test_FD002.txt', sep='\s+')
test_FD003 = pd.read_csv('CMAPSSData/test_FD003.txt', sep='\s+')
test_FD004 = pd.read_csv('CMAPSSData/test_FD004.txt', sep='\s+')

new_columns = ['Unit Number', 'Time(cycles)', 'Operational Setting 1', 'Operational Setting 2', 'Operational Setting 3',
           'Sensor Measurement 1', 'Sensor Measurement 2', 'Sensor Measurement 3', 'Sensor Measurement 4',
           'Sensor Measurement 5', 'Sensor Measurement 6', 'Sensor Measurement 7', 'Sensor Measurement 8',
           'Sensor Measurement 9', 'Sensor Measurement 10', 'Sensor Measurement 11', 'Sensor Measurement 12',
           'Sensor Measurement 13', 'Sensor Measurement 14', 'Sensor Measurement 15', 'Sensor Measurement 16',
           'Sensor Measurement 17', 'Sensor Measurement 18', 'Sensor Measurement 19', 'Sensor Measurement 20',
           'Sensor Measurement 21']


new_row = pd.DataFrame([train_FD004.columns.tolist()], columns=train_FD004.columns)
train_FD004 = pd.concat([new_row, train_FD004], ignore_index=True)
train_FD004.columns = new_columns
for i in train_FD004.columns:
    train_FD004.at[0, i] = float(train_FD004.at[0, i])
train_FD004 = train_FD004.sort_values(by=['Unit Number', 'Time(cycles)'])

new_row = pd.DataFrame([train_FD001.columns.tolist()], columns=train_FD001.columns)
train_FD001 = pd.concat([new_row, train_FD001], ignore_index=True)
print(train_FD001.columns)
train_FD001.columns = new_columns
for i in train_FD001.columns:
    train_FD001.at[0, i] = float(train_FD001.at[0, i])
train_FD001 = train_FD001.sort_values(by=['Unit Number', 'Time(cycles)'])

new_row = pd.DataFrame([train_FD002.columns.tolist()], columns=train_FD002.columns)
train_FD002 = pd.concat([new_row, train_FD002], ignore_index=True)
train_FD002.columns = new_columns
for i in train_FD002.columns:
    train_FD002.at[0, i] = float(train_FD002.at[0, i])
train_FD002 = train_FD002.sort_values(by=['Unit Number', 'Time(cycles)'])

new_row = pd.DataFrame([train_FD003.columns.tolist()], columns=train_FD003.columns)
train_FD003 = pd.concat([new_row, train_FD003], ignore_index=True)
train_FD003.columns = new_columns
for i in train_FD003.columns:
    train_FD003.at[0, i] = float(train_FD003.at[0, i])
train_FD003 = train_FD003.sort_values(by=['Unit Number', 'Time(cycles)'])



new_row = pd.DataFrame([test_FD001.columns.tolist()], columns=test_FD001.columns)
test_FD001 = pd.concat([new_row, test_FD001], ignore_index=True)
test_FD001.columns = new_columns
for i in test_FD001.columns:
    test_FD001.at[0, i] = float(test_FD001.at[0, i])
test_FD001 = test_FD001.sort_values(by=['Unit Number', 'Time(cycles)'])

new_row = pd.DataFrame([test_FD004.columns.tolist()], columns=test_FD004.columns)
test_FD004 = pd.concat([new_row, test_FD004], ignore_index=True)
print(test_FD004.columns)
test_FD004.columns = new_columns
for i in test_FD004.columns:
    test_FD004.at[0, i] = float(test_FD004.at[0, i])
test_FD004 = test_FD004.sort_values(by=['Unit Number', 'Time(cycles)'])

new_row = pd.DataFrame([test_FD002.columns.tolist()], columns=test_FD002.columns)
test_FD002 = pd.concat([new_row, test_FD002], ignore_index=True)
test_FD002.columns = new_columns
for i in test_FD002.columns:
    test_FD002.at[0, i] = float(test_FD002.at[0, i])
test_FD002 = test_FD002.sort_values(by=['Unit Number', 'Time(cycles)'])


new_row = pd.DataFrame([test_FD003.columns.tolist()], columns=test_FD003.columns)
test_FD003 = pd.concat([new_row, test_FD003], ignore_index=True)
test_FD003.columns = new_columns
for i in test_FD002.columns:
    test_FD002.at[0, i] = float(test_FD002.at[0, i])
test_FD002 = test_FD002.sort_values(by=['Unit Number', 'Time(cycles)'])



y = 1
fault_train_FD001 = []
for i in train_FD001['Unit Number']:
    x = i
    if x != y:
        fault_train_FD001.append(1)
    else:
        fault_train_FD001.append(0)
    y = x

fault_train_FD001[0] = 0
fault_train_FD001[1] = 0
fault_train_FD001[len(fault_train_FD001) - 1] = 1
train_FD001['Fault'] = fault_train_FD001


y = 1
fault_train_FD002 = []
for i in train_FD002['Unit Number']:
    x = i
    if x != y:
        fault_train_FD002.append(1)
    else:
        fault_train_FD002.append(0)
    y = x

fault_train_FD002[0] = 0
fault_train_FD002[1] = 0
fault_train_FD002[len(fault_train_FD002) - 1] = 1
train_FD002['Fault'] = fault_train_FD002

y = 1
fault_train_FD003 = []
for i in train_FD003['Unit Number']:
    x = i
    if x != y:
        fault_train_FD003.append(1)
    else:
        fault_train_FD003.append(0)
    y = x

fault_train_FD003[0] = 0
fault_train_FD003[1] = 0
fault_train_FD003[len(fault_train_FD003) - 1] = 1
train_FD003['Fault'] = fault_train_FD003

y = 1
fault_train_FD004 = []
for i in train_FD004['Unit Number']:
    x = i
    if x != y:
        fault_train_FD004.append(1)
    else:
        fault_train_FD004.append(0)
    y = x

fault_train_FD004[0] = 0
fault_train_FD004[1] = 0
fault_train_FD004[len(fault_train_FD004) - 1] = 1
train_FD004['Fault'] = fault_train_FD004


y = 1
fault_test_FD001 = []
for i in test_FD001['Unit Number']:
    x = i
    if x != y:
        fault_test_FD001.append(1)
    else:
        fault_test_FD001.append(0)
    y = x

fault_test_FD001[0] = 0
fault_test_FD001[1] = 0
fault_test_FD001[len(fault_test_FD001) - 1] = 1
test_FD001['Fault'] = fault_test_FD001

y = 1
fault_test_FD002 = []
for i in test_FD002['Unit Number']:
    x = i
    if x != y:
        fault_test_FD002.append(1)
    else:
        fault_test_FD002.append(0)
    y = x

fault_test_FD002[0] = 0
fault_test_FD002[1] = 0
fault_test_FD002[len(fault_test_FD002) - 1] = 1
test_FD002['Fault'] = fault_test_FD002

y = 1
fault_test_FD003 = []
for i in test_FD003['Unit Number']:
    x = i
    if x != y:
        fault_test_FD003.append(1)
    else:
        fault_test_FD003.append(0)
    y = x

fault_test_FD003[0] = 0
fault_test_FD003[1] = 0
fault_test_FD003[len(fault_test_FD003) - 1] = 1
test_FD003['Fault'] = fault_test_FD003

y = 1
fault_test_FD004 = []
for i in test_FD004['Unit Number']:
    x = i
    if x != y:
        fault_test_FD004.append(1)
    else:
        fault_test_FD004.append(0)
    y = x

fault_test_FD004[0] = 0
fault_test_FD004[1] = 0
fault_test_FD004[len(fault_test_FD004) - 1] = 1
test_FD004['Fault'] = fault_test_FD004
