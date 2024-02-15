<div align="center">
<img src="https://cdn.jsdelivr.net/gh/Zhou-Shilin/picx-images-hosting@master/20240202/bukkitgpt-logo.webp"/> 
<h1>BukkitGPT</h1>
<img src="https://img.shields.io/badge/Bukkit-GPT-blue">
<a href="https://github.com/Zhou-Shilin/BukkitGPT/pulls"><img src="https://img.shields.io/badge/PRs-welcome-20BF20"></a>
<img src="https://img.shields.io/badge/License-Apache-red">
<br/>
</div>

## 介绍
> 一句话，AI一键生成定制Minecraft服务器插件，适用于Bukkit, Spigot, Paper, Purpur, Arclight, CatServer, Magma, Mohist等任意基于Bukkit的服务端。

BukkitGPT是一个开源、免费、由ChatGPT4驱动的Minecraft Bukkit插件生成器。它专为小白腐竹开发，用于定制各类小型插件。从代码到构建、调试、修Bug，全部由AI完成。

## 推广

![木桶面板Logo](https://cdn.jsdelivr.net/gh/Zhou-Shilin/picx-images-hosting@master/20240208/woodenbarrelsvr.jpeg)
**木桶高频面板服**  
- 支持130+大型整合包整合包联机体验
- 一键开启 网页管理
- ***独家优惠码`BGPT`***
- i9 10900K 8C10G ***年付低至43.2r每月*** (月付86.4r每月)
- i9 13900K 8C10G ***年付低至62.1r每月*** (月付124r每月)

[官网购买地址 优惠码BGPT](https://vat.yunqiaold.com/index.php?rp=/store/mc)  
***购买时使用优惠码:`BGPT`***  
获得10%off优惠  
支持无条件按剩余时间比例退款  

## 功能

### 核心
- [x] 自动生成代码
- [x] 自动修复Bug
- [ ] ~~自动测试插件~~ 经过长期思考，由于用处不高，这个功能已被移除开发计划。
- [x] AI `Better Description`

### GUI
- [ ] 项目创建
- [ ] 项目管理
- [ ] 设置

![demo](https://cdn.jsdelivr.net/gh/Zhou-Shilin/picx-images-hosting@master/20240210/bukkitgpt-demo.jpeg)

## 原理
当用户键入插件描述时，程序让`gpt-3.5-turbo`优化prompt，然后将优化后的prompt给`gpt-4`。`gpt-4`将以json格式返回编写的代码，举个栗子：
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
程序解析返回的json，复制整个“projects/template”文件夹并将其命名为“artifact_name”，并将json中的代码放入每个文件中。最后，程序使用maven构建插件。

## 运行环境
您可以在任何带有[Java](https://www.azul.com/downloads/)、[Maven](https://maven.apache.org/)、[Python 3+](https://www.python.org/)的计算机上使用BukkitGPT。

您需要安装这些Python轮子：
```
pip install openai
pip install re
pip install pathlib
```

## 快速开始
1. 从[Releases页面](https://github.com/Zhou-Shilin/BukkitGPT/releases)下载`Source Code.zip`并解压缩。
2. 编辑`config.py`，填写你的OpenAI ApiKey。如果你不知道怎么做，请记住[谷歌](https://www.google.com/)和[Bing](https://www.bing.com/)永远是你最好的朋友。
3. 运行`console.py` (bash `python console.py`)，按照提示输入插件名称、描述和Package ID。
4. 将您的插件从`projects/<artifact_name>/target/<artifact_name>-<version>.jar`复制到您的服务器`plugins/`文件夹。
5. 重新启动服务器，享受由GPT4驱动的插件。

## Troubleshooting

### The POM for org.spigotmc:spigot:jar:1.13.2-R0.1-SNAPSHOT
[下载BuildTools](https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar)到一个空文件夹中，双击运行，在设置/选择版本中选择"1.13.2"，点击右下角的 `Compile`并等待运行结束（中国大陆地区因下载速度较慢，请自行解决）。然后到你的BukkitGPT文件夹, 在`projects/插件名称`中双击`build.bat`。你的插件会在`projects/插件名称/target`文件夹。

## 贡献
如果你喜欢这个项目，你可以给这个项目点一个star，或者[提交Issue](https://github.com/Zhou-Shilin/BukkitGPT/issues)、[Pull request](https://github.com/Zhou-Shilin/BukkitGPT/pulls)来帮助它变得更好！

## 开源协议
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
