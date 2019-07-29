#打開txt讀取留言
data=[]
count = 0
message = 0
with open('reviews.txt', 'r') as f :
	for line in f :
		data.append(line)
		count += 1 
		message = message + len(line)
		if count % 10000 == 0:
			print(len(data)) # 每讀10000筆顯示一次
print('檔案讀取完畢,總共有', len(data), '筆資料')
print('留言平均長度為', message/len(data))
print(data[0])

#篩選留言字數
new = []
for d in data :
	if len(d) < 100 :
		new.append(d)
print('一共有', len(new), '筆留言小於100')
print(new[0])

good = []
for d in data :
	if 'good' in d :
		good.append(d)
# good = [d for d in data if 'good' in d] 上面的快寫法


#計算留言文字記數
wc = {}
for d in data:
	words = d.strip().split()
	for word in words:
		if word in wc:
			wc[word] = wc[word] + 1
		else:
			wc[word] = 1


while True:
	s = input('請問你想查詢什麼關鍵字(q離開):')	
	if s == 'q':
		break
	elif s in wc:
		print(s, wc[s])
	else  :
		print('無此關鍵字')










