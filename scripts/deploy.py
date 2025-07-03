import os
import snowflake.connector

def execute_sql_file(cursor, file_path):
    with open(file_path, 'r') as file:
        sql_commands = file.read()
        for statement in sql_commands.strip().split(';'):
            if statement.strip():
                cursor.execute(statement)

def main(env):
    conn = snowflake.connector.connect(
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        user=os.getenv('SNOWFLAKE_USER'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        role=os.getenv('SNOWFLAKE_ROLE'),
        warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
        database=os.getenv('SNOWFLAKE_DATABASE'),
        schema=os.getenv('SNOWFLAKE_SCHEMA'),
    )

    cursor = conn.cursor()
    sql_folder = f'sql/{env}'

    for filename in sorted(os.listdir(sql_folder)):
        if filename.endswith('.sql'):
            path = os.path.join(sql_folder, filename)
            print(f"Executing: {path}")
            execute_sql_file(cursor, path)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    import sys
    env = sys.argv[1] if len(sys.argv) > 1 else "dev"
    main(env)
