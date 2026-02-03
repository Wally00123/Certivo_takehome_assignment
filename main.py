'''
IMPORTS

llama_cpp       :   The main AI implementation for the chatbot
parse_files.py  :   Python program that helps to parse information from 
                        pdf and html files into a format that is usable
                        by python programs like this for further use
glob            :   for finding files, used to locate the .gguf file
'''
from llama_cpp import Llama
import parse_files as pf
import glob


'''
Main

@Inputs:    None
@Output:    None
'''
def main():
    print("Loading model, please wait...\n")
    model_files = glob.glob('Model\\*.gguf', recursive=True)

    if len(model_files) == 0:
        print("No valid .gguf file found in the \"Model\" folder, exiting.")
        return

    llm = create_model(model_files[0])

    print("Initializing Data, please wait...\n")
    data = pf.get_data_words()

    user_input = ""

    while user_input != "Quit":
        # dummy_prompt = "How many parts contain a substance bar?"  # replace
        user_input = input("How can I help you?  (Enter \"Quit\" to exit [case sensitive]):")
        if user_input == "Quit":
            return
        
        prompt = generate_prompt(user_input, data)

        print("\nLoading response...\n")
        response = get_responses(llm=llm, prompt=prompt, temp=0.75)

        print(response['choices'][0]['message']['content'])
        print("\n\n")


'''
Loads and creates the LLM instance locally to act as the chatbot

@Inputs:    (Optional) - model_path:str -> path to model (type .gguf)
@Output:    llm
'''
def create_model(model_path:str = None):
    if model_path is None:
        # model_path="E:\\GGUF Models\\gpt-oss-20b-UD-Q4_K_XL.gguf"
        print("No valid .gguf file found in the \"Model\" folder, exiting.")
        exit(0)

    llm = Llama(model_path=model_path, verbose=False, n_ctx=64000)

    return llm


'''
Takes the inputted data, feeds it to the LLM, and returns the response

@Inputs:    llm -> instance of model
            prompt:str -> the prompt to feed into the model
            (optional) temp:float -> temperature of model, default = 0.25
@Output:    None
'''
def get_responses(llm, prompt:str, temp:float=0.25):
    response = llm.create_chat_completion(
        messages=[
            {"role": "system", "content": prompt}
        ], temperature=temp
    )

    return response


'''
Create the prompt to be fed into the chatbot using the users input and
additonal data as needed

@Inputs:    user_prompt:str -> user inputted prompt
            (Optional) file_data -> Contexual data for LLM
@Output:    prompt -> Generated prompt
'''
def generate_prompt(user_prompt:str, file_data=None):
    prompt = f"{user_prompt} - Use the following data for context: {file_data}"

    return prompt


# Main
if __name__ == "__main__":
    main()