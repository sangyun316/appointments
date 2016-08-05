""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Appointment(Model):
    def __init__(self):
        super(Appointment, self).__init__()

    def get_today_appointments(self, user_id):
        query = "SELECT id, task, appt_time, status FROM appointments WHERE user_id = :user_id AND DATE(appt_date) = CURDATE()"
        data = {'user_id': user_id}
        return self.db.query_db(query, data)

    def get_future_appointments(self, user_id):
        query = "SELECT id, task, appt_date, appt_time FROM appointments WHERE user_id = :user_id AND DATE(appt_date) > DATE(NOW())"
        data = {'user_id': user_id}
        return self.db.query_db(query, data)

    def get_appointment_by_id(self, id):
        query = "SELECT * FROM appointments WHERE id = :id"
        data = { 'id': id}
        return self.db.query_db(query, data)

    def add_appointment(self, appointment):
        query = "INSERT INTO appointments (task, appt_date, appt_time, status, created_at, updated_at, user_id) VALUES (:task, :appt_date, :appt_time, 'Pending', NOW(), NOW(), :user_id)"
        data = { 
            'task': appointment['task'], 
            'appt_date': appointment['appt_date'], 
            'appt_time': appointment['appt_time'],
            'user_id': appointment['user_id']
        }
        return self.db.query_db(query, data)

    def update_appointment(self, appointment):
        query = "UPDATE appointments SET task = :task, status = :status, appt_date = :appt_date, appt_time = :appt_time, updated_at = NOW() WHERE id=:id"
        data = {
            'task': appointment['task'],
            'status': appointment['status'],
            'appt_date': appointment['appt_date'],
            'appt_time': appointment['appt_time'],
            'id': appointment['id']
        }
        return self.db.query_db(query, data)

    def delete_appointment(self, id):
        query = "DELETE FROM appointments WHERE id = :id"
        data = { "id": id }
        return self.db.query_db(query, data)


    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """