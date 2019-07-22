data=[]
count = 0
with open('reviews.txt', 'r') as f :
	for line in f :
		data.append(line)
		count += 1 
		if count % 1000 == 0:
			print(len(data)) # 每讀1000筆顯示一次
print(data[0])
print('---------------')
print(data[1])
