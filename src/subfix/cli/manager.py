from subfix.converter.manager import converter_manager
import argparse
import sys, os

DEFAULT_TARGET_DIRNAME = 'patched'

def main():
    
    default_source_path = os.getcwd()
    default_target_path = os.path.join(default_source_path, 
        DEFAULT_TARGET_DIRNAME)

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', nargs='*', 
        default=[default_source_path], 
        help='source directory or filename (default=<current working directory>)')
    parser.add_argument('-t', '--target', nargs='?', 
        default=default_target_path, 
        help='target directory or filename')
    parser.add_argument('-x', '--extension', nargs='*', 
        default=['srt'], 
        help='list of file extensions you want to process (default=srt)')
    args = parser.parse_args()
    
    # print(args)
    
    for source in args.source:
        if os.path.isdir(source):
            converter_manager.batch_convert(source, 
                target_directory=args.target, extensions=args.extension)
        else:
            converter_manager.convert(os.path.abspath(source), 
                target_directory=os.path.abspath(args.target))

if __name__ == "__main__":
  main()