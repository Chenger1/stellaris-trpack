# TODO Replace values of queries by = ?
"""
                              ↓ Инициализация данных ↓
"""

import sqlite3


sql = {
    'mod_files': """
            CREATE TABLE "mod_files" 
            (
            "mod_id"	                TEXT NOT NULL,
            "hash_key"                  TEXT NOT NULL,
            "mod_name"                  TEXT NOT NULL,
            "target_language"	        TEXT NOT NULL,
            "original_file_name"	    TEXT NOT NULL,
            "original_file_path"	    TEXT UNIQUE,
            "source_file_path"	        TEXT UNIQUE,
            "machine_file_path"         TEXT UNIQUE,
            "user_input_file_path"	    TEXT UNIQUE,
            "tr_status"	                INTEGER DEFAULT 0,
            "pointer_pos"	            INTEGER DEFAULT 0
            )
        """
}


collection_queries = {
    'insert_mod_data': """
        INSERT INTO mod_files
            (
                              mod_id,
                              hash_key,
                              mod_name,
                              target_language,
                              original_file_name,
                              original_file_path,
                              source_file_path,
                              machine_file_path,
                              user_input_file_path
            )
        VALUES
            (
                              @mod_id, 
                              @hash_key,
                              @mod_name,
                              @target_language,
                              @original_file_name,
                              @original_file_path,
                              @source_file_path,
                              @machine_file_path,
                              @user_input_file_path
            )
    """,
    'update_file_data': """
        UPDATE mod_files
            SET tr_status = ?,
                pointer_pos = ?
            WHERE original_file_name = ?;
    """,
    'get_mods_data': 'SELECT * from mod_files'
}


def create_table(conn, sql_key):
    try:
        c = conn.cursor()
        c.execute(sql[sql_key])
    except sqlite3.Error as e:
        print(e)


def db_init(collection_path):
    conn = None
    try:
        conn = sqlite3.connect(collection_path)
        create_table(conn, 'mod_files')
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


"""
                                ↓ Запись данных ↓
"""


def write_data_in_collection(collection_path, mod_info):
    with sqlite3.connect(collection_path) as conn:
        conn.execute(collection_queries['insert_mod_data'],
                     (
                         mod_info['mod_id'],
                         mod_info['hash_key'],
                         mod_info['mod_name'],
                         mod_info['target_language'],
                         mod_info['original_file_name'],
                         mod_info['original_file_path'],
                         mod_info['source_file_path'],
                         mod_info['machine_file_path'],
                         mod_info['user_input_file_path']
                      )
                     )
        conn.commit()


def update_data_in_collection(collection_path, file):
    with sqlite3.connect(collection_path) as conn:
        conn.execute(collection_queries['update_file_data'],
                     (
                         file.tr_status,
                         file.pointer_pos,
                         file.original_file_name
                      )
                     )
        conn.commit()


"""
                                ↓ Чтение данных ↓
"""


class File:
    def __init__(self,
                 mod_id, hash_key, mod_name, target_language, original_file_name,
                 original_file_path, source_file_path, machine_file_path, user_input_file_path,
                 tr_status, pointer_pos
                 ):
        self.mod_id = mod_id
        self.hash_key = hash_key
        self.mod_name = mod_name
        self.target_language = target_language
        self.original_file_name = original_file_name
        self.original_file_path = original_file_path
        self.source_file_path = source_file_path
        self.machine_file_path = machine_file_path
        self.user_input_file_path = user_input_file_path
        self.tr_status = tr_status
        self.pointer_pos = pointer_pos
        self.type = '.yml' if '.yml' in original_file_name else '.txt'


def get_data_from_collection(collection_path):
    files = {}
    with sqlite3.connect(collection_path) as conn:
        c = conn.cursor()
        file_data = c.execute(collection_queries['get_mods_data']).fetchall()
        for elem in file_data:
            file = File(
                        elem[0], elem[1], elem[2], elem[3], elem[4],
                        elem[5], elem[6], elem[7], elem[8],
                        elem[9], elem[10]
                        )
            if elem[0] not in files:
                files[elem[0]] = [file, ]
            else:
                files[elem[0]].append(file, )
    return files
