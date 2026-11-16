.. _parameters:

Parameters
==========

Select a window to see its parameters in the *WindowGen* tab. The settings panel is titled with the name of the active window, so with several windows in the scene you always know which one you are editing.

.. image:: images/03_parameters_settings.gif
   :width: 75%

Every window keeps its own settings. Changing a handle, a profile or a material on one window never affects another.

.. note::
    The panels only show what applies to the selected window type. A fixed frame has no *Rotation* panel, a portal has *Slide* instead of *Rotation*, and so on.

Common Parameters
-----------------

These parameters are shared by most window types.

Window Profile
~~~~~~~~~~~~~~

An icon gallery with the built-in profile systems. Click the preview and pick a profile.

.. image:: images/03_parameters_profile.gif
   :width: 75%

Casement windows offer WHS60, WHS72, Euroline58, Softline70 and Softline82. Sliding windows have their own profile systems, see :ref:`sliding-windows`. Portals use a single profile system and have no *Window Profile* panel.

Profile Resolution
    Sets how finely the rounded corners of the profile are subdivided. Lower it for windows far from the camera, raise it for close-ups.

    .. image:: images/03_parameters_profile_resolution.gif
        :width: 75%

.. note::
    Custom profiles aren't currently supported due to dependencies on specific parameters for hinges, handles, and striker plates. Feel free to contact us for specific profile requests.

.. tip::
    If for some reason there are no previews, press the refresh button next to the gallery.

Size
~~~~

Width and height of the window.

.. image:: images/03_parameters_01_size.gif
   :width: 75%

Rotation Settings
~~~~~~~~~~~~~~~~~

The *Rotation* panel controls how the sashes open. It is available for casement windows that have a sash.

Opening
   Choose between inward and outward opening.

   .. image:: images/03_parameters_opening.gif
        :width: 75%

The turn and tilt angles depend on the window type and are described for each type below.

.. important::
    The tilt angle is limited by the length of the stay arm, as on a real window. Values above the limit have no further effect.

Handle Settings
~~~~~~~~~~~~~~~

The *Handle* panel sets the handle type, its position and its rotation.

Handle
    Choose one of the built-in handles, *No Handle*, or *Custom*.

    .. image:: images/03_parameters_handle.gif
        :width: 75%

Custom Handle
    Use your own handle. Choose *Custom* and assign your objects to *Lever Geometry* and *Backplate Geometry*. Refer to :ref:`customization` on how to prepare them.

    .. image:: images/03_parameters_01_handle_cutom.gif
        :width: 75%

Lever Geometry
    The part that you hold and turn to open or close the window.

    .. image:: images/03_parameters_01_handle_lever.png
        :width: 50%

Backplate Geometry
    Fixed decorative plate around the base of the handle.

    .. image:: images/03_parameters_01_handle_backplate.png
        :width: 50%

Handle Position
    Choose between *Centered* (the middle of the sash) and *Manual*.

    .. image:: images/03_parameters_handle_position.gif
        :width: 75%

Manual Position
    Shown when *Handle Position* is set to *Manual*. Sets the height of the handle.

    .. image:: images/03_parameters_manual_position.gif
        :width: 75%

Handle Rotation
    Sets the rotation of the handle.

    .. image:: images/03_parameters_handle_rotation.gif
        :width: 75%

Glazing Settings
~~~~~~~~~~~~~~~~

Glazing
    Choose between double glazing (two panes, one spacer) and triple glazing (three panes, two spacers). The animation shows the glazing from above.

    .. image:: images/03_parameters_glazing.gif
        :width: 75%

Lites Settings
~~~~~~~~~~~~~~

Lites divide the glass into smaller panes. The panel is available for casement windows.

Horizontal Lites
    Sets the number of horizontal lites.

    .. image:: images/03_parameters_01_lites_h.gif
        :width: 75%

Vertical Lites
    Sets the number of vertical lites.

    .. image:: images/03_parameters_01_lites_v.gif
        :width: 75%

Lites Width
    Sets the width of the lites.

    .. image:: images/03_parameters_01_lites_w.gif
        :width: 75%

Materials
~~~~~~~~~

Assign materials to the parts of the window and control the UV scale.

.. image:: images/03_parameters_material_slots.png
   :width: 50%

Each slot accepts any material in the file. Casement windows have *Hinge* and *Hardware* slots; portals and sliding windows have a *Rail Metal* slot instead.

Texel Density
    Sets the texel density (px/m) for the window. It works together with *Texture Resolution*.

    .. image:: images/03_parameters_material_texel.gif
        :width: 75%

