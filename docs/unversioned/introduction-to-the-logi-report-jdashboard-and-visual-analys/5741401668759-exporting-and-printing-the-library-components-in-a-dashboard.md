---
title: "Exporting and Printing the Library Components in a Dashboard"
id: 5741401668759
section: "Introduction to the Logi Report JDashboard and Visual Analysis Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741401668759-Exporting-and-Printing-the-Library-Components-in-a-Dashboard
updated_at: 2022-10-31T17:16:05Z
---

# Exporting and Printing the Library Components in a Dashboard

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741423625879-Specifying-Parameter-Values-for-a-Dashboard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741396506647-Running-and-Editing-Reports-in-JDashboard)

# Exporting and Printing the Library Components in a Dashboard

You can export and print library components visible in the page panel, for example, library components that you created using Logi Report Designer and then inserted into dashboards via the Resources panel. This topic describes how you can export and print library components in a dashboard, using either the system layout or customized layout.

When you export or print the library components in a dashboard, you can choose whether to use the system layout or customize the layout by yourself. In the system layout, Logi Report will calculate the positions of the library components in the dashboard following certain rule. If you are not satisfied with the system layout, you can customize the layout by yourself to determine the position of each library component and specify whether to export or print all the data of a table/crosstab or just the current page of the table/crosstab displayed in the dashboard. You can save the customized layout for all users who can access the dashboard.

This topic contains the following sections:

