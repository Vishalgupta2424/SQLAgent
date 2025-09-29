import re
import logging
from difflib import get_close_matches
from Myschema import get_table_columns  # my schema access module

logging.basicConfig(level=logging.INFO)

# --- Load entire schema once ---
#  get_table_columns(None) returns dict {table_name: [col1, col2, ...]}
SCHEMA = get_table_columns(None)
ALL_TABLES = list(SCHEMA.keys())

def correct_name(user_name, candidates):
    """
    Case-insensitive + fuzzy matching for table/column names.
    Returns closest schema match or None if no good match.
    """
    lower_map = {name.lower(): name for name in candidates}
    user_lower = user_name.lower()
    if user_lower in lower_map:
        return lower_map[user_lower]
    
    # Fuzzy match if no exact lowercase match
    matches = get_close_matches(user_name, candidates, n=1, cutoff=0.6)
    if matches:
        return matches[0]
    
    return None

def parse_values(values_str):
    """
    Safely parse multiple tuples of values from VALUES clause,
    handles commas inside quotes.
    """
    raw_values_list = re.findall(r"\((.*?)\)", values_str, re.DOTALL)
    parsed_values = []
    for raw_values in raw_values_list:
        # Split on commas not inside quotes
        values = re.findall(r"(?:'[^']*'|[^,]+)", raw_values)
        # Strip quotes and whitespace
        values = [val.strip().strip("'") for val in values]
        parsed_values.append(tuple(values))
    return parsed_values

def fix_insert_query(query, user_table_name):
    """
    Fix INSERT query:
    - Correct table name
    - Correct column names
    - Handle multiple rows and quoted values
    Returns: corrected_query, values_list OR None, error_message
    """
    #  Correct table name
    correct_table = correct_name(user_table_name, ALL_TABLES)
    if not correct_table:
        return None, f"Table `{user_table_name}` not found in schema."
    
    #  Get columns for table
    column_names = SCHEMA[correct_table]
    
    #  Extract VALUES clause
    values_match = re.search(r"VALUES\s*(.*)", query, re.IGNORECASE | re.DOTALL)
    if not values_match:
        return None, "No VALUES found in the INSERT statement."
    
    values_str = values_match.group(1).strip().rstrip(";")
    values_list = parse_values(values_str)
    if not values_list:
        return None, "No tuples found in VALUES."
    
    #  Column count validation
    for row in values_list:
        if len(row) != len(column_names):
            return None, f"Column mismatch: `{correct_table}` expects {len(column_names)} columns, got {len(row)}."
    
    #  Build parameterized query
    placeholders = ', '.join(['%s'] * len(column_names))
    corrected_query = f"INSERT INTO {correct_table} ({', '.join(column_names)}) VALUES ({placeholders})"
    
    return corrected_query, values_list

# --- Example Usage ---
if __name__ == "__main__":
    # Example user input (typo in table name and lowercase)
    user_query = "INSERT INTO students (student_id, name, age, gender, email, dept_id) VALUES (1, 'Aman Gupta', 20, 'Male', 'aman@example.com', 1);"
    
    corrected_sql, values = fix_insert_query(user_query, "students")
    
    if corrected_sql:
        logging.info("Corrected Query: %s", corrected_sql)
        logging.info("Values: %s", values)
    else:
        logging.error("Error: %s", values)
