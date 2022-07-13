# Python-2022
## This repository contains modern Python resources.

This project introduces new features up to Python3.10.5, which is currently the latest stable version.

Some of these features are little known, such as "The Walrus Operator", among others. :)

This repository is complementary to the following article:

To run this project in your development environment, it is necessary to have docker and docker compose installed, but there is no need to have Python installed.

## Just follow the instructions below:

1 - Run the following command in the project root to download the docker compose dependencies and initially configure the project.

```
docker compose build
```

2 - Then run the next command to create the project container and run the app.py file, which is in the app.

```
docker compose up
```

3 - If you want to run a specific file in the app folder, just run the command below, replacing the "main.py" file with the file you created.

```
docker compose run --rm app sh -c "python main.py"
```

If you have any doubts, add an issue to the project, which I will answer as soon as possible. :)