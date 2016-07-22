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
   
    def index(self):
        curr_appts = self.models['Appointment'].get_today_appointments()
        future_appts = self.models['Appointment'].get_future_appointments()
        return self.load_view('index2.html', curr_appts=curr_appts, future_appts=future_appts)

    def add(self):
        appt_details = {
            'task': request.form['task'],
            'appt_date': request.form['appt_date'],
            'appt_time': request.form['appt_time']
        }
        add_status = self.models['Appointment'].add_appointment(appt_details)
        if add_status['status'] == False:
            for message in add_status['errors']:
                flash(message)
            return redirect('/appointments/')
        else:
            session['first_name'] = request.form['first_name']
            return redirect('/appointments')
        self.models['Appointment'].add_appointment(appt_details)
        return redirect('/appointments')

    def update(self, id):
        appointment = self.models['Appointment'].get_appointment_by_id(id)
        return self.load_view('index3.html', appointment=appointment, id=id)

    def delete(self, id):
        self.models['Appointment'].delete_appointment(id)
        return redirect('/appointments')

        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """


