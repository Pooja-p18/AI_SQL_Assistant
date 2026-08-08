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
        
        
if __name__ == "__main__":
    schema = get_database_schema()

    if schema:
        current_table = None

        for table_name, column_name, data_type in schema:

            if table_name != current_table:
                print(f"\nTable: {table_name}")
                current_table = table_name

            print(f"  {column_name}: {data_type}")
        
        