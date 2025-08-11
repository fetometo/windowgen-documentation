Working With WindowGen
======================

How to open the WindowGen interface
-----------------------------------

WindowGen is located in the side panel. To open the WindowGen interface, follow these steps:

1. Press **N** to open the side panel.

    .. important::
        Make sure your mouse cursor is over the 3D View before pressing **N**; otherwise Blender may open a different panel.

2. Select the *WindowGen* tab in the side panel.

    .. image:: images/01_starting_up_install5.png
        :width: 75%

How to append WindowGen to your scene
-------------------------------------

Before you add the first window, append WindowGen components into your scene:

1. Press the "Append WindowGen" button.

    .. image:: images/02_working_with_01append.png
        :width: 50%  

2. The button will turn into progress bar, indicating that Blender is loading all the necessary components into your scene. This process typically takes 5–10 seconds, depending on your hardware and Blender version.

    .. image:: images/02_working_with_01loading.png
        :width: 50%

3. Once all the components are loaded, the button will turn grey, and the text "WindowGen Appended" will appear on the button. And the panel "Add Window" will appear as well.

    .. image:: images/02_working_with_01success.png
        :width: 50%

How to add WindowGen Asset Library to the Blender
-------------------------------------------------

WindowGen Asset Library will bring realistic materials to customize the appearance of your windows even further:

1. Press the "Add WindowGen Library" button.

    .. image:: images/02_working_with_03add.png
        :width: 50%  

2. Once the Asset Library is added, the button will turn grey, and the text "WindowGen Library Added" will appear on the button.

    .. image:: images/02_working_with_03success.png
        :width: 50%

3. Navigate to the Asset Browser, and select WindowGen in the libraries list to find the materials.

    .. image:: images/02_working_with_03browser.gif
        :width: 50%

    .. tip::
        For easier search most of the materials have tags: Metal, Plastic, RAL color code, etc.

How to update WindowGen
-----------------------

Once you install the latest version of WindowGen addon, you will be able to update your older projects to this version.

.. note::
    WindowGen automatically finds the latest version on your PC and changes the UI to indicate if update is available.

1. Press the "Update" button.

    .. image:: images/02_working_with_04update.png
        :width: 50%  

2. The button will turn into progress bar, indicating that Blender is updating all the necessary components. This process typically takes 5–10 seconds, depending on your hardware and Blender version.

    .. image:: images/02_working_with_04loading.png
        :width: 50%

3. Once the upgrade is completed, the UI will return to its default state.

    .. image:: images/02_working_with_04success.png
        :width: 50%

How to add new window to the scene
----------------------------------

1. Choose where to place the window: at the World Origin, at the 3D Cursor or at the Selected Face.

    .. image:: images/02_working_with_02origin.gif
        :width: 75%

2. When Selected Face option is chosen. Before adding the window, enter Edit Mode (Tab) and select a Face or an Edge Loop you want your window to be placed at. After selecting a face or edge loop, press **Tab** to return to Object Mode. And add the window (see the next step).

    .. image:: images/02_working_with_02face.gif
        :width: 75%

3. Choose the window type: Casement, Portal or Sliding.

    .. image:: images/02_working_with_02types.gif
        :width: 75%

4. Click on the Window Icon to open the window presets gallery.

    .. image:: images/02_working_with_02pressets.gif
        :width: 75%

5. Choose one of the presets to add it to your scene.

    .. image:: images/02_working_with_02select.gif
        :width: 75%

Now you can adjust the selected preset to your needs. You can navigate to the :ref:`parameters` section of the documentation to find out how to customize your window.

How to export window using WindowGen
------------------------------------

.. warning::
    This feature is experimental. Please report any bugs you encounter.

You can export your window using WindowGen. It will export in the chosen format with the default Blender settings for each of the format.

1. Select the format you want your Window to be exported.
    
    .. image:: images/02_working_with_05format.gif
        :width: 75%

2. Select Export Location.
    .. note::
        By default WindowGen exports selected window to the folder WindowGen_Export, which is created at the same path where your .blend file is saved.

    .. image:: images/02_working_with_05path.gif
        :width: 75%

3. Export Options.
    You have two options:
    
    **Option A: Prepare for Export (Recommended for inspection)**

    1. Press "Prepare for Export".
        
        .. image:: images/02_working_with_05prepare.gif
            :width: 75%
    
    2. The addon will:
        
        - Create a duplicate of your window
        - Move it to a new collection called "WindowGen Export"
        - Apply the WindowGen modifier (keeps other modifiers like Weighted Normal)
        - Separate the window into logical components:
            
            - Frame
            - Sashes (sash1, sash2, etc.)
            - Handles (sash1_handle, sash2_handle, etc.)
            
            .. image:: images/02_working_with_05origin.gif
                :width: 75%
        
        - Set proper origins for each component
        - Create a parent empty object for easy manipulation
        - Clean up unused materials
        
        .. image:: images/02_working_with_05outliner.png
            :width: 75%

    3. You can now:
        
        - Inspect the separated components
        - Make manual adjustments if needed
        - Export manually using File > Export

    **Option B: Export Window (One-click export)**

    1. Click **"Export Window"**
        
    2. The addon will:
        
        - Perform all preparation steps automatically
        - Immediately export to your chosen format and location
        - Display a success message when complete