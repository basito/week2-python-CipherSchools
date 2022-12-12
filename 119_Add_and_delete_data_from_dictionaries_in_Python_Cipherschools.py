user_info={
    'name':'harshit',
    'age':24,
    'fav-movies':['coco','kimi no na wa'],
    'fav-tunes':['awakening','fairy tale'],
}

user_info['fav_songs']=['song1','song2']
print(user_info)

popped_itemuser_info.pop('age')
prinnt(type(popped_item))
print(user_info)

popped_item=user_info.popitem()
print(user_info)
print(type(popped_item))