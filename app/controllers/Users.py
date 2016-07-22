from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
        self.db = self._app.db
   
    def index(self):
        return self.load_view('index.html')

    def register(self):
        user_info = {
            'name': request.form['name'],
            'email': request.form['email'],
            'password': request.form['password'],
            'confirm_pw': request.form['confirm_pw'],
            'birth_date': request.form['bday']
        }
        register_status = self.models['User'].register_user(user_info)
        if register_status['status'] == False:
            for message in register_status['errors']:
                flash(message)
            return redirect('/')
        else:
            session['name'] = request.form['name']
            return redirect('/appointments')

    def login(self):
        user_info = {
            'email': request.form['email'],
            'password': request.form['password']
        }
        user = self.models['User'].login_validation(user_info)
        if user:
            session['name'] = user[0]['name']
            return redirect('/appointments')
        else:
            flash('Email or password is incorrect. Please log-in again!')
            return redirect('/')

    def success(self):
        return self.load_view('index2.html')

    def destroy(self, id):
        appointment = self.models['Appointment'].get_appointment_by_id(id)
        return self.load_view('index2.html', appointment=appointment, id=id)

    def logout(self):
        session.clear()
        return redirect('/')
    	