a = list(range(1,100))

page = 1
per_page = 5
while page < 11 :
  start = (page -1)*per_page
  end = start + per_page

  print(a[start:end])
  page += 1
