---
title: "Object Property Reference"
id: 4405664614935
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664614935-Object-Property-Reference
updated_at: 2022-01-27T20:35:11Z
---

# Object Property Reference

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661751191-XML-Option-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661831319-Report-Object-Properties)

# Object Property Reference

This topic introduces the properties of objects in Designer: the [report object properties](https://devnet.logianalytics.com/hc/en-us/articles/4405661831319-Report-Object-Properties) in the Report Inspector and [catalog data object properties](https://devnet.logianalytics.com/hc/en-us/articles/4405661804439-Catalog-Data-Object-Properties) in the Catalog Manager.

Keep in mind the following while browsing each object for its properties:

* You start off from a table listing all the properties for an object and what you can achieve with each property.
* Designer uses some properties for showing related information only and you cannot edit them.
* You can [use formula or expression to control the value of some properties](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties). When you select a formula to control a property, Designer displays the name of the formula prefixed by the "@" symbol as its value. Furthermore, some properties must be known by Logi Report Engine before a page break, so that it can lay out the object correctly. In a formula or expression, the special field "PageNumber" is the switch for setting the page break calculation time. If a formula or expression uses "PageNumber", the calculation time is after the page break; otherwise, the calculation time is before the page break. For most properties, you can control their values by formula or expression at any time without concerning about the page break.
* The same property for different objects usually means the same thing, unless otherwise stated.
* Designer determines the unit of the measurement properties like Width, Height, Thickness, and so on, by the [Units](https://devnet.logianalytics.com/hc/en-us/articles/4405661667735-Options-Dialog-Box#Display) setting in the Options dialog box, which can either be inch or centimeter.
* You can use the search box to easily locate the desired property of an object (to display the search box, select the **Search** icon ![Search icon](https://devnet.logianalytics.com/hc/article_attachments/4420402315159/btn_srch.gif) at the upper right corner of the Properties sheet). Designer closes the search box when you select another object.

  ![Qiuck Search Toolbar button](https://devnet.logianalytics.com/hc/article_attachments/4420402354327/btn_srchtlbr.gif)

  + **Text box**  
    Type the text you want to search for in the text box and Designer lists the properties containing the matched text.
  + ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420410584727/btn_close1.gif)**Delete icon**  
    Select to clear the text in the text box.
  + ![More Search Option button](https://devnet.logianalytics.com/hc/article_attachments/4420410625175/btn_srchtlbr_adv.gif)**Drop-down icon**  
    Select to list more search options.
    - **Highlight All**  
      Select to highlight all matched text.
    - **Match Case**  
      Select to search for text that meets the case of the typed text.
    - **Match Whole Word**  
      Select to search for text that looks the same as the typed text.
    - **Include Subnode**  
      Designer displays this option only for the search box in the Report Inspector. Select it if you want to perform the property searching within the property list of the selected object and those of its child objects.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420394642839/noteicon.jpg) When you hover the mouse on any property, Designer displays a tip showing a brief description about the property. You can select the **Question Mark**![](https://devnet.logianalytics.com/hc/article_attachments/4420402354583/btn_tiphelp.gif) on the tip to view more information about the property or select **Close**![](https://devnet.logianalytics.com/hc/article_attachments/4420402354839/btn_tipcls.gif) to close the tip. If you do not want to display the property tips, clear **Show tips** in the General category of the Options dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661751191-XML-Option-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661831319-Report-Object-Properties)
