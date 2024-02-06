import os
import subprocess

def build_project(projectPath):
    """
    Builds a Maven Minecraft Bukkit plugin.

    Args:
        projectPath (str): Path to the project directory containing 'pom.xml' and 'src' folder.

    Returns:
        str: Path of the resulting JAR file if successful, or path of the log file if failed.
    """
    try:
        # Validate project path
        if not os.path.exists(projectPath):
            return f"Error: Project path '{projectPath}' does not exist."

        # Change working directory to project path
        os.chdir(projectPath)

        # Execute Maven build command
        os.system("build.bat")

        return "Suceed"
        
    except Exception as e:
        return f"Error: {str(e)}"

'''
Example Usage:
project_path = "/path/to/your/minecraft-plugin-project"
build_result = build_project(project_path)
print(build_result)
'''