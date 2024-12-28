![cover-v5-optimized](/assets/readme_cover.png)

<p align="center">
  📌 <a href="http://47.251.124.22:8081/use-cases">Introducing Easydoc Workflow File Upload: Recreate Google NotebookLM Podcast</a>
</p>

<p align="center">
  <a href="https://platform.easydoc-ai.sh">Easydoc Platform</a> ·
  <a href="https://easydoc-ai.sh">Documentation</a>
</p>

<p align="center">
    <a href="https://easydoc-ai" target="_blank">
        <img alt="Static Badge" src="https://img.shields.io/badge/Product-F04438"></a>
    <a href="https://easydoc-ai/pricing" target="_blank">
        <img alt="Static Badge" src="https://img.shields.io/badge/free-pricing?logo=free&color=%20%23155EEF&label=pricing&labelColor=%20%23528bff"></a>
    <a href="https://discord.gg/FngNHpbcY7" target="_blank">
        <img src="https://img.shields.io/discord/1082486657678311454?logo=discord&labelColor=%20%235462eb&logoColor=%20%23f5f5f5&color=%20%235462eb"
            alt="chat on Discord"></a>
    <a href="https://reddit.com/r/Easydocai" target="_blank">  
        <img src="https://img.shields.io/reddit/subreddit-subscribers/Easydocai?style=plastic&logo=reddit&label=r%2FEasydocai&labelColor=white"
            alt="join Reddit"></a>
    <a href="https://twitter.com/intent/follow?screen_name=Easydoc_ai" target="_blank">
        <img src="https://img.shields.io/twitter/follow/Easydoc_ai?logo=X&color=%20%23f5f5f5"
            alt="follow on X(Twitter)"></a>
    <a href="https://hub.docker.com/u/langgenius" target="_blank">
        <img alt="Docker Pulls" src="https://img.shields.io/docker/pulls/langgenius/Easydoc-web?labelColor=%20%23FDB062&color=%20%23f79009"></a>
    <a href="https://github.com/langgenius/Easydoc/graphs/commit-activity" target="_blank">
        <img alt="Commits last month" src="https://img.shields.io/github/commit-activity/m/langgenius/Easydoc?labelColor=%20%2332b583&color=%20%2312b76a"></a>
    <a href="https://github.com/langgenius/Easydoc/" target="_blank">
        <img alt="Issues closed" src="https://img.shields.io/github/issues-search?query=repo%3Alanggenius%2FEasydoc%20is%3Aclosed&label=issues%20closed&labelColor=%20%237d89b0&color=%20%235d6b98"></a>
    <a href="https://github.com/langgenius/Easydoc/discussions/" target="_blank">
        <img alt="Discussion posts" src="https://img.shields.io/github/discussions/langgenius/Easydoc?labelColor=%20%239b8afb&color=%20%237a5af8"></a>
</p>

<p align="center">
  <a href="./README.md"><img alt="README in English" src="https://img.shields.io/badge/English-d9d9d9"></a>
  <a href="./README_CN.md"><img alt="简体中文版自述文件" src="https://img.shields.io/badge/简体中文-d9d9d9"></a>
 
</p>


EasyDoc is a powerful multimodal document processing API that transforms unstructured documents into structured, hierarchical JSON, making document assets perfect for your AI and LLM applications. Purpose-built for LLM pipelines, EasyDoc provides high-quality data for model inference, fine-tuning, and optimized context windows.


## Quick start
> Before installing Easydoc, make sure your machine meets the following minimum system requirements:
> 
>- CPU >= 2 Core
>- RAM >= 4 GiB

</br>

The easiest way to start the Easydoc server is through [docker compose](docker/docker-compose.yaml). Before running Easydoc with the following commands, make sure that [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) are installed on your machine:

```bash
cd Easydoc
cd docker
cp .env.example .env
docker compose up -d
```

After running, you can access the Easydoc dashboard in your browser at [http://localhost/install](http://localhost/install) and start the initialization process.

#### Seeking help
Please refer to our [FAQ](https://docs.Easydoc.ai/getting-started/install-self-hosted/faqs) if you encounter problems setting up Easydoc. Reach out to [the community and us](#community--contact) if you are still having issues.

> If you'd like to contribute to Easydoc or do additional development, refer to our [guide to deploying from source code](https://docs.Easydoc.ai/getting-started/install-self-hosted/local-source-code)
