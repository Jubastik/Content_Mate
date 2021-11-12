import os
import sqlite3


class Database:
    def __init__(self, connection_string):
        self.con = sqlite3.connect(connection_string)

    def get_start_settings(self):
        cur = self.cur()
        result = cur.execute(
            """select PathReadOnly, Log, OutPath from main 
            where id = 1"""
        ).fetchone()
        return result

    def get_all_preset_names(self):
        cur = self.cur()
        result = cur.execute("""select Name from preset""").fetchall()
        return [str(i[0]) for i in result]

    def get_default_processing_parameters(self):
        return self.get_processing_parameters("Default")

    def get_processing_parameters(self, name):
        cur = self.cur()
        result = cur.execute(
            """select Sensitivity, Indent, Step from preset 
            where Name = ?""",
            [name],
        ).fetchone()
        if result is None:
            return self.get_default_processing_parameters()
        return result

    def del_preset(self, name):
        cur = self.cur()
        cur.execute(
            """DELETE from preset
                where Name = ?
                    """,
            [name],
        )

    def update_processing_parameters(self, name, sensitivity, indent, step):
        cur = self.cur()
        cur.execute(
            """
            update preset
            set Sensitivity = ?,
            Indent = ?,
            Step = ?
            where Name = ?""",
            [
                sensitivity,
                indent,
                step,
                name,
            ],
        )

    def update_settings(self, can_edit, log, default_path):
        cur = self.cur()
        cur.execute(
            """
            update main
            set PathReadOnly = ?,
            Log = ?
            where id = 1
                """,
            [can_edit, log],
        )
        if default_path == "" or os.path.isdir(default_path):
            cur = self.cur()
            cur.execute(
                """
                    update main
                    set OutPath = ?
                    where id = 1
                            """,
                [default_path],
            )

    def save_preset(self, name, sensitivity, indent, step):
        cur = self.cur()
        cur.execute(
            """
                   INSERT INTO
                   preset VALUES
                   (?, ?, ?, ?)
                       """,
            [
                name,
                sensitivity,
                indent,
                step,
            ],
        )


    def cur(self):
        return self.con.cursor()

    def close(self):
        self.con.close()
