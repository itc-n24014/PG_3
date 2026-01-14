# 書き込みモードでオープン(中身は上書きされる)
write_file = open('write.txt', 'w' , encoding = 'utf-8')
write_file.write("Hi, Linux.\n")
write_file.close()

# アドベントモードでオープン(中身に追記される)
write_file = open('write.txt', 'a')
write_file.write("Happy new year!\n")
write_file.close()