''' Corporate Clash Music.JSON editor GUI '''

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import ast, builtins, glob, json, os, pathlib, requests, subprocess, sys
from ui_window import Ui_MainWindow
from ui_override import Ui_OverrideUI
from ui_compiledial import Ui_CompilingDialog
from Settings import Settings

class ClashMusicGui(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(ClashMusicGui, self).__init__(*args, **kwargs)

        # Get the path to the Documents library
        from sys import platform
        import ctypes.wintypes
        buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(None, 5, None, 0, buf)
        print(f"Found windows documents library at {buf.value}")
        
        builtins.userfiles = os.path.join(buf.value, 'OpenToontownTools', 'ClashResourcePackEditor')
        
        if not os.path.exists(userfiles):
            pathlib.Path(userfiles).mkdir(parents = True, exist_ok = True)
            
        self.setupSettings()
        
        self.setupUi(self)
        self.root = None
        
        self.identifierToLabel = {
            'default': {},
            'halloween': {},
            'christmas': {},
            'april-fools': {}
        }
        
        self.overrides = {
            'halloween': {},
            'christmas': {},
            'april-fools': {}
        }
        
        # load the music.json
        self.defaultJson = self.getDefaultJson()
        i = 0
        for music in self.defaultJson['default']:
            # Add a row
            rowPos = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPos)
            # Set the first column as the music name
            self.tableWidget.setItem(rowPos, 0, QTableWidgetItem(music))
            
            # Create the second column widget
            # This widget includes a horizontal layout with 2 items
            # a browse button, and the label
            widget = QWidget();
            # Create the Browse button
            browseBtn = QPushButton()
            browseBtn.setText("Browse")
            browseBtn.setMaximumSize(QSize(60, 34))
            # Bind it to a lambda event to pop up a file browser
            browseBtn.pressed.connect(lambda i=music: self.browseForMusic(i))
            
            # Create the label
            lbl = QLabel();
            # By default, we show the default song
            lbl.setText(str(self.defaultJson['default'][music]))
            
            # Add the label to a list of labels for later editing
            self.identifierToLabel['default'][music] = lbl
            
            # Make a horizontal layout to put them together
            horLay = QHBoxLayout(widget)
            horLay.addWidget(browseBtn)
            horLay.addWidget(lbl)
            horLay.setContentsMargins(0, 0, 0, 0);
            widget.setLayout(horLay)

            # Set the widget as the contents of the second column
            self.tableWidget.setCellWidget(i, 1, widget)
            i+=1
        
        # bind the save button to write music.json
        self.saveButton.pressed.connect(self.saveFile)
        
        # bind the compile button to build the .mf
        self.compileButton.pressed.connect(self.compileMultifile)
        
        self.addOverrideButton_HA.pressed.connect(lambda: self.selectOverride('halloween'))
        self.addOverrideButton_WI.pressed.connect(lambda: self.selectOverride('christmas'))
        self.addOverrideButton_AF.pressed.connect(lambda: self.selectOverride('april-fools'))
        
        self.optionsBrowsePandaPath.pressed.connect(self.browseForPanda)
        self.label_3.setText(settings['panda-path'])
        
       
        self.browseForRoot()
        if not self.root:
            sys.exit()
        
        # We are done setting up the window
        # Now show it
        self.show()
        
    def getDefaultJson(self):
        print("Downloading latest music.json file")
        try:
            req = requests.get('https://raw.githubusercontent.com/OpenToontownTools/ClashMusicGUI/master/music.json')
            print("Download complete")
            with open('default.json', 'w') as cache:
                cache.writelines(req.text)
            return req.json()
        except:
            QMessageBox.warning(self, "Clash Resource Pack Editor", "Unable to download latest default music.json file\nCheck your internet connection.\nUsing latest cached download.")
            print("using cached version")
            return json.load(open('default.json'))
        
    def setupSettings(self):
        builtins.settings = Settings(f'{userfiles}/config.ott')
        if 'panda-path' not in settings:
            settings['panda-path'] = 'None'
        
    def selectOverride(self, holiday:str):
        self.dial = OverridePopup()
        self.dial.buttonBox.accepted.connect(lambda: self.addOverride(holiday, self.dial.listWidget.selectedItems()))
        
        for music in self.defaultJson['default']:
            if not music in self.identifierToLabel[holiday]:
                self.dial.listWidget.addItem(QListWidgetItem(music))
        
        self.dial.exec_()
        
    def addOverride(self, holiday:str, musics):        
        for music in musics:
            identifier = music.text()
            self.addOverrideToTable(holiday, identifier, 'None')
        
        
        self.dial.close()
        
    def addOverrideToTable(self, holiday, identifier:str, file:str):
        # todo:put the defualt stuff here too
        
        tables = {
            'halloween' : self.overrideTable_HA,
            'christmas' : self.overrideTable_WI,
            'april-fools': self.overrideTable_AF
        }
        
        table = tables[holiday]
    
        rowPos = table.rowCount()
        table.insertRow(rowPos)
        # Set the first column as the music name
        table.setItem(rowPos, 0, QTableWidgetItem(identifier))

        # Create the second column widget
        # This widget includes a horizontal layout with 2 items
        # a browse button, and the label
        widget = QWidget();
        # Create the Browse button
        browseBtn = QPushButton()
        browseBtn.setText('Browse')
        browseBtn.setMaximumSize(QSize(60, 34))
        # Bind it to a lambda event to pop up a file browser
        browseBtn.pressed.connect(lambda i=identifier: self.browseForMusic(i, holiday))

        
        # Create the label
        lbl = QLabel();
        # By default, we show the default song
        lbl.setText(file)
        
        # Add the label to a list of labels for later editing

        self.identifierToLabel[holiday][identifier] = lbl
        
        # Make a horizontal layout to put them together
        horLay = QHBoxLayout(widget)
        horLay.addWidget(browseBtn)
        horLay.addWidget(lbl)
        
        if holiday != 'default':
            removeBtn = QPushButton()
            removeBtn.setText('Remove')
            removeBtn.setMaximumSize(QSize(60, 34))
            removeBtn.pressed.connect(lambda i=identifier: self.removeOverride(i, holiday))
            horLay.addWidget(removeBtn)
        horLay.setContentsMargins(0, 0, 0, 0);
        widget.setLayout(horLay)

        # Set the widget as the contents of the second column
        table.setCellWidget(rowPos, 1, widget)
        
    def browseForRoot(self):
        lastpath = settings['last-path'] if 'last-path' in settings else ""
        path = QFileDialog.getExistingDirectory(self, "Browse for Root Directory", lastpath)
        self.root = path
        if not self.root: return
        settings['last-path'] = path
        self.rootDisplay.setText(path)
        
        # Detect existing music.json file
        if os.path.exists(f'{self.root}/audio/music.json'):
            # If it exists, open and do everything
            with open(f'{self.root}/audio/music.json') as jsonfile:
                data = json.load(jsonfile)
                if 'default' in data:
                    for identifier in data['default']:
                        self.updateLabel('default', identifier, data['default'][identifier])
                for holiday in ['halloween', 'christmas', 'april-fools']:
                    if holiday in data:
                        for identifier in data[holiday]:
                                self.addOverrideToTable(holiday, identifier, data[holiday][identifier])
                
                
                
    def updateLabel(self, holiday, identifier, text):
        #self.identifierToLabel[holiday][identifier].setText(text)
        if holiday == 'default':
            if text == self.defaultJson[holiday][identifier]:
                self.identifierToLabel[holiday][identifier].setText(text)
            else:
                self.identifierToLabel[holiday][identifier].setText(f"<i>{text}</i>")
        else:
            self.identifierToLabel[holiday][identifier].setText(text)
                
    def removeOverride(self, identifier, holiday):   
        self.updateLabel(holiday, identifier, 'None')
        tables = {
            'halloween' : self.overrideTable_HA,
            'christmas' : self.overrideTable_WI,
            'april-fools': self.overrideTable_AF
        }
        
        table = tables[holiday]
        
        rowNum = -1
        
        for row in range(table.rowCount()):
            idCol = table.item(row, 0)
            if idCol.text() == identifier:
                print(f'found identifier on row {row}')
                rowNum = row
                break
        
        table.removeRow(rowNum)
        del self.identifierToLabel[holiday][identifier]

    def saveFile(self):
        # If the user hasn't selected a root, we tell them they need to
        if not self.root:
            QMessageBox.warning(self, "ClashMusicGui", "You need to specify a pack root!\nClick the '...' button in the bottom left")
            return
            
        with open(f'{self.root}/audio/music.json', 'w') as output:
        
            data = {
                # This doesn't work right now, it prevents the file from loading in clash for some reason
                #'_OpenToontownTools': "This file was generated using the Clash Music GUI. https://github.com/OpenToontownTools/ClashMusicGUI",
                'default': {},
                'halloween': {},
                'christmas': {},
                'april-fools': {}
            }
            
            tables = {
                'default': self.tableWidget,
                'halloween' : self.overrideTable_HA,
                'christmas' : self.overrideTable_WI,
                'april-fools': self.overrideTable_AF
            }
            
            for holiday in tables:
                for row in range(tables[holiday].rowCount()):
                    identifier = tables[holiday].item(row, 0).text()
                    file = self.identifierToLabel[holiday][identifier].text().replace('<i>', '').replace('</i>', '')
                    
                    if '[' in file:
                        file = ast.literal_eval(file)
                    
                    if file != self.defaultJson['default'][identifier] or holiday != 'default':
                        data[holiday][identifier] = file

            for type in ['default', 'halloween', 'christmas', 'april-fools']:
                if len(data[type]) == 0:
                    del data[type]
                        
            output.writelines(json.dumps(data, indent = 4, sort_keys = True))
            QMessageBox.information(self, "Corporate Clash music.json Editor", "Saved!")
        

    def compileMultifile(self):
        if not os.path.exists(settings['panda-path']):
            QMessageBox.warning(self, "ClashMusicGui", "You need to select your Panda3D directory in the OPTIONS tab!")
            return
        self.saveFile()
        packname, _ = QInputDialog.getText(self, "Pack File Name", "Enter a pack filename", text = os.path.basename(self.root))
        
        args = [
            f"{settings['panda-path']}/bin/multify.exe",
            '-c', f'-f{packname}.mf']
            
        # Include all folders / files inside the root
        for path in glob.glob(f'{self.root}/*'):
            # except for .mf files - its likely a previous compiled verison
            if os.path.splitext(path)[1] == '.mf':
                continue
            args.append(os.path.basename(path))
        
        process = subprocess.run(args, shell = True, cwd = self.root, stderr = subprocess.PIPE, universal_newlines=True)


        dial = CompileDialog()
        print(process.stderr)
        out = process.stderr.replace('\n', '<br>')
        dial.output.setText(f'<h2>Command Args</h2>{process.args}<br><h2>Output</h2>{out}<br><h2>Compiling Finished!</h2>')
        dial.buttonBox.setEnabled(True)
        dial.buttonBox.accepted.connect(lambda: subprocess.run(['explorer.exe', '/select,', os.path.normpath(self.root)+f'\\{packname}.mf']))

        dial.exec_()

    def browseForMusic(self, identifier, holiday:str = 'default'):
        # If the user hasn't selected a root, we tell them they need to
        if not self.root:
            QMessageBox.warning(self, "ClashMusicGui", "You need to specify a pack root!\nClick the '...' button in the bottom left")
            return
            
        # to allow the user to select multiple files, we use getopenfilenames
        path, _ = QFileDialog.getOpenFileNames(self, "Browse for OGG file(s)", self.root, "OGG Audio Files (*.ogg)")
        
        # The user has selected more than one file
        if len(path) > 1:
            newpath = []
            for p in path:
                # Make sure the song is INSIDE of the content pack
                if not p.startswith(self.root):
                    dial = QMessageBox(self)
                    dial.setWindowTitle("ClashMusicGui")
                    dial.setText("You need to select a file inside the content pack!")
                    dial.exec_()
                    return
                newpath.append(p.replace(self.root+'/', ''))

            path = newpath
            
        # The user has selected one file
        if len(path) == 1:
            path = path[0]
            
            if not path.startswith(self.root):
                dial = QMessageBox(self)
                dial.setWindowTitle("ClashMusicGui")
                dial.setText("You need to select a file inside the content pack!")
                dial.exec_()
                return
            
            path = path.replace(self.root+'/', '')
            
        # The user selected nothing, so we use 'None' which clash will read to not play any audio
        if len(path) == 0:
            path = "None"

        # Set the text of the label
        #self.lbls[index].setText(str(path))
        self.updateLabel(holiday, identifier, str(path))
        
    def browseForPanda(self):
        settings['panda-path'] = QFileDialog.getExistingDirectory(self, "Browse for Panda3D Root Directory", "C:/")
        self.label_3.setText(settings['panda-path'])

class OverridePopup(QDialog, Ui_OverrideUI):
    def __init__(self, *args, **kwargs):
        super(OverridePopup, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()
        

class CompileDialog(QDialog, Ui_CompilingDialog):
    def __init__(self, *args, **kwargs):
        super(CompileDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint)
        self.show()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ClashMusicGui()
    app.exec_()