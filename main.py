from core.vision import verify_user

if __name__ == "__main__":
    if verify_user():
        print("🚀 Welcome, Zaid.")
    else:
        print("❌ Access Denied.")