* [Exporting the Library Components in a Dashboard Using the System Layout](#ExportSystem)
* [Exporting the Library Components in a Dashboard Using a Customized Layout](#ExportCustom)
* [Exporting a Single Library Component Using a Convenient Way](#ExportSingle)
* [Printing the Library Components in a Dashboard Using the System Layout](#PrintSystem)
* [Printing the Library Components in a Dashboard Using a Customized Layout](#PrintCustom)

## Exporting the Library Components in a Dashboard Using the System Layout

1. Take either of the following ways:
   * Select the **Export** button ![Export button](https://devnet.logianalytics.com/hc/article_attachments/9905578054551/btn_expt.gif) on the toolbar.
   * Select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/9905759210647/btn_dshbrd_optn.gif) on the toolbar and then select **Export** from the option list.

   JDashboard displays the [Export](https://devnet.logianalytics.com/hc/en-us/articles/5741426133271-Export-Dialog-Box-Properties#Dashboard) dialog box.
2. JDashboard selects the **System Layout** item as the layout by default.

   ![Export dialog - System Layout](https://devnet.logianalytics.com/hc/article_attachments/9905818178583/expt_dshbd_sys.gif)

   JDashboard displays the preview of the layout in the preview panel on the right. Sometimes you may find that the layout is a little different from what you see in the dashboard.
3. In the **Resources** box, select the library components you want to export. By default, JDashboard lists and selects all exportable library components.
4. The order of the library components in the **Resources** box determines the order in which JDashboard export them. You can select ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif) and ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif) to adjust the exporting order.
5. Select the **Show Component Title** option if you want to show the library component titles in the exported output.
6. You can select the page navigation buttons on the toolbar of the preview panel to browse the pages.
7. Select the **Page Setup** icon ![Page Setup button](https://devnet.logianalytics.com/hc/article_attachments/9905737759767/btn_dshbrd_pgstup.gif) on the toolbar. JDashboard displays the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/5741419794839-Page-Setup-Dialog-Box-Properties#Export) dialog box.

   ![Page Setup dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/9905759812759/pgstup_gnrl.gif)
8. Set the page properties for the exported output file, such as page size and margins. You can either define the page properties generally for all export formats or customize the page properties for each export format as you want.
9. Select the **Export** icon ![Export button](https://devnet.logianalytics.com/hc/article_attachments/9905578054551/btn_expt.gif). JDashboard displays the **Export** dialog box.
10. From the **Export File Format** drop-down list, select the format to which you want to export the library components. For a format other than XML, JDashboard will export all the selected library components into one single file. For XML, JDashboard will export each library component to a separate XML file. When the exported output contains more than one file, JDashboard will zip all the files.
11. In the **File Name** text box, specify the name of the exported output file, which could be either a single file or a zipped package name.
12. Select **Run Linked Report** if you need to include linked report in the exported output file.
13. Select **OK** to start exporting.

## Exporting the Library Components in a Dashboard Using a Customized Layout

1. Select the **Export** button ![Export button](https://devnet.logianalytics.com/hc/article_attachments/9905578054551/btn_expt.gif) on the toolbar. JDashboard displays the [Export](https://devnet.logianalytics.com/hc/en-us/articles/5741426133271-Export-Dialog-Box-Properties#Dashboard) dialog box.
2. Select **Customize Layout** from the **Layout** drop-down list. You can also select an existing customized layout to modify it.

   ![Export dialog - Customize Layout](https://devnet.logianalytics.com/hc/article_attachments/9905760582679/expt_dshbd.gif)
3. Select the **Show Component Title** option if you want to show the library component titles in the exported output.
4. Select the **Page Setup** icon ![Page Setup button](https://devnet.logianalytics.com/hc/article_attachments/9905737759767/btn_dshbrd_pgstup.gif) on the toolbar. JDashboard displays the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/5741419794839-Page-Setup-Dialog-Box-Properties#Export) dialog box.

   ![Page Setup dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/9905759812759/pgstup_gnrl.gif)
5. Set the page properties for the exported output file, such as page size and margins.
6. In the **Design** tab, customize the layout of the library components by making use of the following operations.
   JDashboard arranges the library components using a tabular with each cell holding one component.
   * Split or merge cells using the toolbar icons: **Horizontal Split****![Horizontal Split button](https://devnet.logianalytics.com/hc/article_attachments/9905737778711/btn_dshbrd_splth.gif)**, **Merge****![Merge button](https://devnet.logianalytics.com/hc/article_attachments/9905759670807/btn_dshbrd_merge.gif)**, and **Vertical Split****![Vertical Split button](https://devnet.logianalytics.com/hc/article_attachments/9905737813655/btn_dshbrd_spltv.gif)**.
   * Drag a library component from the **Resources** box into a blank cell in the **Design** tab. A cell can hold only one library component.
   * Delete a library component from a tabular cell using the shortcut menu option **Remove**.
   * For a table or crosstab, JDashboard will only export its current view of data as displayed in the dashboard by default. If you want to export its full data, right-click on the table or crosstab and select **Filter** from the drop-down list. JDashboard displays the [Filter](https://devnet.logianalytics.com/hc/en-us/articles/5741441502359-Filter-Dialog-Box-Properties) dialog box. Switch from **Current View** to **All** and then select **OK**.

     ![Filter dialog](https://devnet.logianalytics.com/hc/article_attachments/9905772181271/fltr.gif)
7. Select the **View** tab to preview the layout. You can browse the pages and zoom in/out by selecting the corresponding toolbar buttons.
8. If you are satisfied with the layout and would like to save it for future use, select the **Save** icon ![Save button](https://devnet.logianalytics.com/hc/article_attachments/9905577991703/btn_save.gif) or the **Save As** icon**![Save As button](https://devnet.logianalytics.com/hc/article_attachments/9905615943319/btn_saveas.gif)** on the toolbar. JDashboard displays the [Save As](https://devnet.logianalytics.com/hc/en-us/articles/5741405177239-Save-As-Dialog-Box-Properties) dialog box. Provide a name for the layout and select **OK**. JDashboard displays the customized layouts you saved in the **Layout** drop-down list to all users who can access the dashboard. For each of them, you can edit its name or delete it using the two icons - **Rename**![Rename icon](https://devnet.logianalytics.com/hc/article_attachments/9905779615511/btn_dshbrd_rename.gif) and **Delete**![Delete icon](https://devnet.logianalytics.com/hc/article_attachments/9905616261527/btn_dltobj.gif) - appearing on the right when the mouse hovers over the layout item in the drop-down list.

   ![Layout Drop-down List](https://devnet.logianalytics.com/hc/article_attachments/9905759609367/dshbrd_expt_layout.gif)
9. Select the **Export** icon ![Export button](https://devnet.logianalytics.com/hc/article_attachments/9905578054551/btn_expt.gif). JDashboard displays the Export dialog box.
10. [Do the last setting and start exporting.](#Export)

## Exporting a Single Library Component Using a Convenient Way

If you just want to export a single library component, you can use a more convenient method.

1. Select the **Options** icon ![Options Icon](https://devnet.logianalytics.com/hc/article_attachments/9905772219671/btn_dshbrd_more.gif) on the [component title bar](https://devnet.logianalytics.com/hc/en-us/articles/5741401720599-General-Operations-in-JDashboard#TitleBar) and then select **Export** from the drop-down menu. JDashboard displays the Export dialog box.

   ![Export dialog](https://devnet.logianalytics.com/hc/article_attachments/9905760554391/expt_lc.gif)
2. Choose the format to which you want to export the library component.
3. Select **OK**.

However, using this method, if the library component is linked with other reports, you cannot control whether to generate the linked reports while exporting. JDashboard will not include the linked reports in the exported output.

## Printing the Library Components in a Dashboard Using the System Layout

1. Take either of the following ways:
   * Select the ****Print**** button **![Print button](https://devnet.logianalytics.com/hc/article_attachments/9905616008343/btn_print.gif)** on the toolbar.
   * Select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/9905759210647/btn_dshbrd_optn.gif) on the toolbar and then select **Print** from the option list.

   JDashboard displays the [Print](https://devnet.logianalytics.com/hc/en-us/articles/5741441698711-Print-Dialog-Box-Properties) dialog box.
2. JDashboard selects **System Layout** as the Layout type by default.

   ![Print dialog - System Layout](https://devnet.logianalytics.com/hc/article_attachments/9905818234007/prnt_sys.gif)

   JDashboard displays the preview of the layout in the preview panel on the right. Sometimes you may find that the layout is a little different from what you see in the dashboard.
3. In the **Resources** box, select the library components you want to print. By default, JDashboard lists and selects all printable library components.
4. The order of the library components in the Resources box determines the order in which JDashboard will print them. You can select ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif) and ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif) to adjust the printing order.
5. Select **Show Component Title** if you want to show the library component titles in the printed output.
6. From the **Printer** drop-down list, select the printer you want to use. JDashboard lists the printers the web browser can access here. If you want to download the library components to a PDF or HTML file and then use your local printer to print the file, select **Save as PDF** or **Save as HTML**.
7. If you select a printer, you can select the **Properties** link to specify the printing properties in the [Printer Properties](https://devnet.logianalytics.com/hc/en-us/articles/5741413067671-Printer-Properties) dialog box.
8. Define the number of copies you want to print accordingly.
9. Specify the page orientation and paper type for the printed file. You can select the **More Settings**  link to set more page properties such as paper size and margins in the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/5741419794839-Page-Setup-Dialog-Box-Properties#Print) dialog box.
10. Select the page navigation buttons on the toolbar of the preview panel to browse the pages.
11. Select the **Print** icon ![Print button](https://devnet.logianalytics.com/hc/article_attachments/9905616008343/btn_print.gif) on the toolbar to start printing. If you have selected **Save as PDF** or **Save as HTML** in the **Printer** drop-down list, JDashboard will open the output file in an associated program with which you can print it to a printer.

## Printing the Library Components in a Dashboard Using a Customized Layout

1. Select the ****Print**** button **![Print button](https://devnet.logianalytics.com/hc/article_attachments/9905616008343/btn_print.gif)** on the toolbar. JDashboard displays the [Print](https://devnet.logianalytics.com/hc/en-us/articles/5741441698711-Print-Dialog-Box-Properties) dialog box.
2. Select **Customize Layout** from the Layout drop-down list. You can also select an existing customized layout to modify it.

   ![Print dialog - Customize Layout](https://devnet.logianalytics.com/hc/article_attachments/9905737705367/prnt.gif)
3. Do the same as described in steps 5 to 10 of the preceding system layout procedure.
4. In the **Design** tab, customize the layout of the library components, then preview it in the **View** tab. For more information, see [Exporting the Library Components in a Dashboard Using a Customized Layout](#ExportCustom).
5. Select the **Print** icon ![Print button](https://devnet.logianalytics.com/hc/article_attachments/9905616008343/btn_print.gif) on the toolbar to start printing. If you have selected **Save as PDF** or **Save as HTML** in the **Printer** drop-down list, JDashboard will open the output file in an associated program with which you can print it to a printer.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741423625879-Specifying-Parameter-Values-for-a-Dashboard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741396506647-Running-and-Editing-Reports-in-JDashboard)
