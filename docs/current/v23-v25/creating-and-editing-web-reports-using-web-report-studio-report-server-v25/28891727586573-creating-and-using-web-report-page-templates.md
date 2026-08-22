---
title: "Creating and Using Web Report Page Templates"
id: 28891727586573
section: "Creating and Editing Web Reports Using Web Report Studio Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891727586573-Creating-and-Using-Web-Report-Page-Templates
updated_at: 2026-02-26T02:14:03Z
source_host: docs-report.zendesk.com
---
# 
Creating and Using Web Report Page Templates

You can create web report page templates to include standard features such as the company logo, company name, and privacy notices, and apply them to web reports you create. This topic describes how you can create, use, rename, and delete web report page templates.

This topic contains the following sections:

- Creating Web Report Page Templates

- Dynamically Displaying the Company Logo

- Setting the Default Page Template for Quick-start Web Reports

- Renaming and Removing Web Report Page Templates

## 
Creating Web Report Page Templates

To create web report page templates, you should be an administrator with the privilege of publishing resources. 

To create a page template by customizing a built-in template in the Web Report Wizard: 

The Web Report Wizard provides sample page templates for you to define your templates based on.

- In the Page screen of the Web Report Wizard, make use of Template1 or Template2 to customize your  page templates. With Template1, you can add your company logo and a report title. With Template2, you can add more items such as company name, title, and report subtitle. 

- Use the ellipsis button  to load your company logo.

- Set the font properties for titles using .

- Select Save. Server displays the Save As dialog box.

- Select the type Web Report Template (*.wsld).

- Type a name for the template in the File Name text box.

- Select Save to save the page template.

To create a page template by editing a report in Web Report Studio:

- Open a report in Web Report Studio.

- Edit the header and footer of the report. The report header and footer are two tabulars. You can split or merge the tabular cells by selecting the Split button  or Merge button   on the toolbar, then add objects from the Components panel into the tabular cells and format them to customize the header and footer.

- Select Menu > File > Save As. Server displays the Save As dialog box.

- Select the type Web Report Template (*.wsld).

- Type a name for the template in the File Name text box.

- Select Save to save the page template.

## 
Dynamically Displaying the Company Logo

If a web report page template contains a company logo, you can display the logo dynamically in the report that uses the page template.

- Select the company logo image in the report and then do either of the following:
    
- Right-click the image and select Properties from the shortcut menu. Server displays the Image Properties dialog box. Select the formula button  next to the Image Name text box.

- Select Menu > View > Inspector. Server displays the Inspector panel. In the Properties sheet, select the formula button   in the value cell of the Image Name property.

- Do either of the following to change the image name.
    
- Select a formula that returns an image source from the drop-down list. By default, there is no formula available in the list. If you want to use a formula to control the image source, you need to first bind a data source to the web report, then create a formula in the Resources panel to return an image source. For more information, see Using formulas to control showing or hiding components.

- Select <Edit Expression> from the drop-down list. Server opens the Formula Editor. Edit an expression to control the image source.
Web Report Studio provides a built-in parameter named JRS_P_LOGOURL, which helps you to specify the image path easily. You can type return @JRS_P_LOGOURL; directly in the editing box of the Formula Editor to create the expression.

- If you are in the Image Properties dialog box, select OK to accept the change.
    If the specified formula or expression uses parameters, Server adds the parameters to the Parameters panel. You can specify the parameter values in the panel to dynamically change the image.

If you are an administrator with the privilege of publishing resources, you can then save the page template as a new one for future use, following the steps 3 to 6. 

However, if you control the company logo of a page template by a formula, you might not create web reports successfully using the page template. In this case, you can use the When web report template cannot work properly Report should property in the Web Report Studio profile to determine what you want Report to do.

## 
Setting the Default Page Template for Quick-start Web Reports

For web reports that you create using the quick start method, you can select a default page template in the Web Report Studio profile in advance to apply to them.

Anyone can select a default page template for themselves: 

- Navigate to the My Profile > Customize Profile page.

- Select Customize Profile. Server displays the Customize Profile dialog box.

- Select Enable Customize Properties.

- Select Web Report Studio

- Select a page template from the Web Report Page Template for Quick Start drop-down list. 

- Select OK to apply your change.

Administrators can select a default page template for all users: 

- Navigate to the Administration > Server Profile > Customize Profile > Web Report Studio tab.

- Select New Profile if you want to create a new profile or select Edit to update an existing profile (later you need to make sure you select this profile as the default profile). Server displays the Web Report Studio Profile dialog box. 

- Select Properties

- Select a page template from the Web Report Page Template for Quick Start drop-down list. 

- Select OK to apply your change.
            

## 
Renaming and Removing Web Report Page Templates

Report Server saves page templates in the <install_root>\templates folder. To rename or remove a web report page template, go to the folder, then rename or delete the template file (.wsld) and its image file (.wsld.png).
