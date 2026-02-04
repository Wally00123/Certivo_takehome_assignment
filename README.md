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

In short: Run the main.py using Python (requires dependencies/libraries to be already installed locally, all libraries can be found via pip)

In more detail: You can directly run the program by calling **main.py** using Python, however this does require all relevant libraries to be installed (running will notify user of missing libraries, use pip install *missing library* to install them)

This program is recommended with the latest python version (3.14.*) - to run in windows, right click folder, open in terminal, then type: `py .\main.py`

Once the program is running, use the command interface to "chat" with the chatbot, enter the phrase "Quit" (case sensitive) to exit the program

Note: If you need to install llama-cpp-python, this requires CMake - to install, do the following:

1. Download Visual Studios 2019 [Link here](https://c2rsetup.officeapps.live.com/c2r/downloadVS.aspx?sku=community&channel=Release&version=VS2019)
2. When installing, check "Desktop Development with C++" (make sure to select all optional components here, especially C++ CMake and Windows SDK), and also check "Universal Windows Platform build tools" (select all optional here as well)
3. Wait for it to install, once finished you should be good to go with the above 'pip install llama-cpp-python'

---

## Brief explanation of approach and architecture decisions

This section will be divided into sub-sections, each of which will go over various parts of the overall project.

### Local Models

So why is there a .gguf file in the program, and why do you need to download it?

- Biggest reason for this is due to quality of data.  Chatbots, and AI in general, is only as good as the data that is fed into it.  While I could have used Tensorflow and NumPy to create a super simple model, the data that I could feed into it over a couple of days would not be high enough quality to make a good chatbot
- .gguf files are pre-compiled, open source models that can be used in C++ and Python (as is in this case) to then build upon further for specific use cases as I did in this application.  This allows for faster development of the main program (the chatbot itself) while keeping high quality outputs
- There are many types of .gguf model files out there, while I chose something generic like GPT for this example, there are optimized models for workflows which also help to improve speed and quality of outputs

So why local models over something like Gemini?  There were a couple of reasons.

- Most importantly, having something local meant that I could iterate fast, test with large amounts of tokens (each request with the files plus prompt was >1k tokens per question), and modify quickly without waiting for rate limits - because I could avoid rate limits, I was able to test freely without any limitations
- As mentioned above, using local could allow me to test with different models without having to rewrite the API calling methods every time
- Was without internet for large periods of time, allowed me to develop even when disconnected (bad winter weather, other impacts)

### Using the Files and Model folders

I used the folder structure because it allows for an easy, controlled way for people to input whatever files are needed/desired without statically defining items.  This also allows for things to be more organized and keeps the main folder clean instead of having everything in one large, cluttered folder

### main.py

This is the main driver of the application - as is such, I only kept the things pertaining to the chatbot (including AI Model) and CLI interfacing here, while keeping all the file processing seperately.  This was mainly to isolate functions in case of errors (easier troubleshooting) and/or upgrading, refactoring, etc.

Main.py also includes only the code that is needed to prompt startup processes (see below) or code that is continuously running during runtime.

### parse_files.py

The main point of this program is to find all the .pdf and .html files found in the "Files" folder, and after iterating through it and finding them all, extract all the data and turn it into python data structures that can be fed along with the user prompt to the chatbot for processing.

I designed it this way because all the data needs to be pre-loaded only - it doesn't make sense to keep it in main.py which is continuously running if the data processing only needs to occur at startup.

This design also allows for files to be added and removed at will without the program breaking, which is important for flexibility.

---
