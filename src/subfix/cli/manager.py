from subfix.converter.manager import converter_manager
import argparse
import sys, os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('source', nargs='+', help='source directory or filename')
    parser.add_argument('-t', '--target', nargs='?', help='target directory or filename')
    parser.add_argument('-x', '--extension', nargs='*', 
        default='srt', help='list of file extensions you want to process (default=srt)')
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