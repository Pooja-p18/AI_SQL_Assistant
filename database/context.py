from database.schema import get_database_schema, get_foreign_keys

def build_database_context():
    """
    Build a readable representation of the database
    schema and foreign key relationships. 
    
    """
    
    schema = get_database_schema()
    foreign_keys = get_foreign_keys()
    
    if schema is None:
        return None
    
    context = "DATABASE SCHEMA\n"
    context += "----------------\n"
    
    current_table = None
    
    for table_name, column_name, data_type in schema:
        
        if table_name != current_table:
            context += "===========================\n"
            current_table = table_name
            
        context += f"   {column_name} : {data_type}\n"
        
    context += "\nFOREIGN KEY RELATIONSHIPS\n"
    context += "=========================\n"
    
    if foreign_keys:
        for source_table, source_column, target_table, target_column in foreign_keys:
            context += (
                f"{source_table}.{source_column}"
                f"→ {target_table}.{target_column}\n"
            )
            
    return context

if __name__ == "__main__":
    
    database_context = build_database_context()
    
    if database_context:
        print(database_context)

