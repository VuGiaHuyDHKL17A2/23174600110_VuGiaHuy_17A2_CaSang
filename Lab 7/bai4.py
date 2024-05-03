inventory = { 'gold' : 500, 'pouch' : ['flint', 'twine', 'gemstone'], 'backpack' : ['xylophone','dagger', 'bedroll','bread loaf'] }

# Thêm key 'pocket'
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

# Sắp xếp các phần tử trong 'backpack'
inventory['backpack'].sort()

# Loại bỏ biến 'dagger'
inventory['backpack'].remove('dagger')

# Thêm giá trị 50 vào 'gold'
inventory['gold'] += 50

# In ra dictionary sau khi thay đổi
print(inventory)