Texture Resolution
    Sets the resolution of the texture. Change it to the resolution of the textures your material uses.

    .. image:: images/03_parameters_material_texture.gif
        :width: 75%

.. tip::
    Texel density controls how many texture pixels (texels) cover a meter of geometry. Use this formula:

    .. code-block:: text

        Texel density = texture resolution (px) / physical size (m)

    Example: a 2048 px texture applied to a 2 m width gives a texel density of 1024 px/m.

    Some texture resources (Megascans, Poliigon, Greyscale Gorilla etc.) include physical size of the texture in meters:

    .. image:: images/03_parameters_materials_uv_scale.png
        :width: 50%

.. warning::
    For the materials to work correctly for mapping, choose the **UV Map** node and select UVMap (in some cases, the **Realize Instances** option must be enabled in the Options section).

    .. image:: images/03_parameters_materials.png
        :width: 75%
        :align: center

.. note::
    - **UVMaps:** The window includes necessary UVMaps, although there may be rotation issues at certain widths due to limitations in controlling UV unwrapping in geometry nodes.
    - **Spacer Material:** If you wish to change the spacer material, it's recommended to adjust the existing material to your needs as it contains a custom bump map for a realistic look and helps to reduce extra geometry for the spacer.

Options
~~~~~~~

Origin in Center
    Moves the origin from the bottom of the window to the center of its bounding box.

    .. image:: images/03_parameters_origin.gif
        :width: 75%

Realize Instances
    Converts instances into real geometry. Keep it off while you work: the viewport is faster and the file smaller. Turn it on when a material or another modifier needs real geometry. The animation shows the vertex count in the viewport statistics.

    .. image:: images/03_parameters_instances.gif
        :width: 75%

Apply Modifier
    Turns the window into a plain mesh.

    .. image:: images/03_parameters_apply.gif
        :width: 75%

    .. warning::
        Once applied, the window is no longer parametric and the settings panel disappears. Use it when you need to edit the final geometry by hand. To hand a window over to another program, use the export described in :ref:`export` instead; it leaves the original window untouched.

Window Single
-------------
 A window featuring a single operable sash that can either tilt or turn.

.. image:: images/03_parameters_06_window.png
   :width: 50%

Rotation Settings
~~~~~~~~~~~~~~~~~

Opening
    Sets the direction in which the sash opens.

    .. image:: images/03_parameters_06_sash_opening.gif
        :width: 75%

Swing Side
    Sets the side the sash is hinged on.

    .. image:: images/03_parameters_06_swing_side.gif
        :width: 75%

Turn Angle
    Sets the turn angle of the sash.

    .. image:: images/03_parameters_06_sash_turn.gif
        :width: 75%

Tilt Angle
    Sets the tilt angle of the sash.

    .. image:: images/03_parameters_06_sash_tilt.gif
        :width: 75%

Window Single Frame
-------------------
 A window with a fixed, non-opening section. It has no *Rotation* and no *Handle* panel.

.. image:: images/03_parameters_07_window.png
    :width: 50%

Window Mullion 1 Sash
---------------------
 A window featuring a single operable sash alongside a fixed, non-opening section.

.. image:: images/03_parameters_03_window.png
   :width: 50%

Size
~~~~

Mullion Centered
    Divides the window into two equal sections. Turned on by default.

    .. image:: images/03_parameters_03_mullion_centered.gif
        :width: 75%

Mullion Section Width
    Sets the width of the fixed section. Shown when *Mullion Centered* is turned off.

    .. image:: images/03_parameters_03_mullion_width.gif
        :width: 75%

Rotation Settings
~~~~~~~~~~~~~~~~~

Sash Position
    Switch the operable sash between the left and the right section.

    .. image:: images/03_parameters_03_left_right.gif
        :width: 75%

Turn Angle
    Sets the turn angle of the sash.

    .. image:: images/03_parameters_03_sash_turn.gif
        :width: 75%

Tilt Angle
    Sets the tilt angle of the sash.

    .. image:: images/03_parameters_03_sash_tilt.gif
        :width: 75%

Window Mullion 2 Sash
---------------------
 A window with two operable sashes that can either tilt or turn.

.. image:: images/03_parameters_04_window.png
   :width: 50%

Rotation Settings
~~~~~~~~~~~~~~~~~

Right Sash Turn
    Sets the turn angle of the right sash.

    .. image:: images/03_parameters_04_sash_turn_r.gif
        :width: 75%

Right Sash Tilt
    Sets the tilt angle of the right sash.

    .. image:: images/03_parameters_04_sash_tilt_r.gif
        :width: 75%

