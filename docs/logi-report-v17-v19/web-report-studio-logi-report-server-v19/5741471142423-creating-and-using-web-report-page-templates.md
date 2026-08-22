---
title: "Creating and Using Web Report Page Templates"
id: 5741471142423
section: "Web Report Studio Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741471142423-Creating-and-Using-Web-Report-Page-Templates
updated_at: 2022-10-31T17:18:36Z
---

# Creating and Using Web Report Page Templates

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741464240919-Creating-Web-Reports-Using-the-Wizard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741484883735-Web-Report-Studio-Window-Elements)

# Creating and Using Web Report Page Templates

You can create web report page templates to include standard features such as the company logo, company name, and privacy notices, and apply them to web reports you create. This topic describes how you can create, use, rename, and delete web report page templates.

This topic contains the following sections:

* [Creating Web Report Page Templates](#Create)
* [Dynamically Displaying the Company Logo](#Logo)
* [Setting the Default Page Template for Quick-start Web Reports](#QuickStart)
* [Renaming and Removing Web Report Page Templates](#Remove)

## Creating Web Report Page Templates

To create web report page templates, you should be an administrator with the privilege of publishing resources.

**To create a page template by customizing a built-in template in the Web Report Wizard:**

The Web Report Wizard provides sample page templates for you to define your templates based on.

1. In the Page screen of the Web Report Wizard, make use of **Template1** or **Template2** to customize your page templates. With Template1, you can add your company logo and a report title. With Template2, you can add more items such as company name, title, and report subtitle.
2. Use the ellipsis button ![Insert Image](https://devnet.logianalytics.com/hc/article_attachments/9905577763991/btn_chsr2.gif) to load your company logo.
3. Set the font properties for titles using ![Font button](https://devnet.logianalytics.com/hc/article_attachments/9905615721239/btn_wbrpt_font.gif).
4. Select **Save**. Server displays the Save As dialog box.
5. Select the type **Web Report Template (\*.wsld)**.
6. Type a name for the template in the **File Name** text box.
7. Select **Save** to save the page template.

**To create a page template by editing a report in Web Report Studio:**

1. Open a report in Web Report Studio.
2. Edit the header and footer of the report. The report header and footer are two tabulars. You can split or merge the tabular cells by selecting the **Split** button ![Split button](https://devnet.logianalytics.com/hc/article_attachments/9905577819287/btn_wbrpt_split.gif) or **Merge** button ![Merge button](https://devnet.logianalytics.com/hc/article_attachments/9905577843607/btn_wbrpt_merge.gif) on the toolbar, then add objects from the **Components** panel into the tabular cells and format them to customize the header and footer.
3. Select **Menu** > **File** > **Save As**. Server displays the Save As dialog box.
4. Select the type **Web Report Template (\*.wsld)**.
5. Type a name for the template in the **File Name** text box.
6. Select **Save** to save the page template.

## Dynamically Displaying the Company Logo

If a web report page template contains a company logo, you can display the logo dynamically in the report that uses the page template.

1. Select the company logo image in the report and then do either of the following:
   * Right-click the image and select **Properties** from the shortcut menu. Server displays the [Image Properties](https://devnet.logianalytics.com/hc/en-us/articles/5741429972759-Image-Properties) dialog box. Select the formula button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9905615792535/btn_wbrpt_fmla.gif) next to the **Image Name** text box.
   * Select **Menu** > **View** > **Inspector**. Server displays the **Inspector** panel. In the Properties sheet, select the formula button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9905577900311/btn_wbrpt_dynfml.gif) in the value cell of the **Image Name** property.
2. Do either of the following to change the image name.
   * Select a formula that returns an image source from the drop-down list. By default, there is no formula available in the list. If you want to use a formula to control the image source, you need to first bind a data source to the web report, then create a formula in the **Resources** panel to return an image source. For more information, see [Using formulas to control showing or hiding components](https://devnet.logianalytics.com/hc/en-us/articles/5741456024727-Making-Simple-Modifications-to-Web-Report-Components#Formula).
   * Select **<Edit Expression>** from the drop-down list. Server opens the [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/5741450053911-Formula-Editor-Properties). Edit an expression to control the image source.  

     Web Report Studio provides a built-in parameter named **JRS\_P\_LOGOURL**, which helps you to specify the image path easily. You can type **return @JRS\_P\_LOGOURL;** directly in the editing box of the Formula Editor to create the expression.
3. If you are in the Image Properties dialog box, select **OK** to accept the change.

   If the specified formula or expression uses parameters, Server adds the parameters to the [Parameters panel](https://devnet.logianalytics.com/hc/en-us/articles/5741490884759-Applying-Parameters-to-Web-Report). You can specify the parameter values in the panel to dynamically change the image.

If you are an administrator with the privilege of publishing resources, you can then [save the page template](#SaveAs) as a new one for future use, following the steps 3 to 6.

However, if you control the company logo of a page template by a formula, you might not create web reports successfully using the page template. In this case, you can use the [When web report template cannot work properly Logi Report should](https://devnet.logianalytics.com/hc/en-us/articles/5741421831831-Web-Report-Studio-Profile-Properties#Template) property in the Web Report Studio profile to determine what you want Logi Report to do.

## Setting the Default Page Template for Quick-start Web Reports

For web reports that you create using the quick start method, you can select a default page template in the Web Report Studio profile in advance to apply to them.

Anyone can select a default page template for themselves:

1. Navigate to the **My Profile** > **Customize Profile** page.
2. Select **Customize Profile**. Server displays the [Customize Profile dialog box](https://devnet.logianalytics.com/hc/en-us/articles/7985371543191-Customize-Profile-Dialog-Box-Properties).
3. Select **Enable Customize Properties**.
4. Select **Web Report Studio**
5. Select a page template from the **Web Report Page Template for Quick Start** drop-down list.
6. Select **OK** to apply your change.

Administrators can select a default page template for all users:

1. Navigate to the **Administration** > **Server Profile** > **Customize Profile** > **Web Report Studio** tab.
2. Select **New Profile** if you want to create a new profile or select **Edit** to update an existing profile (later you need to make sure you select this profile as the default profile). Server displays the [Web Report Studio Profile dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741421831831-Web-Report-Studio-Profile-Properties).
3. Select **Properties**
4. Select a page template from the **Web Report Page Template for Quick Start** drop-down list.
5. Select **OK** to apply your change.

## Renaming and Removing Web Report Page Templates

Logi Report Server saves page templates in the `<install_root>\templates` folder. To rename or remove a web report page template, go to the folder, then rename or delete the template file (.wsld) and its image file (.wsld.png).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741464240919-Creating-Web-Reports-Using-the-Wizard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741484883735-Web-Report-Studio-Window-Elements)
