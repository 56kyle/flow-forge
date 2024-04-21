"""Command-line interface."""

import click


@click.command()
@click.version_option()
def main() -> None:
    """Flow Forge."""


if __name__ == "__main__":
    main(prog_name="flow-forge")  # pragma: no cover
