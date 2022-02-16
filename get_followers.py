import instaloader
from instaloader import Profile
import time

def parsing(profile):  
    i = 0  
    t0 = int(time.time())
    print(f"start parcing at {str(t0)}!")
    with open(f"{profile.username}_followers.txt", "w") as f:
        for followers in profile.get_followers():
            i += 1
            f.write(followers.username + "\n")
            print(followers.username)
            if i % 10 == 0:
                print("stop")
                time.sleep(3)
    done = int(time.time())- t0
    print(f"{str(done)}s was waisted")

def main():
    L = instaloader.Instaloader()
    L.login("login", "password") # Аккаунт через который парсим 
    profile = Profile.from_username(L.context, "dianapagalina") # Аккаунт, который парсим
    parsing(profile)

    

if __name__ == "__main__":
    main()