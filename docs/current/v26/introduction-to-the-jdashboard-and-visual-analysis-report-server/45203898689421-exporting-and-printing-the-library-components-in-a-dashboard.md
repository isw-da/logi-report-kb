---
title: "Exporting and Printing the Library Components in a Dashboard"
id: 45203898689421
section: "Introduction to the JDashboard and Visual Analysis Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203898689421-Exporting-and-Printing-the-Library-Components-in-a-Dashboard
updated_at: 2026-04-30T14:08:06Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Exporting and Printing the Library Components in a Dashboard 

You can export and print library components visible in the page panel, for example, library components that you created using Report Designer and then inserted into dashboards via the Resources panel. This topic describes how you can export and print library components in a dashboard, using either the system layout or customized layout.

When you export or print the library components in a dashboard, you can choose whether to use the system layout or customize the layout by yourself. In the system layout, Report will calculate the positions of the library components in the dashboard following certain rule. If you are not satisfied with the system layout, you can customize the layout by yourself to determine the position of each library component and specify whether to export or print all the data of a table/crosstab or just the current page of the table/crosstab displayed in the dashboard. You can save the customized layout for all users who can access the dashboard.

This topic contains the following sections:

- Exporting the Library Components in a Dashboard Using the System Layout

- Exporting the Library Components in a Dashboard Using a Customized Layout

- Exporting a Single Library Component Using a Convenient Way

- Printing the Library Components in a Dashboard Using the System Layout

- Printing the Library Components in a Dashboard Using a Customized Layout

## 
Exporting the Library Components in a Dashboard Using the System Layout

- Take either of the following ways:
                
- Select the Export button  on the toolbar.

- Select the Options button  on the toolbar and then select Export from the option list. 

JDashboard displays the Export dialog box. 

- JDashboard selects the System Layout item as the layout by default.
    

JDashboard displays the preview of the layout in the preview panel on the right. Sometimes you may find that the layout is a little different from what you see in the dashboard.

- In the Resources box, select the library components you want to export. By default, JDashboard lists and selects all exportable library components.

- The order of the library components in the Resources box determines the order in which JDashboard export them. You can select  and  to adjust the exporting order. 

- Select the Show Component Title option if you want to show the library component titles in the exported output.

- You can select the page navigation buttons on the toolbar of the preview panel to browse the pages.

- Select the Page Setup icon  on the toolbar. JDashboard displays the Page Setup dialog box. 

- Set the page properties for the exported output file, such as page size and margins. You can either define the page properties generally for all export formats or customize the page properties for each export format as you want. 

- 
Select the Export icon . JDashboard displays the Export dialog box.

- From the Export File Format drop-down list, select the format to which you want to export the library components. For a format other than XML, JDashboard will export all the selected library components into one single file. For XML, JDashboard will export each library component to a separate XML file. When the exported output contains more than one file, JDashboard will zip all the files.

- In the File Name text box, specify the name of the exported output file, which could be either a single file or a zipped package name. 

- Select Run Linked Report if you need to include linked report in the exported output file. 

- Select OK to start exporting.

## 
Exporting the Library Components in a Dashboard Using a Customized Layout

- Select the Export button  on the toolbar. JDashboard displays the Export dialog box. 

- Select Customize Layout from the Layout drop-down list. You can also select an existing customized layout to modify it.
    

- Select the Show Component Title option if you want to show the library component titles in the exported output.

- Select the Page Setup icon  on the toolbar. JDashboard displays the Page Setup dialog box.
			

- Set the page properties for the exported output file, such as page size and margins.

- In the Design tab, customize the layout of the library components by making use of the following operations.
 JDashboard arranges the library components using a tabular with each cell holding one component.
    
- Split or merge cells using the toolbar icons: Horizontal Split, Merge, and Vertical Split.

- Drag a library component from the Resources box into a blank cell in the Design tab. A cell can hold only one library component. 

- Delete a library component from a tabular cell using the shortcut menu option Remove. 

- For a table or crosstab, JDashboard will only export its current view of data as displayed in the dashboard by default. If you want to export its full data, right-click on the table or crosstab and select Filter from the drop-down list. JDashboard displays the Filter dialog box. Switch from Current View to All and then select OK.

- Select the View tab to preview the layout. You can browse the pages and zoom in/out by selecting the corresponding toolbar buttons.

- 
If you are satisfied with the layout and would like to save it for future use, select the Save icon  or the Save As icon on the toolbar. JDashboard displays the Save As dialog box. Provide a name for the layout and select OK. JDashboard displays the customized layouts you saved in the Layout drop-down list to all users who can access the dashboard. For each of them, you can edit its name or delete it using the two icons - Rename and Delete - appearing on the right when the mouse hovers over the layout item in the drop-down list.

- Select the Export icon . JDashboard displays the Export dialog box.

- Do the last setting and start exporting.

## 
Exporting a Single Library Component Using a Convenient Way

If you just want to export a single library component, you can use a more convenient method.

- Select the Options icon  on the component title bar and then select Export from the drop-down menu. JDashboard displays the Export dialog box.
      

- Choose the format to which you want to export the library component.

- Select OK.

However, using this method, if the library component is linked with other reports, you cannot control whether to generate the linked reports while exporting. JDashboard will not include the linked reports in the exported output.

## 
Printing the Library Components in a Dashboard Using the System Layout

- Take either of the following ways:
                
- Select the Print button  on the toolbar.

- Select the Options button  on the toolbar and then select Print from the option list. 

JDashboard displays the Print dialog box.

- JDashboard selects System Layout as the Layout type by default.
    

JDashboard displays the preview of the layout in the preview panel on the right. Sometimes you may find that the layout is a little different from what you see in the dashboard.

- In the Resources box, select the library components you want to print. By default, JDashboard lists and selects all printable library components.

- The order of the library components in the Resources box determines the order in which JDashboard will print them. You can select  and  to adjust the printing order. 

- Select Show Component Title if you want to show the library component titles in the printed output.

- From the Printer drop-down list, select the printer you want to use. JDashboard lists the printers the web browser can access here. If you want to download the library components to a PDF or HTML file and then use your local printer to print the file, select Save as PDF or Save as HTML.

- If you select a printer, you can select the Properties link to specify the printing properties in the Printer Properties dialog box.

- Define the number of copies you want to print accordingly. 

- Specify the page orientation and paper type for the printed file. You can select the More Settings  link to set more page properties such as paper size and margins in the Page Setup dialog box.

- Select the page navigation buttons on the toolbar of the preview panel to browse the pages.

- Select the Print icon  on the toolbar to start printing. If you have selected Save as PDF or Save as HTML in the Printer drop-down list, JDashboard will open the output file in an associated program with which you can print it to a printer.

## 
Printing the Library Components in a Dashboard Using a Customized Layout

- Select the Print button  on the toolbar. JDashboard displays the Print dialog box.                

- Select Customize Layout from the Layout drop-down list. You can also select an existing customized layout to modify it.
    

- Do the same as described in steps 5 to 10 of the preceding system layout procedure. 

- In the Design tab, customize the layout of the library components, then preview it in the View tab. For more information, see Exporting the Library Components in a Dashboard Using a Customized Layout.

- Select the Print icon  on the toolbar to start printing. If you have selected Save as PDF or Save as HTML in the Printer drop-down list, JDashboard will open the output file in an associated program with which you can print it to a printer.
