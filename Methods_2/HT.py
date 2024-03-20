def hash(info):
	'''
	Подсчет хеша
	
	:param info: Данные
	:type info: str
	'''
	a = 8949
	val = 0
	for i in info:
		val += a * ord(i)
	return val % 666

def add(obj, hash_table):
	'''
	Добавление записи
	
	:param obj: Данные на запись
	:type obj: People
	:param hash_table: Хеш Таблица
	:type hash_table: int
	'''
	h = hash(obj.name)
	if len(hash_table) > h:
		hash_table[h].append(obj)
		return
	while len(hash_table) <= h:
		hash_table.append([])
	hash_table[h].append(obj)
	return

def collision_num(hash_table):
	'''
	Подсчет коллизий

	:param hash_table: Хеш Таблица
	:type hash_table: int
	'''
	col = 0
	for i in hash_table:
		if len(hash_table) > 1:
			col += 1		
	return col

def search_HT(key, hash_table):
	'''
	Поиск записи

	:param key: Ключ записи для поиска
	:type key: str
	:param hash_table: Хеш Таблица
	:type hash_table: int
	'''
	h = hash(key)
	if len(hash_table[h]) != 1:
		for i in hash_table[h]:
			if i.name == key:
				return i
	else:
		return hash_table[h][0]