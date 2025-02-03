Open WebUI helpers
===
# install
* create venv with python 3.11

``
python3.11 -m venv venv
``
* start the server (otherwise not all folders are created)

``
open-webui serve
``

* create symlink

if already exist

``
ln -sf /media/darkdragon/ssd_data_1to/ai/python_ai/open-webui/venv/lib/python3.11/site-packages/open_webui/data/uploads /media/darkdragon/ssd_data_1to/ai/python_ai/open-webui/uploads-shortcut
``

if not exist

``
ln -s /media/darkdragon/ssd_data_1to/ai/python_ai/open-webui/venv/lib/python3.11/site-packages/open_webui/data/uploads /media/darkdragon/ssd_data_1to/ai/python_ai/open-webui/uploads-shortcut
``

# update open-webui


``pip install --upgrade pip``

``pip install --upgrade open-webui``


# commands

``
open-webui serve
``

# Embeddings models
You can get a full list of available models (compatible with EBert), on the [Ebert website](https://www.sbert.net/docs/sentence_transformer/pretrained_models.html), on follow the link to the huggugface website to add the full link to the model, for instance: sentence-transformers/all-mpnet-base-v2

* Most models of interest can be found and doanloaded from this [huggingface link](https://huggingface.co/spaces/mteb/leaderboard). there you can select reranking models 


default
``
sentence-transformers/all-MiniLM-L6-v2
``

``
mixedbread-ai/mxbai-embed-large-v1
``

``
intfloat/multilingual-e5-large-instruct
``
https://huggingface.co/spaces/mteb/leaderboard
``
Alibaba-NLP/gte-Qwen2-7B-instruct
``

## For multilanguage (including French)
`` sentence-transformers/paraphrase-multilingual-mpnet-base-v2 ``


