.. _customization:

Customization
=============

How to add your custom handle
-----------------------------

To add a custom handle, follow these steps:
            
1. Position your handle to the World Origin.
    
    .. image:: images/04_customization_world_origin.gif
        :width: 75%

2. Navigate to the Right orthographic view (press 3 on your Numpad or press ~ on your keyboard and choose Right).
    
    .. image:: images/04_customization_right_view.gif
        :width: 75%

    .. important::
        Ensure your handle is oriented the same way as in the example provided. **Press Ctrl+A to apply Scale and Rotation**.

3. The origin of your handle must be at the beginning of the backplate geometry. The rotation center of the handle should be appropriately set to prevent clipping issues and ensure correct rotation.
    
    .. image:: images/04_customization_origin.png
        :width: 75%

4. If your handle and its backaplate are joined into a single geometry, separate them to allow independent rotation of the lever while ensuring the backplate remains attached to the sash.
   
    .. image:: images/04_customization_handle_and_base.gif
        :width: 75%

5. Select "Custom" in the Handle Parameters dropdown. Assign your Lever and Backplate geometry to the corresponding sockets.

    .. image:: images/03_parameters_01_handle_cutom.gif
        :width: 75%