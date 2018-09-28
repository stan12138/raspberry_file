import math

class FAT12 :
	def __init__(self, filename="a.img", length="1474560"):
		self.filename = filename
		self.length = length

		self.zero = b"\x00"

		self.sector_length = 512
		self.sector_begin = 2
		self.fat1_sector = 1
		self.fat2_secotr = 10
		self.dir_sector = 19
		self.data_sector = 33

		self.data_sector_begin = 2
		self.fat_sector_num = 9

	def create_empty_img(self) :
		content = self.zero*self.length
		with open(self.filename, "wb") as fi :
			fi.write(content)

	def set_mbr(self, mbr_name) :
		with open(mbr_name, "rb") as fi :
			header = fi.read()

		content = header + self.zero*(self.length-len(header))

		with open(self.filename, "wb") as img_name :
			img_name.write(content)

	def add_file(self, loader_name) :
		with open(loader_name, "rb") as fi :
			loader_content = fi.read()

		loader_length = len(loader_content)
		



		loader_sector_list = list(range(self.data_sector, loader_sector_num))

		


	def generate_fat_table(self, loader_length) :
		#如何解析生成FAT表？
		loader_sector_num = math.ceil(loader_length/self.sector_length)
		fat_sector_list = list(range(self.data_sector_begin+1, self.data_sector_begin+loader_sector_num))
		fat_length = self.fat_sector_num*self.sector_length

		fat_begin = b"\x00\x00\x00"






	def generat_dir(self, loader_name, loader_length) :
		name = loader_name[:loader_name.index(".")].upper().encode("ascii")
		suffix = loader_name[loader_name.index(".")+1:].upper().encode("ascii")

		if len(name)>8 or len(suffix)>3 :
			print("file name too long")
			return False

		name_byte = name + b"\x20"*(8-len(name))
		suffix_byte = suffix + b"\x20"*(3-len(suffix))

		file_attri = b"\x20"

		keep_content = self.zero*10

		time_content = self.zero*2
		date_content = self.zero*2

		sector_begin_content = self.data_sector_begin.to_bytes(2, byteorder="little")
		#首簇号从2开始
		length_content = loader_length.to_bytes(4, byteorder="little")

		return name_byte+suffix_byte+file_attri+keep_content+time_content+date_content+sector_begin_content+length_content