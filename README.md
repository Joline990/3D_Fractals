# 3D Fractals
## Demos
A brief explanation of what each demo contains, is described in the readme file of the demos folder.

## How to set up final code?
Follow these instructions or watch the video below.

1. Install blender
    Download blender: [Link](https://www.blender.org/download/)
    
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

<video width="320" height="240" controls>
  <source src="/footage/Setup project.mp4" type="video/mp4">
</video>

### Add MIDI controller
To connect a midi controller, I used the MidiController add-on: [https://github.com/EldinZenderink/MidiController](https://github.com/EldinZenderink/MidiController).
\
\
Install the full zip as add-on: `Edit > Preferences > Add-ons > Install from Disk...` . Connect your MIDI device and copy the full data path of one of the fractal properties within `Fractal`. Click `Map path`. Change name, min & max.
\
\
To know the min & max → look at the code for each of the custom properties.