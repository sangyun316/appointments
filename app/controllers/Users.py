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
            session['id'] = register_status['id']
            url = '/appointments/' + str(session['id'])
            print url
            return redirect(url)

    def login(self):
        user_info = {
            'email': request.form['email'],
            'password': request.form['password']
        }
        user = self.models['User'].login_validation(user_info)
        if user:
            session['name'] = user[0]['name']
            print session['name']
            session['id'] = user[0]['id']
            url = '/appointments/' + str(session['id'])
            print url
            return redirect(url)
        else:
            flash('Email or password is incorrect. Please log-in again!')
            return redirect('/')

    def logout(self):
        session.clear()
        return redirect('/')
    	