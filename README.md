<div align="center">
<img src="https://cdn.jsdelivr.net/gh/Zhou-Shilin/picx-images-hosting@master/20240202/bukkitgpt-logo.webp"/> 
<h1>BukkitGPT</h1>
<img src="https://img.shields.io/badge/Bukkit-GPT-blue">
<a href="https://github.com/Zhou-Shilin/BukkitGPT/pulls"><img src="https://img.shields.io/badge/PRs-welcome-20BF20"></a>
<img src="https://img.shields.io/badge/License-Apache-red">
<br/>
</div>

## Introduction
> Give GPT your idea, AI generates customized Minecraft server plugins with one click, which is suitable for Bukkit, Spigot, Paper, Purpur, Arclight, CatServer, Magma, Mohist and other Bukkit-based servers.

BukkitGPT is an open source, free, AI-powered Minecraft Bukkit plugin generator. It was developed for minecraft server owners who are not technically savvy but need to implement all kinds of customized small plugins. From code to build, debug, all done by gpt.

## Advertisement
Contact: [admin@baimoqilin.top](mailto:admin@baimoqilin.top)
Advertising revenue will be split among contributors in proportion to their contribution.

## Features
- [x] Core: Automatically generate code
- [x] Core: Automatically fix bugs
- [ ] Core: Automatically test plugins ~~(Finish on February 8 at the latest)~~ *The development program has been delayed for some reason.*
- [x] Core: AI `Better Description`
- [ ] Panel: Projects management (Finish on February 20 at the latest)
- [ ] Panel: GUI (Finish on February 20 at the latest)

## How it works
When the user types the plugin description, the program lets `gpt-3.5-turbo` optimize the prompt, and then gives the optimized prompt to `gpt-4`. `gpt-4` will return it in json format, for example:
```
{
    "output": [
        {
            "file": "%WORKING_PATH%/Main.java",
            "code": "package ...;\nimport org.bukkit.Bukkit;\npublic class Main extends JavaPlugin implements CommandExecutor {\n..."
        },
        {
            "file": "src/main/resources/plugin.yml",
            "code": "name: ...\nversion: ...\n..."
        },
        {
            "file\": "src/main/resources/config.yml",
            "code\": "..."
        },
        {
            "file": "pom.xml",
            "code": "..."
        }
    ]
}
```
The program parses this prompt, copies the entire `projects/template` folder and names it `artifact_name`, and puts the code from the prompt into the each file. Finally the program builds the jar using maven.

## Requirements
You can use BukkitGPT on any computer with [Java](https://www.azul.com/downloads/), [Maven](https://maven.apache.org/), [Python 3+](https://www.python.org/).  

And you need to install these packages:
```
pip install openai
pip install re
pip install pathlib
```

## Quick Start
1. Download `Source Code.zip` from [the release page]([https:///](https://github.com/Zhou-Shilin/BukkitGPT/releases)) and unzip it.
2. Edit `config.py`, fill in your OpenAI Apikey. If you don't know how, remember that [Google](https://www.google.com/) and [Bing](https://www.bing.com/) are always your best friends.
3. Run `main.py` (bash `python main.py`), enter the artifact name & description & package id as instructed to generate your plugin.
4. Copy your plugin from `projects/<artifact_name>/target/<artifact_name>-<version>.jar` to your server `plugins/` folder.
5. Restart your server and enjoy your AI-powered-plugin.

## Troubleshooting

### The POM for org.spigotmc:spigot:jar:1.13.2-R0.1-SNAPSHOT is missing
Solution: [Download BuildTools](https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar), place it in an empty folder, double-click it, choose "1.13.2" in `Settings/Select Version`, click `Compile` in the bottom right corner and let it finish. And then go to your BukkitGPT folder, in `projects/<artifact_name_of_your_plugin>`, double-click `build.bat`. You'll find your plugin in `projects/<artifact_name_of_your_plugin>/target` folder.

## Contributing
If you like the project, you can give the project a star, or [submit an issue](https://github.com/Zhou-Shilin/BukkitGPT/issues) or [pull request](https://github.com/Zhou-Shilin/BukkitGPT/pulls) to help make it better.

## License
```
Copyright [2024] [BukkitGPT Team]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
