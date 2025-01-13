import redis
import bcrypt
import json

class Social_nets:
    def add_user(self, username,password, fullname):
        if self.redis_client.hexists("users", username):
            print("Користувач вже існує")
            return False
        password = bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt()).decode("utf-8")
        user_data = {"password":password,"full_name":fullname}

        self.redis_client.hset("users",username,json.dumps(user_data))
        return True
        data = self.redis_client.hget("users", username)
        json.loads(data)

    def lig_in(self):
        pass

    def del_user(self):
        pass

    def update_user_info(self):
        pass
    def search_user(self):
        pass

    def viev_user(self): #fullname
        pass

    def user_friends(self):
        pass

    def user_publications(self):
        pass