data=[]
count = 0
message = 0
with open('reviews.txt', 'r') as f :
	for line in f :
		data.append(line)
		count += 1 
		message = message + len(line)
		if count % 1000 == 0:
			print(len(data)) # 每讀1000筆顯示一次
print('檔案讀取完畢,總共有', len(data), '筆資料')
print('留言平均長度為', message/len(data))