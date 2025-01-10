import os
import shutil

def createDirectory():

  folderOrigin = "C:\\Users\\edgar\\Desktop"
  folderImg = folderOrigin+"\\images"
  folderFiles = folderOrigin+"\\files"
  folderOthers = folderOrigin+"\\others"

  filesType={"images":[".png", ".jpg", ".jpeg", ".gif", ".webp", ".GIF"],
             "files":[".txt", ".docx", ".doc", ".xls", ".ppt", ".pdf"]}
  try:
    os.mkdir(folderImg)
    os.mkdir(folderFiles)
    os.mkdir(folderOthers)
  except FileExistsError:
   print("Folder already exists!")

  for file in os.scandir(folderOrigin):
    added = False
    locationOriginal = os.path.join(folderOrigin,file.name)

    if os.path.isfile(locationOriginal):
      print("MOVING:",locationOriginal, end=" ")
      for category, extensions in filesType.items():
        for extension in extensions:
          if locationOriginal.endswith(extension):
            destinationFolder = os.path.join(folderOrigin,category,)
            print ("TO ----> ",destinationFolder)
            shutil.move(locationOriginal, destinationFolder)
            added= True
      if not added:
        destinationFolder = os.path.join(folderOrigin,"others",)
        print ("TO:",destinationFolder)
        shutil.move(locationOriginal, destinationFolder)
    

createDirectory()