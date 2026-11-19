import csv
from pathlib import Path


def file_Reporter():
     """Reports Abt files in a Folder"""
     user_input= input("\n Enter the folders you want report on separated by commas: ")
     folder_names = [name.strip() for name in user_input.split(",")]
     path =Path.home()
     grand_total = 0 
     report_rows = []
     for names in folder_names:                     
           folder_search = names.lower()
           found_match = False
           for folder in path.iterdir():
                  folder_name = folder.name.lower()
                  if folder.is_dir() and folder_search == folder_name:
                        found_match = True
                        new_size = 0 
                        print(f"\n Looking for files in {folder_search}")
                        for file in folder.rglob("*"):
                              if file.is_file():
                                    file_name = file.stem
                                    size = file.stat().st_size
                                    MB_size = round(size / (1024*1024), 2 ) 
                                    new_size += MB_size        
                                    print(f"Found:{file_name} , With size:{MB_size} MB")
                                    report_rows.append([folder.name, file.name, MB_size])#save row for csv                                         
                        print(f"The folder size is :{new_size:.2f} MB") 
           grand_total += new_size
           print(f"The total size is :{grand_total:.2f} MB")             
           if not found_match:
                  print(f"\n The input {folder_search} is invalid")
                  print("\n Please input a correct folder name")
     if report_rows:
           output_file = path.home()/ "Desktop"/ "file_report.csv"
           with output_file.open(mode="w", newline="",encoding="utf-8") as f:
                 writer = csv.writer(f)
                 writer.writerow(["Folder", "File Name", "size(MB)"])
                 writer.writerows(report_rows)
           print(f"Report saved to {output_file.resolve()}")     
      
file_Reporter()