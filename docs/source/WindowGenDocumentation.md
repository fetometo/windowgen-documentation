# WindowGen Documentation

Welcome to WindowGen

Procedural Window Generator for blender based on real life PVC window
profiles and furniture. In this documentation you can find how to use
the generator, future plans on development and updates.

Supported Blender versions: 3.6+

[**STARTING UP 3**](#starting-up)

> [How to add a generator to your scene
> 3](#how-to-add-a-generator-to-your-scene)

[**WORKING WITH THE GENERATOR 5**](#working-with-the-generator)

> [How to change parameters 5](#how-to-change-parameters)
>
> [Generator structure 5](#generator-structure)

[**PARAMETERS 6**](#parameters)

> [Profiles 6](#profile)
>
> [Size 6](#size)
>
> [Window Parameters 6](#window-parameters)
>
> [Origin in Center 7](#origin-in-center)
>
> [Frame Only 7](#frame-only)
>
> [Realize instances 7](#realize-instances)
>
> [Rotation Settings 8](#rotation-settings)
>
> [Turn Rotation 8](#turn-rotation)
>
> [Tilt Rotation 8](#tilt-rotation)
>
> [Left Turn Rotation 8](#left-turn-rotation)
>
> [Left Tilt Rotation 8](#left-tilt-rotation)
>
> [Handle Settings 9](#handle-settings)
>
> [Handle 9](#handle)
>
> [Custom Handle Height 9](#custom-handle-height)
>
> [Handle Height 9](#handle-height)
>
> [Handle Rotation 10](#handle-rotation)
>
> [Left Handle Rotation 10](#left-handle-rotation)
>
> [Glazing Settings 10](#glazing-settings)
>
> [Glazing 10](#glazing)
>
> [Impost Settings 11](#impost-settings)
>
> [Impost 11](#impost)
>
> [Left/Right Sash 11](#leftright-sash)
>
> [1/2 Sashes 12](#sashes)
>
> [Middle Section 12](#middle-section)
>
> [Impost Centered 13](#impost-centered)
>
> [Impost Frame Width 13](#impost-frame-width)
>
> [Stulp Settings 14](#stulp-settings)
>
> [Stulp 14](#stulp)
>
> [Right/Left 14](#rightleft)
>
> [Materials 15](#materials)

[**CUSTOMIZATION 15**](#customization)

> [How to add custom handle 15](#how-to-add-custom-handle)

[**FUTURE PLANS 20**](#future-plans)

#  

# STARTING UP

## How to add a generator to your scene

To incorporate a generator into your Blender scene, follow these steps:

1.  Click on \"File\" in the top left corner.

2.  Select \"Append...\".\
    ![](media/image23.png){width="2.952755905511811in"
    height="3.2817771216097986in"}

3.  Navigate to the folder where you saved the .blend file containing
    the generator and double-click on it.

4.  Within the file, navigate to the Collection folder.\
    ![](media/image7.png){width="2.952755905511811in"
    height="2.4878543307086614in"}

5.  Select \"!GENERATOR (Append Me)\" and click \"Append\" in the bottom
    right corner.![](media/image25.png){width="6.5in"
    height="3.888888888888889in"}

Your scene should now reflect the changes made by appending the
generator:\
![](media/image10.png){width="6.5in" height="3.4305555555555554in"}

You can easily disable the \"PROFILES\" and \"FURNITURE\" collections as
they include the modeled geometry that is used in the generator such as
PVC profiles and furniture.

# WORKING WITH THE GENERATOR

## How to change parameters

The generator utilizes the geometry nodes modifier. To adjust
parameters, follow these steps:

1.  Select the \"!Generator\" object.

2.  Click on the wrench icon (Modifier Properties) on the right-hand
    side.\
    ![](media/image22.png){width="2.952755905511811in"
    height="3.117267060367454in"}

## Generator structure

The generator is divided into the following sections:

  -----------------------------------------------------------------------
  **Profile**        Choose from 5 build-in profiles.
  ------------------ ----------------------------------------------------
  **Size**           Adjust the size of your window.

  **Window           Customize window features such as centering, sash
  parameters**       disabling, and instance realization.

  **Rotation         Modify sash rotation.
  settings**         

  **Handle           Choose handle type, position, and rotation.
  settings**         

  **Glazing          Select between double or triple glazing.
  settings**         

  **Impost           Control the presence and attributes of the impost.
  settings**         

  **Stulp settings** Configure settings for two-sash windows without
                     impost.

  **Materials**      Assign window materials.
  -----------------------------------------------------------------------

# PARAMETERS

## Profile

This section features a single parameter **Profiles** (it was called
**System** in previous versions), which allows you to choose a window
profile. For that select profile from 0 to 4:

![](media/image32.gif){width="2.952755905511811in"
height="2.952755905511811in"}

*Note that custom profiles aren\'t currently supported due to
dependencies on specific parameters for hinges, handles, and striker
plates. Feel free to contact us for specific profile requests.*

## Size

This section includes parameters **Width** and **Height** for adjusting
the width and height of the window.

##  

## Window Parameters

This section includes parameters for centering the window, enabling
frame-only window, and realizing instances.

### **Origin in Center**

Positions the window in the center of the geometry bounding box.

![](media/image2.gif){width="2.952755905511811in"
height="2.952755905511811in"}

### **Frame Only**

Disables sashes, leaving only the frame with glass.

![](media/image5.gif){width="2.952755905511811in"
height="2.952755905511811in"}

### **Realize instances**

Converts instances into real geometry.

![](media/image17.gif){width="2.952755905511811in"
height="2.952755905511811in"}

## Rotation Settings

This section includes parameters for adjusting turn and tilt rotations
of the sash.

### **Turn Rotation**

Sets the turn angle of the sash.

*When the **Impost** is activated, it sets the turn angle of the right
sash.*

### **Tilt Rotation**

Sets the tilt angle of the sash. It is constrained to the size of the
scissors, automatically ignoring impossible values for the given window
size.

*When the **Impost** is activated, it sets the tilt angle of the right
sash.*

### **Left Turn Rotation**

Active when the **Impost** is turned on. Sets the turn angle of the left
sash.

### **Left Tilt Rotation**

Active when the **Impost** is turned on. Sets the tilt angle of the left
sash. Similar to **Tilt Rotation**, it is constrained to the size of the
scissors.

## Handle Settings

This section includes parameters for handle type, height, and rotation.

### **Handle**

Choose from different handle types or add a custom handle. More on that
[[here]{.underline}](#how-to-add-custom-handle).![](media/image14.gif){width="2.952755905511811in"
height="2.952755905511811in"}

### **Custom Handle Height**

Allows to set the height position of the handle manually.

### **Handle Height**

Active when the **Custom Handle Height** is turned on. Adjust the
handle\'s height.![](media/image28.gif){width="2.952755905511811in"
height="2.952755905511811in"}

### **Handle Rotation**

Sets the rotation of the handle. When the **Impost** is activated, it
sets the rotation of the right sash's handle.

### **Left Handle Rotation**

Active when **Impost** is turned on. Sets the rotation of the left
sash's handle.

## Glazing Settings

This section allows you to choose between double or triple glazing.

### **Glazing**

Choose between double glazed (0) and triple glazed (1)
windows:![](media/image27.gif){width="2.952755905511811in"
height="2.952755905511811in"}

## Impost Settings

This section includes parameters for the impost (vertical post in the
window frame) and sashes.

### **Impost**

Activate or deactivate the impost.

![](media/image29.gif){width="2.952755905511811in"
height="2.952755905511811in"}

### **Left/Right Sash**

Switch between left and right sashes. Only active when **1/2 Sashes** is
off.

![](media/image6.gif){width="2.952755905511811in"
height="2.952755905511811in"}

###  

### **1/2 Sashes**

Switch between 1 or 2 sashes:

![](media/image15.gif){width="2.952755905511811in"
height="2.952755905511811in"}

### **Middle Section**

Activate distance between 2 sashes:

![](media/image33.gif){width="2.952755905511811in"
height="2.952755905511811in"}

###  

### **Impost Centered**

Automatically calculate even space for sashes and impost frame:

![](media/image18.gif){width="2.952755905511811in"
height="2.952755905511811in"}

### **Impost Frame Width**

Sets the width of the impost frame (**Impost Centered** must be **turned
off**). This both works for 1 and 2 sashes window:

![](media/image20.gif){width="2.952755905511811in"
height="2.952755905511811in"}

##  

## Stulp Settings

This section includes parameters for two-sash windows without an impost.

### **Stulp**

Activate two-sash window without an impost:

![](media/image3.gif){width="2.952755905511811in"
height="2.952755905511811in"}

### **Right/Left**

Switch between right or left leading sash:

![](media/image12.gif){width="2.952755905511811in"
height="2.952755905511811in"}

## Materials

This section allows you to assign materials to your window.

For the materials work correctly for Mapping choose **UV Map** node and
select UVMap (in some cases **Realize Instances** must be turned on in
the WindowGen Modifier):

![](media/image1.png){width="6.5in" height="2.0972222222222223in"}

  -----------------------------------------------------------------------
  **UVMaps:** The window includes necessary UVMaps, although there may be
  rotation issues at certain widths due to limitations in controlling UV
  unwrapping in geometry nodes.
  -----------------------------------------------------------------------
  **Spacer Material:** If you wish to change the spacer material, it\'s
  recommended to adjust the existing material to your needs, as it
  contains a custom bump map for a realistic look and helps to reduce
  extra geometry for the spacer.

  -----------------------------------------------------------------------

# CUSTOMIZATION

## How to add custom handle

To add custom handle, follow these steps:

1.  Temporarily disable Generator in the viewport. Activate \"HANDLES\"
    collection inside \"FURNITURE\" collection:

> ![](media/image9.gif){width="3.937007874015748in"
> height="3.937007874015748in"}

2.  Import your custom handle to the \"HANDLES\" collection.\
    *Note that your custom handle must be comparable in sizes to the
    other handles in the collection*:\
    ![](media/image26.gif){width="3.543307086614173in"
    height="3.543307086614173in"}

3.  Position your handle to the World Origin:\
    ![](media/image31.gif){width="3.543307086614173in"
    height="3.543307086614173in"}

4.  Navigate to the Right orthographic view, for that press 3 on your
    Numpad or press \~ on your keyboard and choose **Right**, as it is
    shown below:\
    ![](media/image30.gif){width="3.543307086614173in"
    height="3.543307086614173in"}\
    *Note that your handle must be oriented the same way as it is
    oriented in the example above. **Press Ctrl+A to apply Scale and
    Rotation**.*

5.  Origin of your handle must be at the beginning of the base geometry.
    Additionally, the rotation center of the handle should be
    appropriately set. Adhering to these guidelines is crucial for
    preventing clipping issues with window geometry and ensuring the
    correct rotation of the handle.\
    ![](media/image8.png){width="3.543307086614173in"
    height="3.543307086614173in"}

6.  In cases where your handle and its base are joined into a single
    geometry, it is essential to separate them. This separation allows
    for independent rotation of the handle while ensuring that the base
    remains firmly attached to the sash:\
    ![](media/image24.gif){width="3.543307086614173in"
    height="3.543307086614173in"}

7.  Unhide the Generator and select it.

8.  Navigate to the geometry nodes tab.

9.  Select **Handle Switch** node (it is located on the blue underlay)
    and press Tab to add your handle:\
    ![](media/image11.gif){width="3.543307086614173in"
    height="3.543307086614173in"}

10. Change one of the current handles and its base to your custom
    handle:\
    ![](media/image16.gif){width="4.724409448818897in"
    height="4.724409448818897in"}

#  

# FUTURE PLANS

Currently in the work and will be delivered with the next update:

-   Transom Window:\
    ![](media/image4.png){width="3.937007874015748in"
    height="3.3858267716535435in"}

-   Window Lites:\
    ![](media/image13.png){width="3.937007874015748in"
    height="3.937007874015748in"}

  -----------------------------------------------------------------------
  If you have ideas for new functionalities you\'d like to see
  implemented or specific requirements tailored to your project, please
  don\'t hesitate to reach out to us. We value your feedback and are
  committed to enhancing WindowGen to better suit your needs. Contact us
  to discuss your suggestions or requirements further. We\'re here to
  help! i@mshevchenko.ru
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

# RELEASES

## Version 1.1

-   Initial release

## Version 1.2

-   Added lites

-   Added transom option (awning and hopper types)

-   Optimization. Average face count reduced by 10%

-   UI improvements for Blender 4.1. Added panels
