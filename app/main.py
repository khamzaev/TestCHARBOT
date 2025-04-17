from app.bot import app

if __name__ == "__main__":
    print("Бот запущен!")
    app.run_app(app, port=8080)
