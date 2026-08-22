---
title: "Object Property Reference"
id: 1500009590301
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009590301-Object-Property-Reference
updated_at: 2021-07-24T05:54:28Z
---

# Object Property Reference

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589621-Other-Operators)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590661-Report-Object-Properties)

# Object Property Reference

This topic is an overall introduction to the properties of objects in Logi JReport Designer. It explains the properties shown in the [Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500009590661-Report-Object-Properties) and [Catalog Manager,](https://devnet.logianalytics.com/hc/en-us/articles/1500009590321-Catalog-Data-Object-Properties) respectively.

Keep in mind the following while browsing each object for its properties:

* You will start off from a table listing all the properties for an object and what can be achieved with each property.
* Some properties are just used to show related information and cannot be edited.
* Some properties can be[controlled by a formula or expression](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties) . If a formula is selected to control a property, it will be automatically generated as an expression prefixed by an @ sign. Also, some properties must be known by Logi JReport Engine before a page break, so that it can lay out the object. In a formula or expression, the special field PageNumber is the switch for setting the page break calculation time. If PageNumber is used in the formula or expression, then the calculation time will be after the page break, if PageNumber is not used, the calculation time will be before the page break. For this reason, Logi JReport will set the calculation time for controlling whether the formula or expression will be marked as before page break or after page break. For most properties, the property can be controlled by formula or expression at any time without concern about the page break.
* The same property for different objects usually means the same thing, unless otherwise stated.
* The unit of the measurement properties like Width, Height, Thickness and so on is determined by the [Units](https://devnet.logianalytics.com/hc/en-us/articles/1500009588081-Options-Dialog#Display) setting in the Options dialog, which can either be inch or centimeter.
* You can use the quick search toolbar to easily locate the desired property of an object (to display the toolbar, select the **Search** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404893807511/btn_srch.gif) at the upper right corner of the Properties sheet). The search toolbar is closed when you select another object.

  ![Qiuck Search Toolbar button](https://devnet.logianalytics.com/hc/article_attachments/4404889288855/btn_srchtlbr.gif)

  + **Text box**  
     The quick search toolbar treats resource names as strings and searches by consecutive text. Type in the text you want to search for in the text box and the resources containing the matched text will be listed.
  + **X**  
     Clear the text in the text box.
  + ![More Search Option button](https://devnet.logianalytics.com/hc/article_attachments/4404889289239/btn_srchtlbr_adv.gif)  
     Lists more search options.
    - **Highlight All**   
       Specifies whether to highlight all matched text.
    - **Match Case**   
       Specifies whether to search for text that meets the case of the typed text.
    - **Match Whole Word**   
       Specifies whether to search for text that looks the same as the typed text.

**Tip:** When you hover the mouse on any property in Logi JReport Designer, a tip is displayed showing a brief description about the property. You can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889299223/btn_tiphelp.gif) on the tip to open the corresponding help doc or select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889299479/btn_tipcls.gif) to close the tip. If you do not want to display the property tips, uncheck Show tips in the Options dialog (**File** > **Options** > **General** > **Show tips**).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589621-Other-Operators)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590661-Report-Object-Properties)