Left Sash Turn
    Sets the turn angle of the left sash.

    .. image:: images/03_parameters_04_sash_turn_l.gif
        :width: 75%

Left Sash Tilt
    Sets the tilt angle of the left sash.

    .. image:: images/03_parameters_04_sash_tilt_l.gif
        :width: 75%

The *Handle* panel of this window has a separate rotation for each handle: *Right Sash Handle* and *Left Sash Handle*.

Window Mullion 3 Sash
---------------------
 A window featuring two operable sashes with a fixed, non-opening section in the middle.

.. image:: images/03_parameters_05_window.png
   :width: 50%

Size
~~~~

Mullion Centered
    Divides the window into three equal sections. Turned on by default.

    .. image:: images/03_parameters_05_mullion_centered.gif
        :width: 75%

Mullion Section Width
    Sets the width of the outer sections. Shown when *Mullion Centered* is turned off.

    .. image:: images/03_parameters_05_mullion_width.gif
        :width: 75%

Rotation Settings
~~~~~~~~~~~~~~~~~

Right Sash Turn
    Sets the turn angle of the right sash.

    .. image:: images/03_parameters_05_sash_turn_r.gif
        :width: 75%

Right Sash Tilt
    Sets the tilt angle of the right sash.

    .. image:: images/03_parameters_05_sash_tilt_r.gif
        :width: 75%

Left Sash Turn
    Sets the turn angle of the left sash.

    .. image:: images/03_parameters_05_sash_turn_l.gif
        :width: 75%

Left Sash Tilt
    Sets the tilt angle of the left sash.

    .. image:: images/03_parameters_05_sash_tilt_l.gif
        :width: 75%

Window Stulp
------------
 A window with two sashes featuring a large, unobstructed opening without a central mullion.

.. image:: images/03_parameters_08_window.png
   :width: 50%

Rotation Settings
~~~~~~~~~~~~~~~~~

Leading Sash
    Sets which sash carries the handle and opens first.

    .. image:: images/03_parameters_08_left_right.gif
        :width: 75%

Right Sash Turn
    Sets the turn angle of the right sash.

    .. image:: images/03_parameters_08_sash_turn_r.gif
        :width: 75%

Right Sash Tilt
    Sets the tilt angle of the right sash.

    .. image:: images/03_parameters_08_sash_tilt_r.gif
        :width: 75%

Left Sash Turn
    Sets the turn angle of the left sash.

    .. image:: images/03_parameters_08_sash_turn_l.gif
        :width: 75%

Left Sash Tilt
    Sets the tilt angle of the left sash.

    .. image:: images/03_parameters_08_sash_tilt_l.gif
        :width: 75%

Window Awning
-------------
 A top-hinged window that swings outward from the bottom.

.. image:: images/03_parameters_01_window.png
   :width: 50%

Rotation Settings
~~~~~~~~~~~~~~~~~

Tilt Angle
    Sets the tilt angle of the sash.

    .. image:: images/03_parameters_01_sash_tilt.gif
        :width: 75%

Window Hopper
-------------
 A bottom-hinged window that tilts inward from the top.

.. image:: images/03_parameters_02_window.png
   :width: 50%

Rotation Settings
~~~~~~~~~~~~~~~~~

Tilt Angle
    Sets the tilt angle of the sash.

    .. image:: images/03_parameters_02_sash_tilt.gif
        :width: 75%

.. _portal-windows:

Portal Windows
--------------
 Lift and slide doors. Seven schemes are available; the letter follows the usual naming of lift-and-slide schemes.

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Preset
     - Layout
   * - Portal A
     - One sliding sash and one fixed section.
   * - Portal C
     - One sliding sash in the middle of two fixed sections.
   * - Portal C4
     - Two sliding sashes that meet in the middle, with a fixed section on each side.
   * - Portal D
     - Two sliding sashes, each with its own handle.
   * - Portal F
     - Four sliding sashes.
   * - Portal K
     - Two sliding sashes at the sides of a fixed middle section.
   * - Portal K4
     - Two sliding sashes at the sides, with the middle divided into fixed sections.

.. image:: images/03_parameters_11_window.png
   :width: 24%
.. image:: images/03_parameters_12_window.png
   :width: 24%
.. image:: images/03_parameters_13_window.png
   :width: 24%
.. image:: images/03_parameters_14_window.png
   :width: 24%

.. image:: images/03_parameters_15_window.png
   :width: 24%
.. image:: images/03_parameters_16_window.png
   :width: 24%
