from os.path import dirname, join


class f24_read_write_file:

    def __init__(self):
        project_root = dirname(dirname(__file__))
        # 設定專案讀寫檔案路徑
        self._path = join(project_root, 'flightradar24', 'f24_data')

    def search_f24_file_id(self, seach_flight_id):
        #
        file_path = join(self._path,'Flight_Record.txt')
        try:
            file = open(file_path, 'r')
            data = file.read()
            file.close()
        except:
            file = open(file_path, 'w')
            file.write("__init__\n")
            file.close()
        #
        return data.find(seach_flight_id)

    # 航班紀錄寫入json
    def write_json(self, file_name, flight_record_data):
        # 紀錄以抓取航班ID
        # json_file path
        new_file_name = file_name + '.json'
        json_file_path = join(self._path, new_file_name)
        #
        try:
            file = open(json_file_path, "w")
            file.write(flight_record_data)
            file.close()
            self.record_file(file_name)
        except:
            pass
    #
    # 紀錄寫入航班id
    def record_file(self, flight_id):
        file_path = join(self._path, 'Flight_Record.txt')
        try:
            file = open(file_path, "a")
            file.write('%s \n' % flight_id)
            file.close()
        except:
            pass