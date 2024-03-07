from openai import OpenAI
import sys
import platform
import os
import shutil
import json

from log_writer import logger
import config
import build

def initialize():
    logger(f"Launch. Software version {config.VERSION_NUMBER}, platform {sys.platform}")

def askgpt(system_prompt, user_prompt, model_name):
    """
    Interacts with ChatGPT using the specified prompts.

    Args:
        system_prompt (str): The system prompt.
        user_prompt (str): The user prompt.

    Returns:
        str: The response from ChatGPT.
    """
    client = OpenAI(api_key=config.API_KEY, base_url=config.BASE_URL)
    logger("Initialized the OpenAI client.")

    # Define the messages for the conversation
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    logger(f"askgpt: system {system_prompt}")
    logger(f"askgpt: user {user_prompt}")

    # Create a chat completion
    response = client.chat.completions.create(
        model=model_name,
        response_format={"type": "json_object"},
        messages=messages
    )

    logger(f"askgpt: response {response}")

    # Extract the assistant's reply
    assistant_reply = response.choices[0].message.content
    logger(f"askgpt: extracted reply {assistant_reply}")
    return assistant_reply


def package_to_path(package_id):
    """
    Converts a package ID to its corresponding path.

    Args:
        package_id (str): The package ID (e.g., "top.baimoqilin.demo").

    Returns:
        str: The path corresponding to the package ID (e.g., "src/main/java/top/baimoqilin/demo").
    """
    # Replace dots with slashes and add the appropriate directory structure
    path_elements = package_id.split('.')
    path = '/'.join(path_elements)
    full_path = f"src/main/java/{path}"

    logger(f"package_to_path: full_path {full_path}")
    return full_path

def text_to_action(text, folder_name, package_list):
    text = json.loads(text)
    base_path = "projects"
    source_folder = "template"
    destination_folder = os.path.join(base_path, folder_name)

    # Copy the whole folder from source to destination
    shutil.copytree(os.path.join(base_path, source_folder), destination_folder)

    for item in text["output"]:
        file_path = os.path.join(destination_folder, item["file"])
        code = item["code"]

        # Create necessary directories if not exists
        file_directory = os.path.dirname(file_path)
        os.makedirs(file_directory, exist_ok=True)

        # Write code to the specified file
        with open(file_path, "w") as file:
            file.write(code)
            logger(f"text_to_action: Write file {file_path} content: {code}")
    

def package_id_to_list(package_id):
    # Split the package_id using the dot as the delimiter
    package_list = package_id.split('.')
    return package_list

def generate_plugin(working_path, description, package_id, artifact_name, package_list):
    # Edit info.bukkitgpt
    with open("info.bukkitgpt", "w") as f:
        f.write("{\n")
        f.write(f"""\t\"artifact_name\": \"{artifact_name}\",
\t"description\": \"{description}\",
\t"package_id\": \"{package_id}\"""")
        f.write("\n}")
    # Get the codes
    SYS_GEN = config.SYS_GEN.replace("%WORKING_PATH%", working_path)
    USR_GEN = config.USR_GEN.replace("%DESCRIPTION%", description).replace("%PACKAGE_ID%", package_id).replace("%ARTIFACT_NAME%", artifact_name)
    CODING_MODEL = config.CODING_MODEL
    print("[1/3] Generating codes with model " + CODING_MODEL + "...")
    print("This step may take 1 to 2 minutes, depending on the complexity of the project.")
    code_reponse = askgpt(SYS_GEN, USR_GEN, CODING_MODEL)
    while not "public void onEnable()" in code_reponse:
        print("Bad code, regenerating...")
        logger(f"Bad code, regenerating...")
        code_reponse = askgpt(SYS_GEN, USR_GEN, CODING_MODEL)

    print("[2/3] Creating project and copying the codes...")
    text_to_action(code_reponse, artifact_name, package_list)

    print("[3/3] Building project.")
    print("The first build can take 5 minutes or even more, as Maven needs to download a lot of files. This depends somewhat on your network. You're better off doing something else during this long wait.")
    project_path = "projects/" + artifact_name
    build_result = build.build_project(project_path)

    return build_result
