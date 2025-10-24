import os
from dotenv import load_dotenv
import sys
from google import genai
from google.genai import types

def main():
    load_dotenv()

    args = sys.argv[1:]
    verbose = False
    
    if not args:
        print("Error: No input detected")
        sys.exit(1)
    
    if "--verbose" in args:
        args.remove("--verbose")
        verbose = True
    
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    user_prompt = " ".join(args)
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    
    response = generate_content(client, messages)
    print("Response:")
    print(response.text)
    if verbose == True:
        print(f"User prompt: {user_prompt}")
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
            

        
def generate_content(client, messages):
    response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
    )

    return response
    
        


if __name__ == "__main__":
    main()
