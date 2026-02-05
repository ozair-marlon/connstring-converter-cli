import typer
from typing_extensions import Annotated
from rich.console import Console
from urllib.parse import quote_plus

app = typer.Typer(
    help="CLI to convert connection details into various connection string formats.",
    invoke_without_command=True
)
console = Console()


@app.callback()
def generate(
        db_type: Annotated[
            str,
            typer.Option(
                "--db-type", "-d",
                help="Database type (e.g., postgresql).",
                rich_help_panel="Connection Details"
            )
        ] = "postgresql",
        host: Annotated[
            str,
            typer.Option(
                "--host", "-h",
                help="Database host.",
                rich_help_panel="Connection Details"
            )
        ] = "localhost",
        port: Annotated[
            int,
            typer.Option(
                "--port", "-p",
                help="Database port.",
                rich_help_panel="Connection Details"
            )
        ] = 5432,
        user: Annotated[
            str,
            typer.Option(
                "--user", "-u",
                help="Database user.",
                rich_help_panel="Connection Details"
            )
        ] = "postgres",
        password: Annotated[
            str,
            typer.Option(
                "--password", "-P",
                help="Database password.",
                rich_help_panel="Connection Details"
            )
        ] = "postgres",
        database: Annotated[
            str,
            typer.Option(
                "--database", "-D",
                help="Database name.",
                rich_help_panel="Connection Details"
            )
        ] = "postgres",
        schema: Annotated[
            str,
            typer.Option(
                "--schema", "-s",
                help="Database schema (for Prisma/PostgreSQL).",
                rich_help_panel="Connection Details"
            )
        ] = "public",
):
    """
    Generates connection strings for various frameworks.
    """
    console.print(f"[bold blue]Generating connection strings for {db_type.upper()}:[/bold blue]")

    # Encode password for URL
    encoded_password = quote_plus(password)

    # Prisma
    if db_type == "postgresql" or "postgres" or "pg":
        prisma_string = (
            f"{db_type}://{user}:{encoded_password}@{host}:{port}/{database}?schema={schema}"
        )
        console.print(f"  [green]PRISMA:[/green] [yellow]{prisma_string}[/yellow]")

        jdbc_string = (
            f"jdbc:{db_type}://{host}:{port}/{database}?user={user}&password={password}"
        )
        console.print(f"  [green]JDBC (Spring Boot):[/green] [yellow]{jdbc_string}[/yellow]")

        sqlalchemy_string = (
            f"{db_type}+psycopg2://{user}:{encoded_password}@{host}:{port}/{database}"
        )
        console.print(f"  [green]SQLAlchemy:[/green] [yellow]{sqlalchemy_string}[/yellow]")
    else:
        console.print(f"[bold red]Unsupported database type: {db_type}[/bold red]")


if __name__ == "__main__":
    app()


def cli_entry_point():
    app()
