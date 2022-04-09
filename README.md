# Eterlast's challenge
## Running it
### With docker
cd to the root of this repo and run `./geoffrey start`. That will download the image and run a container from it.

### Just python
This repo uses `poetry`, so you should use it in order to install all dependencies with it. If you're not convinced, just make sure you read `pyproject.toml` to install the required libraries.

Once you've got your dependencies in place, run `python manage.py runserver` and open the browser at the host indicated by `runserver`.

#### What's the difference?
The image with docker is loaded on purpose with the SQLite database I used so you got some objects in there already. I'm not uploading that to this repo, so running it with python will create a fresh database.

