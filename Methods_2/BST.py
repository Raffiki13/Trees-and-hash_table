class Node:
	'''
	Класс Ноды
	
	:param key: Ключ значения
	:type key: str
	:param value: Значение
	:type value: People
	'''
	def __init__(self, key, value):
		'''
		Конструктор
		'''
		self.key = key
		self.values = [value]
		self.left = None
		self.right = None
	
def create_tree(data):
	'''
	Создание дерева из данных
	
	:param data: Массив данных
	:type data: People
	'''
	for i in range(len(data)):
		if i == 0:
			root = Node(data[i].name, data[i])
			continue
		tmp = root
		while True:
			if tmp.key == data[i].name:
				tmp.values.append(data[i])
				break
			if data[i].name < tmp.key:
				if tmp.left == None:
					tmp.left = Node(data[i].name, data[i])
					break
				else:
					tmp = tmp.left
					continue
			if data[i].name > tmp.key:
				if tmp.right == None:
					tmp.right = Node(data[i].name, data[i])
					break
				else:
					tmp = tmp.right
					continue
	return root

def search_BST(root, key):
	'''
	Поиск по бинарному дереву
	:param root: Указатель на начало
	:type root: ptr
	:param key: Ключ который ищем
	:type key: People
	'''
	if root.key == key:
		return root.values
	if key < root.key:
		return search_BST(root.left, key)
	if key > root.key:
		return search_BST(root.right, key)
