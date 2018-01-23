a = '''srcip STRING
srcport NUMERIC
dstip STRING
dstport NUMERIC
proto NUMERIC
total_fpackets NUMERIC
total_fvolume NUMERIC
total_bpackets NUMERIC
total_bvolume NUMERIC
min_fpktl NUMERIC
mean_fpktl NUMERIC
max_fpktl NUMERIC
std_fpktl NUMERIC
min_bpktl NUMERIC
mean_bpktl NUMERIC
max_bpktl NUMERIC
std_bpktl NUMERIC
min_fiat NUMERIC
mean_fiat NUMERIC
max_fiat NUMERIC
std_fiat NUMERIC
min_biat NUMERIC
mean_biat NUMERIC
max_biat NUMERIC
std_biat NUMERIC
duration NUMERIC
min_active NUMERIC
mean_active NUMERIC
max_active NUMERIC
std_active NUMERIC
min_idle NUMERIC
mean_idle NUMERIC
max_idle NUMERIC
std_idle NUMERIC
sflow_fpackets NUMERIC
sflow_fbytes NUMERIC
sflow_bpackets NUMERIC
sflow_bbytes NUMERIC
fpsh_cnt NUMERIC
bpsh_cnt NUMERIC
furg_cnt NUMERIC
burg_cnt NUMERIC
total_fhlen NUMERIC
total_bhlen NUMERIC
dscp NUMERIC'''

b = {}
a = a.split("\n")
for i in range(len(a)):
    b[a[i].split()[0]]=i
for key in b:
    exec(key + '=b[key]')