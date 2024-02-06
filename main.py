# Import necessary libraries
from openai import OpenAI
import sys
import platform
import pathlib
import os
import shutil
import re
import json

from log_writer import logger
import config
import build

version = "Alpha 0.2"

logger(f"Launch. Software version {version}, platform {sys.platform}")
logger(f"""Configs: 
BASE_URL = {config.BASE_URL}
CODING_MODEL = {config.CODING_MODEL}
BETTER_DESCRIPTION_MODEL = {config.BETTER_DESCRIPTION_MODEL}
ENABLE_BETTER_DESCRIPTION = {config.ENABLE_BETTER_DESCRIPTION}
""")

# Initialize the OpenAI client
client = OpenAI(api_key=config.API_KEY, base_url=config.BASE_URL)
logger("Initialized the OpenAI client.")

def askgpt(system_prompt, user_prompt, model_name):
    """
    Interacts with ChatGPT using the specified prompts.

    Args:
        system_prompt (str): The system prompt.
        user_prompt (str): The user prompt.

    Returns:
        str: The response from ChatGPT.
    """
    # Define the messages for the conversation
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    print("system: " + system_prompt)
    print("user: " + user_prompt)

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

if sys.platform.startswith('linux') or sys.platform.startswith('daiwin'):
    clear_command = "clear"
elif sys.platform.startswith('win'):
    clear_command = "cls"

def generate_plugin():
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
    os.system(clear_command)

    print("[2/3] Creating project and copying the codes...")
    text_to_action(code_reponse, artifact_name, package_list)
    os.system(clear_command)

    print("[3/3] Building project.")
    print("The first build can take 5 minutes or even more, as Maven needs to download a lot of files. This depends somewhat on your network. You're better off doing something else during this long wait.")
    project_path = "projects/" + artifact_name
    build_result = build.build_project(project_path)

    make_response(build_result)

def make_response(build_result):
    if "Error:" in build_result:
        print("This may be due to a bug in the ChatGPT writeup. Typically, GPT4 writes more accurate code. So you should probably toggle CODING_MODEL to gpt-4 in config.py. In later releases, we'll add the ability to have ChatGPT fix bugs automatically, but not yet in the version you're using. You can start the program again and enter the same description to have ChatGPT regenerate the code.")
        logger(f"Build failed. {build_result}")
        print(build_result)
        regenerate = input("Regenerate codes? (Y/n) ")
        if regenerate == "n":
            pass
        else:
            generate_plugin()
    else:
        print(build_result)
        logger(f"Plugin is ready.")
        print(f"Congratulations! Your plugin is ready. Now add the plugin to the projects/{artifact_name}/target directory and just find the jar file and put it in your server's plugins folder.")
        print("BukkitGPT is an open source and free project. Feel free to make pull requests. If you can, you can sponsor this project: https://www.buymeacoffee.com/baimoqilin")

print("Welcome to BukkitGPT, an open source, free, AI-powered Minecraft Bukkit plugin generator developed by BaimoQilin (@Zhou-Shilin). Don't forget to check out the config.py configuration file, you need to fill in the OpenAI API key.")

print("\n")
print("[1/3] Let's start by nameing your plugin! The name should be in English and without spaces.")
artifact_name = input("(artifact_name) ")
logger(f"artifact_name = {artifact_name}")
os.system(clear_command)
print("[2/3] What features do you want your plugin to have? Please describe as clearly and thoroughly as possible. For example, does it require any commands to be registered? If you think you're inexperienced in this aspect of prompt engineering, we recommend you turn on the better description option in config.py.")
description = input("(description) ")
logger(f"description = {description}")
os.system(clear_command)
print("[3/3] What is the package id of your plugin? If you have a domain name like baimoqilin.top, you should write the domain name backwards and add the name of your plugin at the end (no spaces), for example if my plugin is called demo, then you should fill in top.baimoqilin.demo.")
package_id = input("(package_id) ")
logger(f"package_id = {package_id}")
os.system(clear_command)

working_path = package_to_path(package_id)
package_list = package_id_to_list(package_id)

if config.ENABLE_BETTER_DESCRIPTION == True:
    print("[0/3] Generating better description")
    description = askgpt(config.SYS_BETTER_DESCRIPTION, config.USR_BETTER_DESCRIPTION, config.BETTER_DESCRIPTION_MODEL)
    logger(f"better description: {description}")
    os.system(clear_command)

generate_plugin()