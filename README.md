# Certivo_takehome_assignment

---

## Setup/installation instructions

Setup will involve a few steps, but in short:

1. Download the repository (extract if zip file)
2. Download the AI model for use (link provided below)
3. Replace/insert files into the Files folder as needed
4. Replace/insert model into the Model folder

For the more in-depth version:

1. In GitHub, download the repository or clone it locally - if downloaded as a .zip file, make sure to extract it first
2. Chatbots are dependent on the data it is trained on (see section **Brief Explination of approach and archetecture decisions** for more information) - the link provided here  is a great general use model based on ChatGPT.  [Follow this link to download the model automatically](https://huggingface.co/ggml-org/gpt-oss-20b-GGUF/resolve/main/gpt-oss-20b-mxfp4.gguf).  (Note - this file is ~12 GB)
3. The **Files** folder is where all the .pdf and .html files should go into - the code will automatically take these and process them into a format the chatbot can use
4. Once the above is done (or if you have your own .gguf file you would like to use), insert it into the **Model** folder - the program will run so long as there is a valid .gguf file present

---

## How to run the application

In short: Run the .exe OR run main.py using Python (requires dependencies/libraries to be already installed locally)

In more detail: For the easiest solution, run the included .exe file (Windows only at this time, will include Linux later) and program will start up - for an alternative solution, you can directly run the program by calling **main.py** using Python, however this does require all relevant libraries to be installed (running will notify user of missing libraries)

Regardless of which option you choose, once the program is running, use the command interface to "chat" with the chatbot, enter the phrase "Quit" (case sensitive) to exit the program

---

## Brief explanation of approach and architecture decisions

==TO DO==

---
