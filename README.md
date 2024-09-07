# Langcheck CLI

This is a command line interface for the [langcheck](https://github.com/citadel-ai/langcheck/tree/main)

## Warning

1. This is not official.
2. This is a prototype. It is not stable and may not work as expected.

## Installation

```shell
git clone git@github.com:shunsock/langcheck_cli.git
cd langcheck_cli
uv run langcheck --help
```

## Usage

```shell
Usage: uv run langcheck_cli [options] [sub_commend] ...
Options:
    -h, --help      show help message

Subcommands:
    metrics:
        show metrics of the target
        
        -n, --name          metrics
        -f, --file          file path
        -u, --upper-than    show metrics of the target that is upper than the value
        -l, --lower-than    show metrics of the target that is lower than the value
```