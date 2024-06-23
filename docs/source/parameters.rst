Parameters
==========

Profile
-------

This section features a single parameter **Profiles** (it was called **System** in previous versions) which allows you to choose a window profile. For that select profile from 0 to 4:

.. image:: images/03_parameters_profile.gif
   :width: 50%

.. note::
    Custom profiles aren't currently supported due to dependencies on specific parameters for hinges, handles, and striker plates. Feel free to contact us for specific profile requests.

Size
----

This section includes parameters **Width** and **Height** for adjusting the width and height of the window.

Window Parameters
-----------------

This section includes parameters for centering the window, enabling frame-only window, and realizing instances.

Origin in Center
    Positions the window in the center of the geometry bounding box.

    .. image:: images/03_parameters_origin.gif

Frame Only
    Disables sashes leaving only the frame with glass.
 
    .. image:: images/03_parameters_frame.gif
        :alt: Frame Only
        :width: 320
        :height: 320
        :align: center

Realize instances
    Converts instances into real geometry.
 
    .. image:: images/03_parameters_instances.gif
        :alt: Realize Instances
        :width: 320
        :height: 320
        :align: center

Rotation Settings
-----------------

This section includes parameters for adjusting turn and tilt rotations of the sash.

Turn Rotation
    Sets the turn angle of the sash.
Tilt Rotation
    Sets the tilt angle of the sash, constrained to the size of the scissors.
Left Turn Rotation
    Active when the **Impost** is turned on. Sets the turn angle of the left sash.
Left Tilt Rotation
    Active when the **Impost** is turned on. Sets the tilt angle of the left sash.

Handle Settings
---------------

This section includes parameters for handle type, height, and rotation.

Handle
    Choose from different handle types or add a custom handle.
    
    .. image:: images/03_parameters_handle.gif
        :alt: Handle
        :width: 320
        :height: 320
        :align: center

Custom Handle Height
    Allows setting the height position of the handle manually.
Handle Height
    Active when the Custom Handle Height is turned on. Adjust the handle's height.
    
    .. image:: images/03_parameters_handle_height.gif
        :alt: Handle Height
        :width: 320
        :height: 320
        :align: center

Handle Rotation
    Sets the rotation of the handle. When the **Impost** is activated, it sets the rotation of the right sash’s handle.
Left Handle Rotation
    Active when **Impost** is turned on. Sets the rotation of the left sash’s handle.

Glazing Settings
----------------

This section allows you to choose between double or triple glazing.

Glazing
    Choose between double glazed (0) and triple glazed (1) windows.
    
    .. image:: images/03_parameters_glazing.gif
        :alt: Glazing
        :width: 320
        :height: 320
        :align: center

Impost Settings
---------------

This section includes parameters for the impost (vertical post in the window frame) and sashes.

Impost
    Activate or deactivate the impost.
    
    .. image:: images/03_parameters_impost.gif
        :alt: Impost
        :width: 320
        :height: 320
        :align: center

Left/Right Sash
    Switch between left and right sashes. Only active when **1/2 Sashes** is off.
   
    .. image:: images/03_parameters_impost_left_right.gif
        :alt: Left or Right Sash
        :width: 320
        :height: 320
        :align: center

1/2 Sashes
    Switch between 1 or 2 sashes.
    
    .. image:: images/03_parameters_impost_one_two.gif
        :alt: One or Two Sashes
        :width: 320
        :height: 320
        :align: center

Middle Section
    Activate distance between 2 sashes.
    
    .. image:: images/03_parameters_impost_middle.gif
        :alt: Middle Section
        :width: 320
        :height: 320
        :align: center

Impost Centered
    Automatically calculate even space for sashes and impost frame.
    
    .. image:: images/03_parameters_impost_centered.gif
        :alt: Impost Centered
        :width: 320
        :height: 320
        :align: center

Impost Frame Width
    Sets the width of the impost frame (**Impost Centered** must be **turned off**). This works for both 1 and 2 sash windows.
    
    .. image:: images/03_parameters_impost_width.gif
        :alt: Impost Frame Width
        :width: 320
        :height: 320
        :align: center

Stulp Settings
--------------

This section includes parameters for two-sash windows without an impost.

Stulp
    Activate two-sash window without an impost.

    .. image:: images/03_parameters_stulp.gif
        :alt: Stulp
        :width: 320
        :height: 320
        :align: center

Right/Left
    Switch between right or left leading sash.

    .. image:: images/03_parameters_stulp_right_left.gif
        :alt: Stulp Leading Sash
        :width: 320
        :height: 320
        :align: center

Materials
---------

This section allows you to assign materials to your window.

.. warning::
    For the materials to work correctly for Mapping, choose **UV Map** node and select UVMap (in some cases, **Realize Instances** must be turned on in the WindowGen Modifier).
    
        .. image:: images/03_parameters_materials.png
            :alt: Materials
            :align: center
        
.. note::
    - **UVMaps:** The window includes necessary UVMaps, although there may be rotation issues at certain widths due to limitations in controlling UV unwrapping in geometry nodes.
    - **Spacer Material:** If you wish to change the spacer material, it's recommended to adjust the existing material to your needs as it contains a custom bump map for a realistic look and helps to reduce extra geometry for the spacer.