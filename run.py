from app import create_app
# imports the create_app() function from app/__init__.py
app = create_app()

if __name__ == "__main__": # Ensures the app runs only if this script is executed directly
    app.run(debug=True) 
# This will start the Flask development server
