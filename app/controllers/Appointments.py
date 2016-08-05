"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Appointments(Controller):
    def __init__(self, action):
        super(Appointments, self).__init__(action)
        """
        This is an example of loading a model.
        Every controller has access to the load_model method.
        """
        self.load_model('Appointment')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self, id):
        session['id'] = id
        return redirect('/dashboard')

    def dashboard(self):
        print session['id']
        curr_appts = self.models['Appointment'].get_today_appointments(session['id'])
        future_appts = self.models['Appointment'].get_future_appointments(session['id'])
        return self.load_view('index2.html', curr_appts=curr_appts, future_appts=future_appts)        
    
    def add(self, user_id):
        appt_details = {
            'task': request.form['tasks'],
            'appt_date': request.form['date'],
            'appt_time': request.form['time'],
            'user_id': user_id
        }
        self.models['Appointment'].add_appointment(appt_details)
        return redirect('/dashboard')

    def edit(self, id):
        appointment = self.models['Appointment'].get_appointment_by_id(id)
        return self.load_view('index3.html', appointment=appointment[0], id=id)
    
    def update(self, id):
        self.models['Appointment'].update_appointment(request.form)
        return redirect('/dashboard')

    def delete(self, id):
        self.models['Appointment'].delete_appointment(id)
        return redirect('/dashboard')

        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """


