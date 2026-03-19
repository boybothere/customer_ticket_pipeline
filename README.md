# Customer Ticket Ingestion Pipeline

![PyPI version](https://img.shields.io/pypi/v/customer_ticket_pipeline.svg)

An automated backend pipeline to ingest and split customer support tickets

* GitHub: https://github.com/boybothere/customer_ticket_pipeline/
* PyPI package: https://pypi.org/project/customer_ticket_pipeline/
* Created by: **[Adrian J Fernandes](https://github.com/boybothere)** | GitHub https://github.com/boybothere | PyPI https://pypi.org/user/boybothere/
* Free software: MIT License

## Features

* TODO

## Documentation

Documentation is built with [Zensical](https://zensical.org/) and deployed to GitHub Pages.

* **Live site:** https://boybothere.github.io/customer_ticket_pipeline/
* **Preview locally:** `just docs-serve` (serves at http://localhost:8000)
* **Build:** `just docs-build`

API documentation is auto-generated from docstrings using [mkdocstrings](https://mkdocstrings.github.io/).

Docs deploy automatically on push to `main` via GitHub Actions. To enable this, go to your repo's Settings > Pages and set the source to **GitHub Actions**.

## Development

To set up for local development:

```bash
# Clone your fork
git clone git@github.com:your_username/customer_ticket_pipeline.git
cd customer_ticket_pipeline

# Install in editable mode with live updates
uv tool install --editable .
```

This installs the CLI globally but with live updates - any changes you make to the source code are immediately available when you run `customer_ticket_pipeline`.

Run tests:

```bash
uv run pytest
```

Run quality checks (format, lint, type check, test):

```bash
just qa
```

## Author

Customer Ticket Ingestion Pipeline was created in 2026 by Adrian J Fernandes.

Built with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) project template.
