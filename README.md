# IS_IA1_Burpsuite_Notesapp

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#features">Features Explored</a></li>
    <li><a href="#team">Team Members</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
Burp or Burp Suite is a set of tools used for penetration testing of web applications.  BurpSuite is designed to be an all-in-one toolkit, and BApps are add-ons that may be installed to expand its functionality. It is the most popular tool among professional web app security researchers and bug bounty hunters. Its ease of use makes it a more suitable choice over free alternatives like OWASP.

Various Burp Suite tools work seamlessly together to support the entire testing process, from initial mapping and analysis of an application's attack surface, through to finding and exploiting security vulnerabilities.

In this project, we have implemented a notes app with login and sign up page (encryption and decryption implemented) and tried out features of Burp through the webapp.

### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Python][Python]][Python-url]
* [![Flask][Flask]][Flask]
* [![Burpsuite][Burpsuite]][Burpsuite-url]

<!-- GETTING STARTED -->
## Getting Started



### Prerequisites

Install the prerequisites using:
  ```sh
   pip install -r requirements.txt
  ```

### Installation

1. Clone this repo
   ```sh
   git clone https://github.com/IshikaDe-2803/IS_IA1_Burpsuite_Notesapp.git
   ```
2. Change the directory to the main code directory
   ```sh
   cd IS_IA_Burpsuite
   ```
3. Install prerequisites
   ```sh
   pip install -r requirements.txt
   ```
4. Run the app
   ```sh
   flask --app notes_app run
   ```
5. Open Burpsuite application and open the app in the browser.

<!-- Features -->
## Features
* **Proxy**: 
Burp Proxy operates as a web proxy server between the browser and target applications. It enables the user to intercept, inspect, and modify traffic that passes in both directions.
* **Repeater**: 
Burp Repeater is a tool that enables you to modify and send an interesting HTTP or WebSocket message over and over.
* **Intruder**: 
Burp Intruder is a tool for automating customized attacks against web applications. It enables you to configure attacks that send the same HTTP request over and over again.
* **Sequencer**: 
Burp Sequencer enables you to analyze the quality of randomness in a sample of tokens. You can use Sequencer to test any tokens that are intended to be unpredictable.
* **Comparer**: 
Burp Comparer enables you to compare any two items of data. You can use Comparer to quickly and easily identify subtle differences between requests or responses.

<!-- ACKNOWLEDGMENTS -->
## Team
* Sanyukta Joshi (16010120019)
* Umaima Dabir (16010120064)
* Ishika De (16010120065)
* Tanvi Deshpande (16010120067)

<!-- MARKDOWN LINKS & IMAGES -->
[Python]: https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Flask]: https://img.shields.io/badge/Flask-20232A?style=for-the-badge&logo=flask&logoColor=61DAFB
[Flask-url]: https://flask.palletsprojects.com/en/2.2.x/
[Burpsuite]: https://img.shields.io/badge/Burpsuite-000000?style=for-the-badge&logo=burpsuite&logoColor=white
[Burpsuite-url]: https://portswigger.net/burp

