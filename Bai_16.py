diem_sinh_vien = {'An': 8, 'Long': 9, 'Tam': 7, 'Tung': 10}
list = sorted(diem_sinh_vien.items(),key=lambda x: x[1],reverse=True)
print(list)