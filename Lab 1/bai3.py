tien_ban_dau = 10000 
lai_suat = 0.06                  
# 1.
amount_after_5_years = tien_ban_dau * ((1 + lai_suat)**5)
# 2.
amount_after_10_years = tien_ban_dau * ((1 + lai_suat)**10)
# 3.
growth_rate = (amount_after_10_years - amount_after_5_years) / amount_after_5_years
# 4.
print('Số tiền sẽ có sau 5 năm là:{:.2f}'.format(amount_after_5_years)) 
print("Số tiền sẽ có sau 10 năm là:{:.2f}".format(amount_after_10_years))  
print("Tỷ lệ tăng trưởng của số tiền sau 10 năm so với số tiền sau 5 năm là: {:.2f}".format(growth_rate))
