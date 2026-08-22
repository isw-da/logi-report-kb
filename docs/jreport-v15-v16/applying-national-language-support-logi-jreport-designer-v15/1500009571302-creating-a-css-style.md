---
title: "Creating a CSS Style"
id: 1500009571302
section: "Applying National Language Support - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009571302-Creating-a-CSS-Style
updated_at: 2021-07-24T05:53:41Z
---

# Creating a CSS Style

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009571282-CSS-Styles)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009571322-Managing-CSS-Styles)

# Creating a CSS Style

You can apply a CSS style that is created directly using the properties provided in Logi JReport Designer.

**To create a CSS style in Logi JReport Designer:**

1. Right-click an object in the design area and then select **Save Style** from the shortcut menu. The [New CSS Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009587901-New-CSS-Style-Dialog) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889275031/nwcss.gif)
2. Define the type of the CSS style as required:
   * To create a custom style that can be applied as a class attribute to a range or block of text, select the **Class** option and then enter a name for the style in the Selector Name combo box.

     **Note:** Class names must begin with a period and can contain any combination of letters and numbers (for example, .myhead1). If you don't enter a beginning period, Logi JReport Designer automatically enters it for you.
   * To redefine the default formatting of a specific tag, select the **Tag** option and then select a tag from the Selector Name combo box.
   * To define the formatting for a particular combination of tags or for all tags that contain a specific ID attribute, select the **Advanced** option and then enter one or more tags in the Selector Name combo box or select one from the box.
3. Select the location in which the style will be defined in the Add Selector to Style drop-down list.
   * If you want to create an external style file, select **New Style Sheet File** and select **OK**. Then,
     1. In the Save CSS As dialog, specify the name of the new CSS file.
     2. Select **Save** to save the file and the [CSS Style Definition](https://devnet.logianalytics.com/hc/en-us/articles/1500009586121-CSS-Style-Definition-Dialog) dialog appears.

        ![](https://devnet.logianalytics.com/hc/article_attachments/4404893790743/cssdfntn.gif)
     3. Define the properties of the CSS file. When done, select **Save** to save the CSS file.
   * If you want to embed the style in an existing CSS file, select any of the existing styles and select **OK**. Then,
     1. In the CSS Style Definition dialog, define the properties of the style as required.
     2. When done, select **Save** to save the file.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009571282-CSS-Styles)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009571322-Managing-CSS-Styles)
