**eBay Cart Automation Test with Playwright (Python)**
This project automates the process of searching for a book on eBay, adding it to the cart, and verifying that the cart has been updated using Playwright in Python.

**Prerequisites**
•	Python 3.7 or higher
•	A code editor like Visual Studio Code, PyCharm, or any editor of your choice.
•	Google Chrome, Microsoft Edge, or any other browser supported by Playwright.

**Installation**
Step 1: Install Python Dependencies
1.	First, make sure that you have Python installed on your machine.
2.	Install Playwright by running the following command:
bash
Copy code
pip install playwright
**Step 2: Install Browsers for Playwright**
Playwright needs the browser binaries to work. Install them by running:
bash
Copy code
python -m playwright install
This will automatically download the required browser binaries (e.g., Chromium).
**Project Structure**
plaintext
Copy code
.
├── test_script.py              # The main Python script that automates the eBay test
├── README.md                   # This readme file
└── requirements.txt            # Python dependencies for the project
**requirements.txt**
You can also create a requirements.txt file that contains the necessary dependencies:
plaintext
Copy code
playwright
To install dependencies from requirements.txt, use the following command:
bash
Copy code
pip install -r requirements.txt

**Running the Test**
To run the test script, simply execute the Python script:
bash
Copy code
python test_script.py
**What the Test Does**
1.	Launches a browser and navigates to eBay.
2.	Searches for 'book' in the search bar.
3.	Clicks on the first book listed in the search results.
4.	Adds the item to the cart.
5.	Verifies the cart has been updated, and checks if at least one item is added to the cart.
**Output**
When the test runs successfully, you will see the following message:
mathematica
Copy code
Test Passed: Item successfully added to the cart.
If the cart is empty or there is any issue, you will see an error message like:
csharp
Copy code
Test Failed: Cart is empty.

**Notes**
•	**Headless Mode**: The script by default opens the browser with a visible UI (headless=False). If you want to run the test without the browser window showing up (headlessly), modify the line browser = p.chromium.launch(headless=False) to browser = p.chromium.launch(headless=True).
•	**Waiting for Elements**: Playwright's wait_for_selector() ensures that the script waits for elements to load before interacting with them.
•	**Browser Compatibility**: Playwright supports multiple browsers (Chromium, Firefox, WebKit). This script uses Chromium by default, but you can easily switch to another browser if needed.
Troubleshooting
•	**Browser not launching or crashing**: Make sure the necessary browser binaries are installed using the command python -m playwright install.
•	**Dependency issues**: If you encounter issues with missing dependencies, try installing them manually via pip install.
•	**Slow execution**: If you experience delays, you can adjust the time wait_for_selector() uses or add more explicit waits.

**Troubleshooting**
•	**Browser not launching or crashing**: Make sure the necessary browser binaries are installed using the command python -m playwright install.
•	**Dependency issues**: If you encounter issues with missing dependencies, try installing them manually via pip install.
•	**Slow execution**: If you experience delays, you can adjust the time wait_for_selector() uses or add more explicit waits.


  
