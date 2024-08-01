import MySQLdb

# Establishing connection
connection = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="password", db="netflix", charset="utf8")
cursor = connection.cursor()

# Creating table if not exists
create_table = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INT
)
"""

insert_data = """
INSERT INTO users (username, email, age) VALUES
('john2', 'john2@doe.com', 20),
('jane2', 'jane2@doe.com', 38),
('jack2', 'jack2@doe.com', 67)
"""

# Inserting data into the table
cursor.execute(create_table)
cursor.execute(insert_data)

# Committing the changes
connection.commit()

select_data = "SELECT * FROM users"

cursor.execute(select_data)

users = cursor.fetchall()

for user in users:
    print(user)

# Closing the connection
cursor.close()
connection.close()

