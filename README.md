<div align="center">
<img src="https://cdn.jsdelivr.net/gh/Zhou-Shilin/picx-images-hosting@master/20240202/bukkitgpt-logo.webp"/> 
<h1>BukkitGPT</h1>
<img src="https://img.shields.io/badge/Bukkit-GPT-blue">
<a href="https://github.com/Zhou-Shilin/BukkitGPT/pulls"><img src="https://img.shields.io/badge/PRs-welcome-20BF20"></a>
<img src="https://img.shields.io/badge/License-Apache-red">
<br/>
</div>

## Introduction
BukkitGPT is an open source, free, AI-powered Minecraft Bukkit plugin generator. It was developed for minecraft server owners who are not technically savvy but need to implement all kinds of customized small plugins. From code to build, debug, all done by gpt.

## TODO
- [x] Automatically generate code
- [x] Automatically build plugin
- [ ] Automatically fix bugs
- [ ] Automatically test plugins
- [x] AI `Better Description`
- [ ] Projects management
- [ ] GUI

## Requirements
You can use BukkitGPT on any computer with [Java](https://www.azul.com/downloads/), [Maven](https://maven.apache.org/), [Python 3+](https://www.python.org/).  
And you need to install these packages:
```
pip install openai
pip install re
pip install pathlib
```

## How to use
1. Download `Source Code.zip` from [the release page]([https:///](https://github.com/Zhou-Shilin/BukkitGPT/releases)) and unzip it.
2. Edit `config.py`, fill in your OpenAI Apikey. If you don't know how, remember that [Google](https://www.google.com/) and [Bing](https://www.bing.com/) are always your best friends.
3. Run `main.py` (bash `python main.py`), enter the artifact name & description & package id as instructed to generate your plugin.
4. Copy your plugin from `projects/<artifact_name>/target/<artifact_name>-<version>.jar` to your server `plugins/` folder.
5. Restart your server and enjoy your AI-powered-plugin.

## Contributing
If you like the project, you can give the project a start, or [submit an issue](https://github.com/Zhou-Shilin/BukkitGPT/issues) or [pull request](https://github.com/Zhou-Shilin/BukkitGPT/pulls) to help make it better.