# Corporate Clash Resource Pack Editor
Tool to assist resource pack creators with Music.json

The source code is publicly available for contributions, but if you do not intend on contributing, I recommend you download the pre-built [installers](https://github.com/OpenToontownTools/ClashMusicGUI/releases)
(The installer will eventually be replaced with an Open Toontown Tools launcher which includes auto updating and will be a hub for all Open Toontown Tools applications)

# How-To Guide
### How to edit the music using this application
1. Open the application
2. Set the root folder. This will be the folder where the audio and the phase folders are contained.
![step2](https://raw.githubusercontent.com/OpenToontownTools/web/master/assets/rpehowto/rpe_howto_step2.png)
3. For any song you want to change the file path of, look for it and press Browse. In this example, I will be changing the Sellbot HQ Courtyard theme to the Toontown Infinite Donald's Dreamland Playground theme, which in my pack, is located at `phase_9/audio/bgm/DL_nbrhood.ogg`
![step3](https://raw.githubusercontent.com/OpenToontownTools/web/master/assets/rpehowto/rpe_howto_step3.png)
4. Locate and select the file you want. If you intend to have the game randomly select between different files, you can select multiple in this screen.
![step4](https://raw.githubusercontent.com/OpenToontownTools/web/master/assets/rpehowto/rpe_howto_step4.png)
5. You will now see the new path in place of the old one. All modified paths will be displayed in italics to help you distinguish which ones you have changed and have not.
![step5](https://raw.githubusercontent.com/OpenToontownTools/web/master/assets/rpehowto/rpe_howto_step5.png)
6. To add a holiday override, navigate to the tab of the holiday you want to modify, in this example I will be modifying what song plays on the main menu during halloween.
![step6](https://raw.githubusercontent.com/OpenToontownTools/web/master/assets/rpehowto/rpe_howto_step6.png)
7. Press Add Override
![step7](https://raw.githubusercontent.com/OpenToontownTools/web/master/assets/rpehowto/rpe_howto_step7.png)
8. Find the music you want to replace. You can also select more than one in this list by clicking on multiple. (Note that clicking on one will NOT deselect one you previously clicked on, so you have to click the one you want to deselect.) Then press OK.
![step8](https://raw.githubusercontent.com/OpenToontownTools/web/master/assets/rpehowto/rpe_howto_step8.png)
9. Press Browse on the music to select a file.
![step9](https://raw.githubusercontent.com/OpenToontownTools/web/master/assets/rpehowto/rpe_howto_step9.png)
10. Select the file you want. In this example, I will be using the Toontown Infinite Halloween Theme, which in my pack, is located at `phase_3/audio/bgm/tti_theme_halloween.ogg`
![step10](https://raw.githubusercontent.com/OpenToontownTools/web/master/assets/rpehowto/rpe_howto_step10.png)
11. You will now see the new path. If you want to remove the override at any point, you can press the Remove button.
![step11](https://raw.githubusercontent.com/OpenToontownTools/web/master/assets/rpehowto/rpe_howto_step11.png)
12. After you make any changes, you should always save using the Save button at the bottom. **Currently, closing the application will *NOT* notify you if you have not saved, so be sure to save frequently!**
13. To compile the pack for use in game, press the Compile Resource Pack button. 
![step13](https://raw.githubusercontent.com/OpenToontownTools/web/master/assets/rpehowto/rpe_howto_step13.png)
    * If you haven't set a Panda3D path, go to the Options tab, and browse for one. You must have a semi recent version of the Panda3D SDK, but the specific version doesn't matter.
    ![step13b](https://raw.githubusercontent.com/OpenToontownTools/web/master/assets/rpehowto/rpe_howto_step13b.png)
14. Enter a pack file name. This should only include letters, numbers, spaces, dashes, or underscores.
15. Press OK, the pack will compile.
16. Press OPEN to browse to the outputted file.

![step16](https://raw.githubusercontent.com/OpenToontownTools/web/master/assets/rpehowto/rpe_howto_step16.png)

17. Copy the file to Corporate Clash's contentpacks folder, located at `%localappdata%/Corporate Clash/resources/contentpacks`
![step17](https://raw.githubusercontent.com/OpenToontownTools/web/master/assets/rpehowto/rpe_howto_step17.png)
