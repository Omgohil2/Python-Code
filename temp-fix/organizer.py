import os
import shutil

def organize_folder():
    print("⚡ [Shadow Script] Initializing workspace optimization...")
    
    # Get the current directory where the script is running
    current_dir = os.getcwd()
    
    # Track files moved for the final output log
    files_moved = 0
    
    # Loop through every file in the folder
    for filename in os.listdir(current_dir):
        # Skip the script itself and directories
        if filename == "organizer.py" or os.path.isdir(filename):
            continue
            
        # Get the file extension (e.g., .txt, .png, .pdf)
        file_ext = filename.split('.')[-1].lower() if '.' in filename else None
        
        if file_ext:
            # Name the target folder based on the extension (e.g., "TXT_Files")
            target_folder = f"{file_ext.upper()}_Files"
            
            # Create the folder if it doesn't exist yet
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
                print(f"📁 Created folder: {target_folder}")
                
            # Move the file inside
            shutil.move(filename, os.path.join(target_folder, filename))
            print(f" ╰─> Moved: {filename} to {target_folder}/")
            files_moved += 1

    print(f"\n🚀 Optimization complete. Total files organized: {files_moved}")

if __name__ == "__main__":
    organize_folder()