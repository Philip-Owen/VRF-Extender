import jinja2
import json
import yaml
import sys
import os


def main():
    if len(sys.argv) == 1:
        print("\n\nPlease specify a file type with either, --json or --yaml\n")
        sys.exit()

    if sys.argv[1] == '--json':
        params_file = 'params.json'
        config_params = json.load(open(params_file))
    elif sys.argv[1] == '--yaml':
        params_file = 'params.yml'
        config_params = yaml.safe_load(open(params_file))
    else:
        print("\n\nPlease specify a file type with either, --json or --yaml\n")
        sys.exit()

    BuildConfigurationFiles(config_params)
    print("Template Build Complete...")


def BuildConfigurationFiles(param):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="."),
                             trim_blocks=True, lstrip_blocks=True)

    output_directory = "_output"
    if not os.path.exists(output_directory):
        os.mkdir(output_directory)

    for templateFile in os.listdir('./templates'):
        template = env.get_template('./templates/' + templateFile)
        result = template.render(param)
        f = open(os.path.join(output_directory,
                              templateFile.split('.')[0]+".txt"), "w")
        f.write(result)
        f.close()

if __name__ == "__main__":
    main()
