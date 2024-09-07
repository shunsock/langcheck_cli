# Langcheck CLI

This is a command line interface for the [langcheck](https://github.com/citadel-ai/langcheck)

## Warning

1. This is not official.
2. This is a prototype. It is not stable and may not work as expected.

## Dependencies

This is the dependencies of the CLI.

1. [uv](https://docs.astral.sh/uv/)
2. [langcheck](https://github.com/citadel-ai/langcheck)

## Installation

This is the installation of the CLI.

```shell
git clone git@github.com:shunsock/langcheck_cli.git
cd langcheck_cli
uv run langcheck --help
```

## Usage

This is the usage of the CLI.

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

## Example

This is an example of how to use the CLI.

```shell
# show metrics of the target
uv run langcheck metrics -f ./example/ai_disclaimer.txt -n ai_disclaimer_similarity
```

output:

```
Configuration Load Succeeded!
Warning: Specifying a revision is not currently supported.
Getting embeddings: 100%|█████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  4.20it/s]
Computing semantic similarity: 100%|██████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 90.51it/s]
  prompt source                                   generated_output reference_output explanation  metric_value
0   None   None  This content was generated automatically using...             None        None      0.169740
1   None   None                             thank you ha ha ha(^^;             None        None     -0.000877
```

you can also filter the metrics by the value.

```shell
# show metrics of the target that is upper than the value (positive)
uv run langcheck metrics -f ./example/sentiment.txt -n sentiment -u 0.5
```

output:

```
Configuration Load Succeeded!
Progress: 100%|███████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  1.98it/s]
  prompt source                                   generated_output reference_output explanation  metric_value
0   None   None  AI is changing the world, and the world will b...             None        None      0.978342
```

we support both upper and lower filters.

```shell
# show metrics of the target that is lower than the value (not toxic)
uv run langcheck metrics -f ./example/toxicity.txt -n toxicity -l 0.3
```

output:

```
Progress: 100%|███████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  4.71it/s]
  prompt source                     generated_output reference_output explanation  metric_value
0   None   None           good, this is a good idea.             None        None      0.000563
1   None   None  This is a good idea; it works well.             None        None      0.000556
2   None   None   That idea doesn't make much sense.             None        None      0.000740
```

## License

[MIT License](LICENSE)
