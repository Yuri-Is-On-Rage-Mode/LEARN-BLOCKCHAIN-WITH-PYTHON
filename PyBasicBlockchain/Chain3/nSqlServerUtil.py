import os
import json
import yaml
import toml
from tabulate import tabulate
import shutil
import argparse

class JSQL:
    @staticmethod
    def serve(dirpath):
        return SQLServer(dirpath)

class SQLServer:
    def __init__(self, dirpath):
        self.dirpath = dirpath
        os.makedirs(dirpath, exist_ok=True)

    def NewDB(self, db_name):
        db_path = os.path.join(self.dirpath, db_name)
        os.makedirs(db_path, exist_ok=True)
        return Database(db_path)

    def SaveAll(self, backup_path):
        """
        Save all databases and their tables to a backup location.
        """
        if os.path.exists(backup_path):
            shutil.rmtree(backup_path)
        shutil.copytree(self.dirpath, backup_path)
        print(f"All databases and tables saved to: {backup_path}")

class Database:
    def __init__(self, db_path):
        self.db_path = db_path

    def NewTable(self, table_name, column_names):
        table_path = os.path.join(self.db_path, f"{table_name}.json")
        data = {"0": {col: "genesis_block" for col in column_names}}
        with open(table_path, 'w') as f:
            json.dump(data, f, indent=2)
        return Table(table_path)

    def SaveDB(self, backup_path):
        """
        Save the current database and all its tables to a backup location.
        """
        db_name = os.path.basename(self.db_path)
        backup_db_path = os.path.join(backup_path, db_name)
        if os.path.exists(backup_db_path):
            shutil.rmtree(backup_db_path)
        shutil.copytree(self.db_path, backup_db_path)
        print(f"Database '{db_name}' and all its tables saved to: {backup_db_path}")

class Table:
    def __init__(self, table_path):
        self.table_path = table_path

    def _load_data(self):
        with open(self.table_path, 'r') as f:
            return json.load(f)

    def _save_data(self, data):
        with open(self.table_path, 'w') as f:
            json.dump(data, f, indent=2)

    def Insert(self, values):
        data = self._load_data()
        new_id = str(max(map(int, data.keys())) + 1)
        data[new_id] = dict(zip(data['0'].keys(), values))
        self._save_data(data)

    def Replace(self, old_values, new_values):
        data = self._load_data()
        for row_id, row in data.items():
            if row_id != '0' and list(row.values()) == old_values:
                data[row_id] = dict(zip(data['0'].keys(), new_values))
                break
        self._save_data(data)

    def ShowGrid(self):
        data = self._load_data()
        headers = list(data['0'].keys())
        rows = [list(row.values()) for row_id, row in data.items() if row_id != '0']
        print(tabulate(rows, headers=headers, tablefmt='grid'))

    def Grid(self, format):
        data = self._load_data()
        headers = list(data['0'].keys())
        rows = [list(row.values()) for row_id, row in data.items() if row_id != '0']
        table_data = [dict(zip(headers, row)) for row in rows]
        
        if format == "json":
            return json.dumps(table_data, indent=2)
        elif format == "yaml":
            return yaml.dump(table_data)
        elif format == "toml":
            return toml.dumps({"table": table_data})
        else:
            raise ValueError("Unsupported format. Use 'json', 'yaml', or 'toml'.")

    def SaveTable(self, backup_path):
        """
        Save the current table to a backup location.
        """
        table_name = os.path.basename(self.table_path)
        backup_table_path = os.path.join(backup_path, table_name)
        shutil.copy2(self.table_path, backup_table_path)
        print(f"Table '{table_name}' saved to: {backup_table_path}")

    def SaveGridToFile(self, filepath, format="json"):
        """
        Save the grid data to a file in the specified format.
        
        :param filepath: The path where the file will be saved
        :param format: The format of the file (json, yaml, or toml)
        """
        grid_data = self.Grid(format)
        
        with open(filepath, 'w') as f:
            f.write(grid_data)
        
        print(f"Grid data saved to: {filepath}")

def main():
    parser = argparse.ArgumentParser(description="JSQL Command Line Interface")
    
    parser.add_argument("--serve", type=str, help="Serve the SQL server at a directory path.")
    
    parser.add_argument("--newdb", type=str, help="Create a new database.")
    parser.add_argument("--dbpath", type=str, help="Path to the database.")
    
    parser.add_argument("--newtable", type=str, help="Create a new table in the database.")
    parser.add_argument("--columns", nargs='+', help="Column names for the new table.")
    
    parser.add_argument("--insert", nargs='+', help="Insert new data into the table.")
    
    parser.add_argument("--replace", nargs='+', help="Replace old data in the table with new data.")
    
    parser.add_argument("--showgrid", action='store_true', help="Show the table data in a grid format.")
    
    parser.add_argument("--grid", type=str, choices=["json", "yaml", "toml"], help="Get the table data in a specific format.")
    
    parser.add_argument("--savetable", type=str, help="Save the table to a backup location.")
    
    parser.add_argument("--savedb", type=str, help="Save the database to a backup location.")
    
    parser.add_argument("--saveall", type=str, help="Save all databases to a backup location.")
    
    parser.add_argument("--savegrid", nargs=2, help="Save the grid data to a file. Provide file path and format.")
    
    args = parser.parse_args()

    sql_server = JSQL.serve("./")

    if args.serve:
        print("Serving in './', we dont value your args, we will serve this in `./` only, :)")
        #sql_server = JSQL.serve(args.serve)
        
    if args.newdb:
        db = sql_server.NewDB(args.newdb)
    
    if args.newtable and args.columns and args.dbpath:
        db = Database(args.dbpath)
        db.NewTable(args.newtable, args.columns)
    
    if args.insert and args.dbpath:
        table = Table(args.dbpath)
        table.Insert(args.insert)
    
    if args.replace and args.dbpath:
        table = Table(args.dbpath)
        old_values, new_values = args.replace[:len(args.replace)//2], args.replace[len(args.replace)//2:]
        table.Replace(old_values, new_values)
    
    if args.showgrid and args.dbpath:
        table = Table(args.dbpath)
        table.ShowGrid()
    
    if args.grid and args.dbpath:
        table = Table(args.dbpath)
        print(table.Grid(args.grid))
    
    if args.savetable and args.dbpath:
        table = Table(args.dbpath)
        table.SaveTable(args.savetable)
    
    if args.savedb and args.dbpath:
        db = Database(args.dbpath)
        db.SaveDB(args.savedb)
    
    if args.saveall and args.serve:
        sql_server.SaveAll(args.saveall)
    
    if args.savegrid and args.dbpath:
        table = Table(args.dbpath)
        table.SaveGridToFile(args.savegrid[0], args.savegrid[1])

if __name__ == "__main__":
    main()
