# 3D Fractals
This is the code for my personal passion project: exploring 3d fractals.
Read my blog here: [https://joline990.github.io/](https://joline990.github.io/)

## Demos
A brief explanation of what each demo contains, is described in the readme file of the demos folder.

## How to set up final code?
Follow these instructions or watch the video below.

1. Install blender

    Download blender: [https://www.blender.org/download/](https://www.blender.org/download/)
    
2. Create a new general file & delete all items from the viewport 
    - Click A + X + D
    or
    - Select all objects > right mouse > delete

3. Click tab scripting & open the `final_rhombohedron_fractal.py`

4. Run script
    - Click on play button
    or
    - Option + P
    
    You must see a tab “Fractal” inside the N-panel. Click on that tab. 
    
    Interact with the rhombohedron fractal and have fun!

https://github.com/user-attachments/assets/dc54ea7d-7991-4f57-8311-83a269cc1544


### Add MIDI controller
To connect a midi controller, I used the MidiController add-on: [https://github.com/EldinZenderink/MidiController](https://github.com/EldinZenderink/MidiController).
\
\
Install the full zip as add-on: `Edit > Preferences > Add-ons > Install from Disk...` . Connect your MIDI device and copy the full data path of one of the fractal properties within `Fractal`. Click `Map path`. Change name, min & max.
\
\
To know the min & max → look at the code for each of the custom properties.
