import sqlite3


sql = {
    'mod_files': """
            CREATE TABLE "mod_files" (
            "mod_id"	TEXT NOT NULL,
            "file_name"	TEXT NOT NULL UNIQUE,
            "picture"	TEXT,
            "file_tr_status"	INTEGER DEFAULT 0,
            "file_name_pointer_pos"	INTEGER DEFAULT 0,
            "language"	TEXT,
            "original_name"	TEXT UNIQUE,
            "full_path"	TEXT,
            "mod_name"	TEXT,
            "folder_path"	TEXT,
            "cutter_file_name"	TEXT,
            "translated_name"	TEXT,
            "cuttered"	TEXT,
            "translated_file"	TEXT,
            "machine_text"	TEXT,
            "status" TEXT,
            "base_dir" TEXT,
            "id" TEXT

            )
        """
}


collection_queries = {
    'save_mod_status': """
        INSERT OR REPLACE INTO mod_files (
                              mod_id,
                              file_name,
                              picture,
                              file_tr_status,
                              file_name_pointer_pos,
                              language,
                              original_name,
                              full_path,
                              mod_name,
                              folder_path,
                              cutter_file_name,
                              translated_name,
                              cuttered,
                              translated_file,
                              machine_text,
                              status,
                              base_dir,
                              id) VALUES(
                              @mod_id, 
                              @file_name,
                              @picture,
                              @file_tr_status,
                              @file_name_pointer_pos,
                              @language,
                              @original_name,
                              @full_path,
                              @mod_name,
                              @folder_path,
                              @cutter_file_name,
                              @translated_name,
                              @cuttered,
                              @translated_file,
                              @machine_text,
                              @status,
                              @base_dir,
                              @id
                              )
    """,
    'set_other_mods': """
        INSERT OR IGNORE INTO mod_files (
                              mod_id,
                              file_name,
                              original_name,
                              mod_name,
                              status,
                              id) VALUES(
                              @mod_id, 
                              @file_name,
                              @original_name,
                              @mod_name,
                              @status,
                              @id
                              )
    """,
    'get_info': 'SELECT * from mod_files'
}


class Mod:
    def __init__(self, mod_id, mod_name):
        self.mod_id = mod_id
        self.mod_name = mod_name,
        self.base_dir = None
        self.files = {}
        self.hashKey = ''


def write_data_in_collection(db_path, data):
    mod_info = data[0]
    file_name_list = data[1]
    with sqlite3.connect(db_path) as conn:
        conn.execute(collection_queries['save_mod_status'],
                     (
                         mod_info['mod_id'],
                         mod_info['file_name'],
                         mod_info['picture'],
                         mod_info['file_tr_status'],
                         mod_info['file_name_pointer_pos'],
                         mod_info['language'],
                         mod_info['original_name'],
                         mod_info['full_path'],
                         mod_info['mod_name'],
                         mod_info['folder_path'],
                         mod_info['cutter_file_name'],
                         mod_info['translated_name'],
                         mod_info['cuttered'],
                         mod_info['translated_file'],
                         mod_info['machine_text'],
                         mod_info['status'],
                         mod_info['base_dir'],
                         mod_info['id']
                     )
                     )
        conn.commit()
        if file_name_list:
            for file_name in file_name_list:
                conn.execute(collection_queries['set_other_mods'],
                             (
                                 mod_info['mod_id'],
                                 file_name,
                                 file_name,
                                 mod_info['mod_name'],
                                 mod_info['status'],
                                 mod_info['id']
                             )
                             )
            conn.commit()


def get_data_from_collection(db_path):
    mods = {}
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        raw_data = c.execute(collection_queries['get_info']).fetchall()
        for elem in raw_data:
            data = {}
            try:
                mod = mods[elem[0]]
                if elem[16] and not mod.base_dir:
                    mod.base_dir = elem[16]
            except KeyError:
                mod = Mod(elem[0], elem[8])
                if elem[16] and not mod.base_dir:
                    mod.base_dir = elem[16]
                mod.hashKey = elem[17]
                mods[elem[0]] = mod
            mod.files[elem[1]] = {
                'mod_id': elem[0],
                'file_name': elem[1],
                'picture': elem[2],
                'file_tr_status': elem[3],
                'file_name_pointer_pos': elem[4],
                'language': elem[5],
                'original_name': elem[6],
                'full_path': elem[7],
                'mod_name': elem[8],
                'folder_path': elem[9],
                'cutter_file_name': elem[10],
                'translated_name': elem[11],
                'cuttered': elem[12],
                'translated_file': elem[13],
                'machine_text': elem[14],
                'status': elem[15],
                'base_dir': elem[16],
                'id': elem[17]
            }
    return mods


def create_db(db_path):
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        create_table(conn, 'mod_files')
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def create_table(conn, sql_key):
    try:
        c = conn.cursor()
        c.execute(sql[sql_key])
    except sqlite3.Error as e:
        print(e)
