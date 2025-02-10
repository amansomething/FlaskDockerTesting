# Flask and Docker Testing

## Setup
Create a `.env` file with the following contents in the root directory:

```
FLASK_APP="app.py"
PORT="8000"
HOST="0.0.0.0"
```

The port can be adjusted if you are already using it for something else.

## Usage

Assuming you are in the directory with the compose.yml file:

- Run with:

```bash
  docker compose up -d
```

- Stop with:

```bash
  docker compose down
```

- Access the app at: `http://localhost:8000`

## Additional Notes
Code changes will be reflected without needing to rebuild or reload the container, unless the app crashes.
In that case, run `docker compose up -d` again.

I used `docker init` to generate the initial docker-related files.

Exercise for the reader: What's up with the `-d` flag? What happens if you don't use it?
