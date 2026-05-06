import psycopg2

def get_elos():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="postgres_test",
            user="test",
            password="test",
            port="5430"
        )
        cursor = connection.cursor()

        query = """SELECT image, elo FROM ratings ORDER BY (substring(image, '^[0-9]+'))::INT ASC;"""
        cursor.execute(query)
        rows = cursor.fetchall()

        elo_list = [row[1] for row in rows]
        return elo_list

    except Exception as e:
        print(f"Database error: {e}")
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'connection' in locals(): connection.close()


elos = get_elos()
print("TOTAL IMAGES = ", len(elos))
print("ELOS = ", elos)