import time
import requests, json

class Trenstagram:
    def __init__(self):
        self.BASE_URL = 'https://www.instagram.com/'
        self.USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0"
        self.session = requests.Session()
        self.session.headers = {'user-agent': self.USER_AGENT}
        self.session.headers.update({'Referer': self.BASE_URL})
        self.logged_in = False

    def login(self, USERNAME, PASSWD, EMAIL):
        self.email = EMAIL
        self.username = USERNAME
        try:
            req = self.session.get(self.BASE_URL)
            self.session.headers.update({'X-CSRFToken': req.cookies['csrftoken']})
            str_time = str(int(time.time()))
            PASSWORD = '#PWD_INSTAGRAM_BROWSER:0:' + str_time + ':' + PASSWD
            login_data = {'username': USERNAME, 'enc_password': PASSWORD}
            LOGIN_URL = self.BASE_URL + 'accounts/login/ajax/'
            login = self.session.post(LOGIN_URL , data=login_data, allow_redirects=True)
            self.session.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
            if(login.json()['authenticated']):
                self.logged_in = True
                print("Logged in")
                return True
            else:
                raise Exception()
        except:
            print("Error Logging in.")
        return False


    def verify(self):
        if self.logged_in:
            return True
        print("Log in first.")
        return False

    def change_username(self, new_username):
        if self.verify():
            try:
                data = {
                    'username': new_username,
                    'email': self.email
                }
                r = self.session.post(self.BASE_URL + "accounts/edit/", data=data)
                if r.json()['status'] == "ok":
                    print(f'Username Changed to {new_username}')
                    self.username = new_username
                    return True
                else:
                    raise Exception()
            except:
                print('Error Changing Username')
        return False

    def change_bio(self, new_bio):
        if self.verify():
            try:
                data = {
                    'username': self.username,
                    'biography': new_bio,
                    'email': self.email
                }
                r = self.session.post(self.BASE_URL + "accounts/edit/", data=data)
                if r.json()['status'] == "ok":
                    print(f'Bio Changed to {new_bio}')
                    return True
                else:
                    raise Exception()
            except:
                print('Error Changing Bio')
        return False

    def change_name(self, new_name):
        if self.verify():
            try:
                data = {
                    'username': self.username,
                    'first_name': new_name,
                    'email': self.email
                }
                r = self.session.post(self.BASE_URL + "accounts/edit/", data=data)
                if r.json()['status'] == "ok":
                    print(f'Name Changed to {new_name}')
                    return True
                else:
                    raise Exception()
            except:
                print('Error Changing Name')
        return False
        
    def change_website(self, new_website):
        if self.verify():
            try:
                data = {
                    'username': self.username,
                    'external_url': new_website,
                    'email': self.email
                }
                r = self.session.post(self.BASE_URL + "accounts/edit/", data=data)
                if r.json()['status'] == "ok":
                    print(f'Website Changed to {new_website}')
                    return True
                else:
                    raise Exception()
            except:
                print('Error Changing Website')
        return False
        
    def change_profile_image(self, image_url):
        if self.verify():
            try:
                data = {"Content-Disposition": "form-data", "name": "profile_pic", "filename":"profilepic.jpg","Content-Type": "image/jpeg"}
                image_req = requests.get(image_url).content
                pfp = bytes(image_req)
                self.session.headers.update({'Content-Length' : str(len(pfp))})
                r = self.session.post(self.BASE_URL + "accounts/web_change_profile_picture/", files={'profile_pic': pfp}, data=data)
                if r.json()['changed_profile']:
                    print("Profile picture changed!")
                    return True
                else:
                    raise Exception()
            except:
                print('Error Changing Profile Image')
        return False
