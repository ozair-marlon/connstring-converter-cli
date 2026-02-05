# Connstring Converter CLI

A CLI tool to convert connection details into various connection string formats for frameworks like Prisma, Spring Boot (JDBC), and SQLAlchemy.

## Local Development

To set up the project for local development:

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd connstring-converter-cli
    ```

2.  **Create and activate a virtual environment (Python 3.11+ recommended):**
    ```bash
    python -m venv .venv
    # On Windows:
    .venv\Scripts\activate
    # On macOS/Linux:
    source .venv/bin/activate
    ```

3.  **Install the project in editable mode:**
    ```bash
    pip install -e .
    ```

4.  **Run the CLI locally:**
    ```bash
    connstring-converter --help
    connstring-converter --db-type postgresql --host localhost --user myuser --password mypass --database mydb
    ```

## Installation via Pipx

`pipx` is recommended for installing Python applications in isolated environments.

1.  **Install pipx (if you haven't already):**
    ```bash
    python -m pip install --user pipx
    python -m pipx ensurepath
    ```

2.  **Install the CLI from the current directory:**
    ```bash
    cd /path/to/connstring-converter-cli
    pipx install .
    ```

3.  **Run the installed CLI:**
    ```bash
    connstring-converter --help
    connstring-converter --db-type postgresql --host localhost --user myuser --password mypass --database mydb
    ```

## Usage

The `connstring-converter` CLI tool helps you generate connection strings for different database types and frameworks.

### Getting Help

To see all available options and commands, use the `--help` flag:

```bash
connstring-converter --help
```

### Generating Connection Strings

By default, the tool will generate PostgreSQL connection strings using common default values (e.g., host `localhost`, port `5432`, user `user`, password `password`, database `mydatabase`, schema `public`).

```bash
connstring-converter
```

### Specifying Connection Details

You can customize the connection details using the following options:

*   `-d`, `--db-type`: Database type (e.g., `postgresql`). Currently, only `postgresql` is supported.
*   `-h`, `--host`: Database host.
*   `-p`, `--port`: Database port.
*   `-u`, `--user`: Database user.
*   `-P`, `--password`: Database password.
*   `-D`, `--database`: Database name.
*   `-s`, `--schema`: Database schema (primarily for Prisma/PostgreSQL).

**Example with custom details:**

```bash
connstring-converter \
  --db-type postgresql \
  --host my.database.server \
  --port 5433 \
  --user admin \
  --password your_secure_password \
  --database production_db \
  --schema app_schema
```

This will output the generated connection strings for Prisma, Spring Boot (JDBC), and SQLAlchemy, ready to be used in your `.env` files or application configurations.