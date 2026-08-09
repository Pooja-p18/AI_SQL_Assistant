from database.connection import get_connection

def get_database_schema():
    """
    Retrieve tables and columns from the PostgreSQL database.
    
    """
    
    connection = get_connection()
    
    if connection is None:
        return None
    
    try:
        cursor = connection.cursor()
        
        query = """
        SELECT
            table_name,
            column_name,
            data_type
        FROM information_schema.columns
        WHERE table_schema = 'public'
        ORDER BY table_name, ordinal_position;
        """
        
        cursor.execute(query)
        
        results = cursor.fetchall()
        
        return results
    
    except Exception as e:
        print(f"Schema Retrieval Error: {e}")
        return None
    
    finally:
        cursor.close()
        connection.close()

def get_foreign_keys():
    """
    Retrieve foreign key relationships from the PostgreSQL database.
    
    """
    connection = get_connection()
    
    if connection is None:
        return None
    
    try:
        cursor = connection.cursor()
        
        query = """
        SELECT 
            tc.table_name AS source_table,
            kcu.column_name AS source_column,
            ccu.table_name AS target_table,
            ccu.column_name AS target_column
        FROM information_schema.table_constraints AS tc
        JOIN information_schema.key_column_usage AS kcu
            ON tc.constraint_name =kcu.constraint_name
            AND tc.table_schema = kcu.table_schema
        JOIN information_schema.constraint_column_usage AS ccu
            ON ccu.constraint_name = tc.constraint_name
            AND ccu.table_schema = tc.table_schema
        WHERE tc.constraint_type = 'FOREIGN KEY'
            AND tc.table_schema = 'public'
        ORDER BY tc.table_name;
        """
        
        cursor.execute(query)
        
        results = cursor.fetchall()
        
        return results
    
    except Exception as e:
        print(f"Foreign Key Retrieval Error: {e}")
        return None
    
    finally:
        cursor.close()
        connection.close()
        
        
if __name__ == "__main__":

    print("\nDATABASE SCHEMA")
    print("----------------")

    schema = get_database_schema()

    if schema:
        current_table = None

        for table_name, column_name, data_type in schema:

            if table_name != current_table:
                print(f"\nTable: {table_name}")
                current_table = table_name

            print(f"  {column_name}: {data_type}")

    print("\nFOREIGN KEY RELATIONSHIPS")
    print("-------------------------")

    foreign_keys = get_foreign_keys()

    if foreign_keys:
        for row in foreign_keys:
            print(row)