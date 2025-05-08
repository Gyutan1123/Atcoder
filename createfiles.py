import os
import shutil
import argparse
import datetime

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("prefix")
    parser.add_argument("-n", "--number",required=False, default="")
    args = parser.parse_args()
          

    base_dir = args.prefix
    target_subdir = f"{args.prefix}{args.number}"
    target_dir = os.path.join(base_dir, target_subdir)

    template_file = "template.py"
    files_to_create = ["A.py", "B.py", "C.py", "D.py", "E.py","F.py","G.py"]

    if args.prefix == 'ADT':
      target_dir = "ADT/"+datetime.datetime.today().strftime("%Y-%m-%d")
      files_to_create = ["A.py", "B.py", "C.py", "D.py", "E.py","F.py","G.py","H.py","I.py"]
      
    os.makedirs(target_dir, exist_ok=True)
    
    for filename in files_to_create:
        dest_file = os.path.join(target_dir, filename)
        shutil.copy(template_file, dest_file)

if __name__ == "__main__":
    main()