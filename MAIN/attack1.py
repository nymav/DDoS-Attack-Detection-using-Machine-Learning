import os 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import time 

# reading features list 
with open("kddcup.names", 'r') as f: 
	 f.read()
#Appending columns to the dataset and adding a new column name ‘target’ to the dataset. 
cols ="""duration, 
protocol_type, 
service, 
flag, 
src_bytes, 
dst_bytes, 
land, 
wrong_fragment, 
urgent, 
hot, 
num_failed_logins, 
logged_in, 
num_compromised, 
root_shell, 
su_attempted, 
num_root, 
num_file_creations, 
num_shells, 
num_access_files, 
num_outbound_cmds, 
is_host_login, 
is_guest_login, 
count, 
srv_count, 
serror_rate, 
srv_serror_rate, 
rerror_rate, 
srv_rerror_rate, 
same_srv_rate, 
diff_srv_rate, 
srv_diff_host_rate, 
dst_host_count, 
dst_host_srv_count, 
dst_host_same_srv_rate, 
dst_host_diff_srv_rate, 
dst_host_same_src_port_rate, 
dst_host_srv_diff_host_rate, 
dst_host_serror_rate, 
dst_host_srv_serror_rate, 
dst_host_rerror_rate, 
dst_host_srv_rerror_rate"""

columns =[] 
for c in cols.split(', '): 
	if(c.strip()): 
	  columns.append(c.strip()) 

columns.append('target') 
#print(len(columns)) 

#Reading the ‘attack_types’ file.
with open("training_attack_types", 'r') as f: 
	f.read()
#Creating a dictionary of attack_types
 
attacks_types = { 
	'normal': 'normal', 
'back': 'dos', 
'buffer_overflow': 'u2r', 
'ftp_write': 'r2l', 
'guess_passwd': 'r2l', 
'imap': 'r2l', 
'ipsweep': 'probe', 
'land': 'dos', 
'loadmodule': 'u2r', 
'multihop': 'r2l', 
'neptune': 'dos', 
'nmap': 'probe', 
'perl': 'u2r', 
'phf': 'r2l', 
'pod': 'dos', 
'portsweep': 'probe', 
'rootkit': 'u2r', 
'satan': 'probe', 
'smurf': 'dos', 
'spy': 'r2l', 
'teardrop': 'dos', 
'warezclient': 'r2l', 
'warezmaster': 'r2l', 
} 
#Reading the dataset(‘kddcup.data_10_percent.gz’) and adding 
#Attack Type feature in the training dataset where attack type feature has 5 distinct values i.e. dos, normal, probe, r2l, u2r.	
path = "kddcup.data_10_percent.gz"
df = pd.read_csv(path, names = columns) 

# Adding Attack Type column 
df['Attack Type'] = df.target.apply(lambda r:attacks_types[r[:-1]]) 
#print(df.head())
df.shape
#Finding missing values of all features
#print(df.isnull().sum())

#Finding Categorical Features
num_cols = df._get_numeric_data().columns 

cate_cols = list(set(df.columns)-set(num_cols)) 
cate_cols.remove('target') 
cate_cols.remove('Attack Type') 
#print(cate_cols)

# Data Correlation – Find the highly correlated variables using heatmap and ignore them for analysis
df = df.dropna('columns')# drop columns with NaN 
df = df[[col for col in df if df[col].nunique() > 1]]# keep columns where there are more than 1 unique values 
corr = df.corr() 
plt.figure(figsize =(15, 12)) 
sns.heatmap(corr) 
plt.show()
##Note: The white colored boxes in the heat map,indicates the highly correlated columns, and these columns can be dropped for further analysis.



