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

    def log_in(self,username, password):
        stored_password = self.redis_client.hget(f"user:{username}", "password_hash")
        if stored_password and bcrypt.checkpw(password.encode("utf-8"), stored_password.encode("utf-8")):
            self.current_user = username
            print(f"Ви увійшли як {username}.")
            return True
        print("Неправильний логін або пароль.")
        return False

    def del_user(self, username):
        if not self.redis_client.hdel("users", username):
            print("Користувач не знайдений.")
            return False

        print(f"Користувача {username} успішно видалено.")
        return True

    def update_user_info(self):
        user_data = self.redis_client.hget("users", username)
        if not user_data:
            print("Користувач не знайдений.")
            return False

        user_data = json.loads(user_data)
        if fullname:
            user_data["full_name"] = fullname
        if password:
            user_data["password"] = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

        self.redis_client.hset("users", username, json.dumps(user_data))
        print(f"Інформація про користувача {username} успішно оновлена.")
