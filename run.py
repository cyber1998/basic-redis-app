from app import create_app


if __name__ == '__main__':
    app = create_app('app.configs.config')
    app.run(debug=True, port=5000, host='localhost')
