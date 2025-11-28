# Currency Exchange

A simple Kivy-based desktop currency exchange app — made quickly to improve my mother's ease of access and quality of life.

## Features
- Simple, easy-to-use desktop UI built with Kivy and KivyMD
- Live currency conversion (if conversion logic/data is included)
- Designed for accessibility and straightforward operation

## Requirements
- Python 3.11
- Kivy 2.1.0
- KivyMD 1.2.0

No requirements.txt is included in the repository; the minimal dependencies can be installed with pip as shown below.

## Installation (desktop)
1. Clone the repo:

   git clone https://github.com/AnnaNutzz/Currency-Exchange.git
   cd Currency-Exchange

2. (Optional but recommended) Create and activate a virtual environment:

   python3.11 -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .\.venv\Scripts\activate  # Windows PowerShell

3. Upgrade pip and install dependencies:

   pip install --upgrade pip
   pip install kivy==2.1.0 kivymd==1.2.0

   If you later add other dependencies, you can create a requirements.txt with:

   pip freeze > requirements.txt

## Running the app
Run the entrypoint file from the project root:

   python main.py

This will open the desktop application built with Kivy.

## Packaging for desktop (optional)
You can package the app into a single executable using PyInstaller:

1. Install PyInstaller:

   pip install pyinstaller

2. Create a standalone binary (example):

   pyinstaller --noconfirm --windowed --name CurrencyExchange main.py

Notes:
- If your app uses additional resource files (KV files, images, data), update the PyInstaller spec to include them or use the --add-data flag.
- Test the packaged app on the target OS.

## Screenshots
I will upload screenshots or GIFs later. Add them to the `assets/` or `docs/` folder and reference them here.

## Contributing
If you want to contribute improvements or fixes, please open an issue or submit a pull request. Keep changes small and include a brief description of why the change is needed.

## License
This project is provided under the MIT License. See the LICENSE file for details.

## Contact
If you have questions, open an issue or contact the repository owner at https://github.com/AnnaNutzz.
