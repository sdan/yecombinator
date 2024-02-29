# yecombinator
search all of kanye's tweets and lyrics with vlite2, a simple vector db


## Setup

1. Install the Python dependencies:

```bash
pip install -r requirements.txt
```

2. Run the Flask application:

```bash
python main.py
```

The application will be accessible at `http://localhost:5000`.

## Usage

To build and run the Docker image:

1. Build the Docker image:

```bash
docker build -t my-flask-app .
```

2. Run the Docker container:

```bash
docker run -p 5000:5000 my-flask-app
```

The application will be accessible at `http://localhost:5000`.

## GitHub Actions

The GitHub Actions workflow in `.github/workflows/build.yaml` builds the Docker image whenever you push to the `main` branch.

## License

This project is licensed under the terms of the MIT license.