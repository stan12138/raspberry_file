import math

class FAT12 :
	def __init__(self, filename="a.img", length=1474560):
		self.filename = filename
		self.length = length

		self.zero = b"\x00"

		self.sector_length = 512
		self.sector_begin = 2
		self.fat1_sector = 1
		self.fat2_secotr = 10
		self.dir_sector = 14
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
		
		fat_table = self.generate_fat_table(loader_length)

		dir_table = self.generat_dir(loader_name, loader_length)

		all_content = fat_table + fat_table + dir_table + loader_content

		all_content_and_empty = all_content + self.zero*(self.length-self.sector_length-len(all_content))

		with open(self.filename, "rb") as fi:
			c = fi.read()

		with open(self.filename, "wb") as fi :
			length = fi.write(c[:512]+all_content_and_empty)

		print("write %s bytes"%length)
		


	def generate_fat_table(self, loader_length) :
		#如何解析生成FAT表？
		loader_sector_num = math.ceil(loader_length/self.sector_length)
		fat_sector_list = list(range(self.data_sector_begin+1, self.data_sector_begin+loader_sector_num))
		fat_sector_list.append(0xfff)
		if len(fat_sector_list)%2==1 :
			fat_sector_list.append(0x000)

		label_num = len(fat_sector_list)

		print(label_num)

		fat_content = b""

		for i in range(int(label_num/2)) :
			a = fat_sector_list[2*i]
			b = fat_sector_list[2*i+1]

			a1 = a & 0x0ff
			a2 = a >> 8

			b1 = b & 0xff0
			b2 = b & 0x00f
			b2 = b2 << 4

			fat_content += a1.to_bytes(1, byteorder="little")
			fat_content += (b2+a2).to_bytes(1, byteorder="little")
			fat_content += b1.to_bytes(1, byteorder="little")


		fat_length = self.fat_sector_num*self.sector_length

		fat_used = b"\x00\x00\x00" + fat_content

		return fat_used + self.zero*(fat_length-len(fat_used))



	def generat_dir(self, loader_name, loader_length) :
		name = loader_name[:loader_name.index(".")].upper().encode("ascii")
		suffix = loader_name[loader_name.index(".")+1:].upper().encode("ascii")

		if len(name)>8 or len(suffix)>3 :
			print("file name too long")
			return False

		dir_length = self.sector_length*self.dir_sector

		name_byte = name + b"\x20"*(8-len(name))
		suffix_byte = suffix + b"\x20"*(3-len(suffix))

		file_attri = b"\x20"

		keep_content = self.zero*10

		time_content = self.zero*2
		date_content = self.zero*2

		sector_begin_content = self.data_sector_begin.to_bytes(2, byteorder="little")
		#首簇号从2开始
		length_content = loader_length.to_bytes(4, byteorder="little")

		dir_used = name_byte+suffix_byte+file_attri+keep_content+time_content+date_content+sector_begin_content+length_content

		return dir_used + self.zero*(dir_length-len(dir_used))