.. image:: images/03_parameters_17_window.png
   :width: 24%

*Top row: Portal A, C, C4, D. Bottom row: Portal F, K, K4.*

Portals share *Size*, *Materials* and *Options* with the other windows. Instead of *Rotation* they have a *Slide* panel, and their *Handle* panel offers the portal handles.

Size
~~~~

Mullion Centered
    Available for Portal A and Portal K. Turn it off to set the width of the fixed section with *Mullion Section Width*.

    .. image:: images/03_parameters_10_mullion.gif
        :width: 75%

Slide
~~~~~

Sash Slide
    Slides the sash along its track. 0 is closed, 1 is fully open.

    .. image:: images/03_parameters_10_slide.gif
        :width: 75%

Sash Position
    Available for Portal A, C and D. Sets the side the sliding sash closes on.

    .. image:: images/03_parameters_10_sash_position.gif
        :width: 75%

Left Sash Slide, Right Sash Slide
    Schemes with two sliding sashes (C4, D, K, K4) have one value for each sash.

    .. image:: images/03_parameters_10_slide_two.gif
        :width: 75%

Left, Mid Left, Mid Right and Right Sash
    Portal F has one value for each of its four sashes.

    .. image:: images/03_parameters_10_slide_four.gif
        :width: 75%

Handle
~~~~~~

Handle
    Choose one of the portal handles, *No Handle*, or *Custom*. With *Custom* you assign your own *Lever Geometry*, *Backplate Geometry* and *Pull Geometry*.

    .. image:: images/03_parameters_10_handle.gif
        :width: 75%

Handle Position
    *Fixed* places the handle 1 m above the floor, *Centered* in the middle of the sash, and *Manual* at the height set with *Manual Position*.

    .. image:: images/03_parameters_10_handle_position.gif
        :width: 75%

Manual Position
    Shown when *Handle Position* is set to *Manual*. Sets the height of the handle.

    .. image:: images/03_parameters_10_handle_manual.gif
        :width: 75%

Handle Rotation
    Sets the rotation of the handle. Schemes with several sliding sashes have one value for each handle (*Left Handle*, *Right Handle* and so on).

    .. image:: images/03_parameters_10_handle_rotation.gif
        :width: 75%

.. _sliding-windows:

Sliding Windows
---------------
 Lightweight sliding windows on two or three rails.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Preset
     - Layout
   * - Sliding Double
     - Two sashes on two rails.
   * - Sliding Double + Mesh
     - Two sashes on two rails and a sliding mosquito screen.
   * - Sliding Mullion
     - One sliding sash next to a fixed section.
   * - Sliding Triple
     - Three sashes on three rails.

.. image:: images/03_parameters_21_window.png
   :width: 24%
.. image:: images/03_parameters_22_window.png
   :width: 24%
.. image:: images/03_parameters_23_window.png
   :width: 24%
.. image:: images/03_parameters_24_window.png
   :width: 24%

*From left to right: Sliding Double, Sliding Double + Mesh, Sliding Mullion, Sliding Triple.*

Window Profile
~~~~~~~~~~~~~~

Sliding windows have their own profile systems (SL44, SL50, SL60, SL64). The gallery shows the ones available for the selected window type.

.. image:: images/03_parameters_20_profile.gif
   :width: 75%

Slide
~~~~~

Front Sash Slide, Back Sash Slide
    Slides each sash along its rail. 0 is closed, 1 is fully open.

    .. image:: images/03_parameters_20_slide.gif
        :width: 75%

Sash Position
    Swaps the front and back sashes.

    .. image:: images/03_parameters_20_sash_position.gif
        :width: 75%

Middle Sash Slide
    Sliding Triple has a third value for the sash on the middle rail.

    .. image:: images/03_parameters_20_slide_triple.gif
        :width: 75%

Sash Slide
    Sliding Mullion has a single sliding sash.

    .. image:: images/03_parameters_20_slide_mullion.gif
        :width: 75%

Mosquito Slide
    Sliding Double + Mesh has a mosquito screen on its own rail. The animation shows the window from outside.

    .. image:: images/03_parameters_20_mosquito.gif
        :width: 75%

Handle
~~~~~~

Handle
    Choose one of the sliding handles, *No Handle*, or *Custom* with your own *Pull Handle* object.

    .. image:: images/03_parameters_20_handle.gif
        :width: 75%

Glazing
~~~~~~~

Glazing
    Choose between single and double glazing. The animation shows the glazing from above.

    .. image:: images/03_parameters_20_glazing.gif
        :width: 75%
